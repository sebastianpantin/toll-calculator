# Toll fee calculator in python.

## Short description of implementation
I created two services for the assignment, one backend in Python and one frontend with React. The entire thing is runnable in docker compose where I
also implemented a reverse proxy using nginx for communication between backend and frontend. 

## Python backend
Since I didn't want to spend too much time I choose to use Python as that is what I'm using at my current workplace. The api framework used is called FastAPI. 
I tried to do as much typing as possible to increase the readability and maintainability of the code base, even though Python is not a typed language in that sense.
I implemented a few unit tests for the main class "TollCalculator" and some integration tests to show case how one would run these in this kind of environment.

## React frontend

My plan was to create a dashboard-like experience where you could view the toll events in different perspectives, for example to see how much toll a certain vehicle
pays per day/week/month/year but as I was running out of time (personal deadline). I instead just created a simple view where one can register toll events to showcase
connection between frontend and backend. The design is heavily inspired by standard chakra UI templates, since I'm pretty bad at designing stuff..

## How to run?
It should be enough to have the tools necessary to run `docker compose up`, for installation instructions I refer to [docker compose](https://docs.docker.com/compose/install/).

    1. Run `docker compose up` in the root folder
    2. Open `http://localhost:8000` in your browser to open the frontend
    3. In the Register tab in the left sidebar you can register events that will be saved to the database.
