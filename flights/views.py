from datetime import timezone
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
import pytz
from accounts.serializers import UserSerializer
from .models import Flight,FlightSeatManager,FlightBookinglog
from django.db import connection
from django.http import JsonResponse
from home.models import Userlog



# Create your views here.
@login_required(login_url='/accounts/login')
def flights(request):
    if request.user.is_authenticated :
       
        if request.method == "POST" :
            journey_source=request.POST['select_source']
            journey_destination=request.POST['select_destination']
            journey_date=request.POST['journey_date']
            journey_time=request.POST['journey_time']

            # print(" source : ",source , " destination : ",destination ," date : ",journey_date , "time : ",journey_time)
            try :
                with connection.cursor() as cursor:

                    flight_details_query=""" SELECT f.id,f.number,f.name,f.seats,f.departure_date,f.departure_time,
                                            (select c.name from flights_country c where c.id=f.source_id) as journey_source,
                                            (select c.name from flights_country c where c.id=f.destination_id) as journey_destination,
                                            (select count(seat) as available_seats from flights_flightseatmanager where flight_id=f.id and status != 1 ) as available_seats,
                                            
                                            CASE
                                                WHEN f.cancellation_period > CURRENT_TIMESTAMP THEN 1
                                                ELSE 0
                                            END AS is_booking_allowed
                                            FROM flights_flight f
                                            where f.source_id= %s and f.destination_id= %s and f.departure_date= %s and f.departure_time >= %s ;
                                            
                                            """
                    
                    cursor.execute(flight_details_query,(journey_source,journey_destination,journey_date,journey_time))
                    rows = cursor.fetchall()
                    
                    flight_details = []
                    for row in rows:
                        flight_detail = {
                            'id': row[0],
                            'number': row[1],
                            'name': row[2],
                            'seats': row[3],
                            'departure_date': row[4],
                            'departure_time': row[5],
                            'journey_source': row[6],
                            'journey_destination': row[7],
                            'available_seats': row[8],
                            'is_booking_allowed': row[9],
                        }
                        flight_details.append(flight_detail)
                    
                    user_serialized_data=UserSerializer(request.user);
                    

                    response = {
                        'user': user_serialized_data.data,
                        'flight': flight_details
                    }
                    
                    return render(request,'flights.html', {'response': response })
                
            except Exception as e :
                print(e)
                messages.info(request, "An error encountered, please try again.")
                return redirect('home-page')
        
        else:
            messages.info(request, "An error encountered, please try again.")
            return redirect('home-page')
    else:
        messages.info(request, "Access denied, Please login.") 
        return redirect('index-page')           

@login_required(login_url='/accounts/login')
def bookflight(request):
    if request.user.is_authenticated :
        user_id=request.POST['user_id']
        flight_id=request.POST['flight_id']
        
        try :
                with connection.cursor() as cursor:

                    seat_status_query=""" SELECT id ,seat as available_seat
                                          from flights_flightseatmanager
                                          where 
                                          flight_id= %s and status != 1
                                          order by seat 
                                          limit 1

                                      """
                    
                    cursor.execute(seat_status_query,(flight_id,))
                    seat_status = cursor.fetchall()
                    
                   
                    if(not seat_status):
                        
                        response={
                            'status':0,
                            'message':'Sorry remaining seats are already occupied.'
                        }
                        return JsonResponse(response)         

                    # seat allocation..
                   
                    allot_seat=FlightSeatManager.objects.get(id=str(seat_status[0][0]))
                    allot_seat.status=1
                    allot_seat.save()

                    booking_log=FlightBookinglog.objects.create(seat=seat_status[0][1],status=1,flight_id=flight_id,user_id=user_id)

                    user_log=Userlog.objects.create(seat=seat_status[0][1],status=1,flight_id=flight_id,user_id=user_id)
                    
                    response={
                            'status':1,
                            'message':'Your seat has been booked successfully.'
                        }
                    return JsonResponse(response)

                    
        except Exception as e:
            print(e)
            response={
                        'status':-1,
                        'message':'An error encountered, please try again.'
                    }
            return JsonResponse(response) 

    else:
        messages.info(request, "Access denied, Please login.") 
        return redirect('index-page')       

def userlogout(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect('index-page')
