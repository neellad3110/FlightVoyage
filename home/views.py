from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from accounts.serializers import UserSerializer
from django.http import JsonResponse
from django.db import connection
from datetime import datetime
from FlightVoyage.settings import TIME_ZONE as local_timezone
from .models import Userlog
from flights.models import Flight,FlightBookinglog,FlightSeatManager
from flights.models import Country 


# Create your views here.
@login_required(login_url='/accounts/login')
def home(request):
    if request.user.is_authenticated :
      try:
            serialized_user=UserSerializer(request.user);
            countries=Country.objects.all().values('id','name').order_by('name')

            response={
                  'user': serialized_user.data,
                  'countries' : countries
            }

            return render(request,'home.html', {'response': response}) 
      except Exception as e:
            messages.info(request, "An error encountered, please try again.")
            return redirect('index-page')
    
    else:
      messages.info(request, "Access denied, Please login.") 
      return redirect('index-page')
    
@login_required(login_url='/accounts/login')
def mybookings(request):
    return render(request,"bookings.html")  

@login_required(login_url='/accounts/login')
def mybookings_history(request):
      if request.user.is_authenticated :
            
            if request.method=='POST':

                  flight_id=request.POST['flight_id']
                  seat=request.POST['seat']
                  current_time = datetime.now()

                  try :

                        flight_cancellation_confirm=Flight.objects.get(id=flight_id,cancellation_period__gt=current_time)

                        if(flight_cancellation_confirm):

                              # update seat deallocation
                              flight_seat_manager=FlightSeatManager.objects.get(flight_id=flight_id,seat=seat)
                              flight_seat_manager.status=0
                              flight_seat_manager.save()

                              # adding new flight log
                              FlightBookinglog.objects.create(user_id=request.user.id,flight_id=flight_id,seat=seat,status=-1)

                              # updating user log
                              user_log=Userlog.objects.get(user_id=request.user.id,flight_id=flight_id,seat=seat)
                              user_log.status=-1
                              user_log.save()
                              
                              response={
                                    'status':1,
                                    'message':'Your Booking is cancelled successfully',
                              }

                        else:
                              response={
                                    'status':0,
                                    'message':'Your Cancellation period is over. Kindly refresh the page.'
                              }
                              return JsonResponse(response)
                                                 
                  except Exception as e:
                        response={
                                    'status':-1,
                                    'message':'An error encountered, please try again.'
                              }
                        return JsonResponse(response)
            
            else :      


                  user_id=request.user.id
            
                  try :
                        with connection.cursor() as cursor:

                             
                              flight_details_query=""" SELECT f.id,f.number,f.name,f.departure_date,f.departure_time,
                                                      (select c.name from flights_country c where c.id=f.source_id) as journey_source,
                                                      (select c.name from flights_country c where c.id=f.destination_id) as journey_destination,
                                                      ul.seat,ul.status,
                                                      ul.created_at AT TIME ZONE %s as booking_datetime,
                                                      ul.modified_at AT TIME ZONE %s as modified_at,

                                                      CASE
                                                            WHEN ul.status = 1 THEN 
                                                                  CASE
                                                                        WHEN f.cancellation_period > CURRENT_TIMESTAMP THEN 1
                                                                        ELSE 0
                                                                  END
                                                            ELSE 
                                                                  NULL 
                                                      END AS request_cancellation
                                                
                                                      FROM flights_flight f inner join home_userlog ul on f.id=ul.flight_id
                                                      where  ul.user_id = %s order by ul.created_at desc ;
                                                      
                                                      """
                              
                              cursor.execute(flight_details_query,(local_timezone,local_timezone,user_id,))
                              rows = cursor.fetchall()
                              
                              flight_details = []
                              for row in rows:
                                    flight_detail = {
                                    'id': row[0],
                                    'number': row[1],
                                    'name': row[2],
                                    'departure_date': row[3],
                                    'departure_time': row[4],
                                    'journey_source': row[5],
                                    'journey_destination': row[6],
                                    'seat': row[7],
                                    'status': row[8],
                                    'booking_datetime': formatdatetime(row[9]),
                                    'modified_at': formatdatetime(row[10]),
                                    'request_cancellation': row[11],
                                    }
                                    flight_details.append(flight_detail)
                              
                              response={
                                    'status':1,
                                    'message':'success',
                                    'flight': flight_details
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
	messages.info(request, "You have been logged out.") 
	return redirect('index-page')


def formatdatetime(value):
    
      datetime_value = datetime.strptime(str(value), "%Y-%m-%d %H:%M:%S.%f")
      
      formatted_datetime = datetime_value.strftime("%Y-%m-%d , %H:%M")
      return formatted_datetime