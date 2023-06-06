# pb-full-stack-brooks

## Description
pb-full-stack-brooks is a simple, full stack web application that utilizes real whale sighting data from the Farallon Islands lighthouse, located just miles off the coast of San Francisco, CA. The app provides users with a visual interface to explore and analyze whale sighting information in the area. 

## Stack
The application is built using the following technologies:

### UI
* Angular + TypeScript + Bootstrap

### Server side code
* Gunicorn + Flask + Python

### Database
* PostgreSQL

## Installation

### Prerequisites
* Python 3.x
* PostgreSQL
### Clone the repository

`git clone https://github.com/jackbrooks11/pb-full-stack-brooks.git`

`cd pb-full-stack-brooks`

### Set up the backend

`cd backend`

`pipenv install`

`pipenv shell`

### Set up the database

Create a PostgreSQL database and update the DATABASE_URL with your database connection details

`export DATABASE_URL="postgresql://<username>:<password>@<host>:<port>/<dbname>"`

### Start the backend server

`gunicorn -w 1 "app:create_app()"`

### Set up the frontend

Open a new terminal window and navigate to the frontend directory

`cd ../frontend`

`npm install`

### Start the frontend development server

`ng serve`

### Access the application

Open your web browser and visit http://localhost:4200 to access the pb-full-stack-brooks application