<h1 align="center">Flight Voyage</h1>

FlightVoyage is a demonstration of a flight management application built on Django, offering seamless booking experiences for passengers and robust management tools for airline administrators. With FlightVoyage, users can effortlessly search for flights based on their preferred source, destination, date, and time, making travel planning a breeze.

<hr>

## Table of Contents:

- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
  1. [Docker Containers](#docker-containers) 
        - [Docker Installation](#docker-installation)
        - [Build and run commands](#build-and-run-commands)
  2. [Manual Installtion](#manual-installation) 
        - [Python installation](#python-installation)
        - [PostgreSQL installation](#postgresql-installation)
        - [Django Configurations](#django-configurations)

- [Screenshots](#screenshots)
     
- [References](#references)
<hr>

## Technology Stack

<div align="center"> 

[![HTML](https://img.shields.io/badge/HTML-5-orange.svg)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS](https://img.shields.io/badge/CSS-3-blue.svg)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple.svg)](https://getbootstrap.com/)
[![jQuery](https://img.shields.io/badge/jQuery-3.6.0-blue.svg)](https://jquery.com/)
[![AJAX](https://img.shields.io/badge/AJAX-Asynchronous-green.svg)](https://developer.mozilla.org/en-US/docs/Web/Guide/AJAX)


[![Python](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-3.2-green.svg)](https://www.djangoproject.com/)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow.svg)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13-blue.svg)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-20.10.11-blue.svg)](https://www.docker.com/)
[![JSON](https://img.shields.io/badge/JSON-Data-blue.svg)](https://www.json.org/)

</div> 
<hr>

## Key Features:

- Flight Search: Passengers can easily search for flights based on their preferred source, destination, date, and time. The intuitive search interface provides real-time availability.

- Booking: Once the desired flight is found, passengers can proceed to book their tickets securely through the platform.
    - Booking is available as per vacancy as well as 24h prior to the flight depature.

- Booking History: Users have access to their booking history, enabling them to view past and upcoming flights. This feature provides a convenient way for users to track their travel history and manage future plans effectively.
    
    - Cancellation is applicable 24h prior to the flight departure. 

- Admin Panel: A comprehensive Django-based admin panel for administrators to manage flights, user bookings, logs, and system configurations. Admins can efficiently handle flight schedules, view booking details, and perform various management tasks.


## Installation

1. Fork this repository to your github account
2. Clone the forked repository and proceed with steps mentioned below

```
git clone https://github.com/neellad3110/FlightVoyage.git
```

### Docker Containers

<img width="1470" alt="Docker" src="https://github.com/neellad3110/FlightVoyage/assets/92388308/8ec1c274-e431-436a-9324-2b263e4fb950">

#### What is Docker ?

[Docker](https://www.docker.com/get-started/) is a software platform that allows you to build, test, and deploy applications quickly. Docker packages software into standardized units called containers that have everything the software needs to run including libraries, system tools, code, and runtime. Using Docker, you can quickly deploy and scale applications into any environment and know your code will run.

#### How does docker works ?

Docker works by providing a standard way to run your code. Docker is an operating system for containers. Similar to how a virtual machine virtualizes (removes the need to directly manage) server hardware, containers virtualize the operating system of a server. Docker is installed on each server and provides simple commands you can use to build, start, or stop containers.

#### Docker Installation
> [!TIP]
> Check out the [docker documentation](https://docs.docker.com/desktop/install/windows-install/) to set up in your machine.  


> [!IMPORTANT]
> Before building up containers, verify database service configuration from [project settings.py](FlightVoyage/settings.py) file and [docker-compose.yaml](docker-compose.yaml)

Firstly, open your [docker-compose.yaml](docker-compose.yaml) file.

```
  db:       <-- postgres service name

    image: postgres
    environment:
      POSTGRES_DB : FlightVoyage
      POSTGRES_USER : postgres
      POSTGRES_PASSWORD : postgres@123
      
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      retries: 5  
    
    ports:
      - "5432:5432"
```

Now, open your [settings.py](FlightVoyage/settings.py) file and verify database configuration as per mentioned above.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'FlightVoyage',
        'USER': 'postgres',
        'PASSWORD': 'postgres@123',

        'HOST': 'db',    <---- Docker postgres service name

        'PORT': '5432',
    }

}
```

#### Build and run commands.

1. Open a terminal in your project directory and run:

```
docker-compose build
```
<img width="1477" alt="Screenshot 2024-03-08 at 23 27 30" src="https://github.com/neellad3110/FlightVoyage/assets/92388308/c55ef275-de23-4a8f-852a-813160efd7cb">

>The `docker-compose build` is a command used to build Docker images for services defined in a `docker-compose.yml` file. It reads the Dockerfile in each service's build context and creates Docker images accordingly. This command is useful for preparing Docker images before starting containers with docker-compose up.

2. Now run:

```
docker-compose up
```
Containers
<img width="1461" alt="Screenshot 2024-03-08 at 23 37 54" src="https://github.com/neellad3110/FlightVoyage/assets/92388308/eb38b02c-a0bd-455a-9a53-4a1f56312fc7">


<img width="1368" alt="Screenshot 2024-03-08 at 01 08 04" src="https://github.com/neellad3110/FlightVoyage/assets/92388308/7eb31c41-d7a3-4abe-b00e-b8b89242d5ca">

<hr>
<br>
State of Containers
<img width="1493" alt="Screenshot 2024-03-08 at 23 41 13" src="https://github.com/neellad3110/FlightVoyage/assets/92388308/5bdeb44c-c561-4d3e-9e8b-1bc362c191f2">


>The `docker-compose up` command is used to start services defined in your` docker-compose.yml` file. It reads the configuration from the `docker-compose.yml` file and creates and starts containers for all services defined within it. If the containers already exist, it will attempt to start them. If the images for the services have not been built yet, it will build them first before starting the containers.


>[!NOTE]
>To get the IP address and port number of the containers.

Open a new terminal and run :

```
docker ps
```
<img width="1399" alt="Screenshot 2024-03-08 at 23 53 30" src="https://github.com/neellad3110/FlightVoyage/assets/92388308/b58add59-982f-4ba1-afe0-d0ec6b2c92b3">
<br>
As per above information

> At [0.0.0.0:8000](http://0.0.0.0:8000/)  : Our Django Web application is accessible.
<hr>
<br>
<img width="1268" alt="Screenshot 2024-03-09 at 00 03 23" src="https://github.com/neellad3110/FlightVoyage/assets/92388308/6d757367-3f5b-4161-ac7a-1236cb26f9fe">

<hr>
<br>

> At [0.0.0.0:5050](http://0.0.0.0:5050/)  : Our PgAdmin web panel is accessible.

>[!NOTE]
> Use credentials mentioned on [docker-compose.yaml](docker-compose.yaml) for pgadmin service.

>[!CAUTION]
> STOP all the services running on port 5432 such as local postgres or any other services to avoid connection error.

<img width="1159" alt="Screenshot 2024-03-08 at 00 54 27" src="https://github.com/neellad3110/FlightVoyage/assets/92388308/67bcb6ee-8de0-4043-9206-896b74c329be">

<hr>
<br>

Register new server by using the DATABASE configuration mentioned in [settings.py](FlightVoyage/settings.py)

<img width="1467" alt="Screenshot 2024-03-08 at 00 55 32" src="https://github.com/neellad3110/FlightVoyage/assets/92388308/7c9b2381-55d0-4194-a063-ef799546ac63">

<img width="1467" alt="Screenshot 2024-03-08 at 00 57 05" src="https://github.com/neellad3110/FlightVoyage/assets/92388308/d455aab0-43fd-4c89-ac3e-546c6d3ac040">
<hr>
<br>

> At [0.0.0.0:8000/admin/](http://0.0.0.0:8000/admin/)  : Our Django Admin web panel is accessible.

<img width="1470" alt="Screenshot 2024-03-07 at 19 41 54" src="https://github.com/neellad3110/FlightVoyage/assets/92388308/a9abdaed-e556-4151-8ba1-3f668f1abbaf">

<hr>

### Manual Installation


#### Python installation

Head over to the [official Python website](https://www.python.org/downloads/) and download the installer
Also, be sure to have `git` donwloaded and available in your PATH as well.

#### PostgreSQL installation 

[PostgreSQL](https://www.postgresql.org/download/) is available for download as ready-to-use packages or installers for various platforms.

>[!TIP]
> Follow the complete installation guide from [here](https://www.w3schools.com/postgresql/postgresql_install.php)

After installtion, login to your pgAdmin. Expand `Servers` and `PostgreSQL`. Now right click on `Databases` then create a new database.

<img src="https://static.javatpoint.com/postgre/images/postgresql-create-database.png" />

#### Django Configurations

#### Virtual Environment (`venv`)

While there are a few ways to achieve a programming environment in Python, we’ll be using the venv module here, which is part of the standard Python 3 library. Let’s install venv by typing:

```
pip install virtualenv
```
Creating and entering a new virtual environment:
```
python -m venv env
source env/bin/activate
```
##### Running the project

Before running the project, We need to install required packages for the project from requirements.txt.
```
pip install -r requirements.txt
``` 
Now open project [settings.py](FlightVoyage/settings.py) file and update your database configuation in `DATABASES` part.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': localhost,
        'PORT': 5432,
        'USER': postgres,                               # pgAdmin username
        'PASSWORD': postgres@123,                      # pgAdmin passoword
        'NAME': FlightVoyage,                     # Database name
    }
}

```
Let's map your `Model` and create new `Relation` in database by migration.

```
python manage.py makemigrations
pythom manage.py migrate
```
Now lets dump the initials data to the database

```
python manage.py loaddata initials/accounts_initial_data.json
python manage.py loaddata initials/flights_initial_data.json
```

Finally start the server.
```
python manage.py runserver
```
>[!NOTE]
>Once the server has started up, you can visit it at [localhost:8000/](http://127.0.0.1:8000) , or [127.0.0.1:8000/](http://127.0.0.1:8000).

>[!NOTE]
For Admin Panel, you can visit it at [localhost:8000/admin](http://127.0.0.1:8000/admin) , or [127.0.0.1:8000/](http://127.0.0.1:8000/admin).

## Screenshots

### User Registration
<br>
<img width="1677" alt="Screenshot 2024-03-07 at 19 41 23" src="https://github.com/neellad3110/FlightVoyage/assets/92388308/a9ec08f9-6e40-4072-ae38-a0747a8167a4">
<hr>


### User Authentication
<br>
<img width="1680" alt="Screenshot 2024-03-07 at 19 41 08" src="https://github.com/neellad3110/FlightVoyage/assets/92388308/02dcb2e0-c1de-49e9-802e-ed4f245e15a3">
<hr>


### Home page
<br>
<img width="1680" alt="Screenshot 2024-03-07 at 19 35 28" src="https://github.com/neellad3110/FlightVoyage/assets/92388308/ea938f05-8e46-47e3-b8f9-0dc7ed5550fa">
<hr>
<br>

### Available flights page
<br>
<img width="1680" alt="Screenshot 2024-03-07 at 19 35 52" src="https://github.com/neellad3110/FlightVoyage/assets/92388308/cf7d2f46-1623-4f50-a153-a524faa5e8a3">
<hr>

#### Flights not available due to seats unavailability or post booking period.

<br>
<img width="1672" alt="Screenshot 2024-03-07 at 19 37 02" src="https://github.com/neellad3110/FlightVoyage/assets/92388308/701f9046-e3b4-447e-870c-b71655fa09bd">
<img width="1677" alt="Screenshot 2024-03-07 at 19 38 09" src="https://github.com/neellad3110/FlightVoyage/assets/92388308/3011093a-213d-4bb8-ab3a-8f8d2e4f703f">

<hr>

### My Bookings

<br>
<img width="1680" alt="Screenshot 2024-03-07 at 19 33 54" src="https://github.com/neellad3110/FlightVoyage/assets/92388308/d3d67cc8-ba6d-449a-a44f-396fdd84a949">

<hr>

#### When cancellation period is over.

<br>

<img width="1680" alt="Screenshot 2024-03-07 at 19 40 11" src="https://github.com/neellad3110/FlightVoyage/assets/92388308/194e6cf1-421d-4e7b-a10f-935a0e86c21f">

<hr>

#### When booking is cancelled .

<br>

<img width="1671" alt="Screenshot 2024-03-07 at 19 34 44" src="https://github.com/neellad3110/FlightVoyage/assets/92388308/dcb1ef7e-e11b-4f61-bf70-deb745dd1960">

<hr>

#### When booking is cancelled by Admin.

<br>

<img width="1664" alt="Screenshot 2024-03-07 at 19 34 59" src="https://github.com/neellad3110/FlightVoyage/assets/92388308/e4197906-ef87-4c26-901c-b5b1db8707d8">

<hr>

#### Admin Flight management.

<br>

<img width="1671" alt="Screenshot 2024-03-07 at 19 42 11" src="https://github.com/neellad3110/FlightVoyage/assets/92388308/c43714de-23aa-4992-a56c-c14248543454">
<img width="1680" alt="Screenshot 2024-03-07 at 19 46 05" src="https://github.com/neellad3110/FlightVoyage/assets/92388308/6f6c2f1f-7c14-4e62-aa2f-d5dfdd8f2d9d">

<hr>

### Admin User management
<br>

<img width="1470" alt="Screenshot 2024-03-07 at 19 41 54" src="https://github.com/neellad3110/FlightVoyage/assets/92388308/5f4194e2-f12d-4c22-8829-4d7dad1021d1">

<hr>

### Admin Flight log
<br>

<img width="1668" alt="Screenshot 2024-03-07 at 19 44 19" src="https://github.com/neellad3110/FlightVoyage/assets/92388308/e512a06f-740f-48a1-a875-640f727a0f02">

<hr>

## References 

1. Django Admin Panel Customization : https://realpython.com/customize-django-admin-python/

2. Django ORM : https://www.javatpoint.com/django-orm-queries

3. Dockerizartion Django app with PostgreSQL : https://www.youtube.com/watch?v=Pox10kU7d2c&t=1093s
