# Sports API

Full Stack Sports Data Management System

## Description

This is a Full Stack application that provides a Sports Data Management System. The project consists of four major apps: ETL, Database, REST API, and Frontend.

The ETL (Extract, Transform, Load) app is responsible for handling the data pipeline. It extracts sports data from external sources, performs necessary transformations, and loads it into the database.

The Database app utilizes SQLite to store the sports data. It provides models and migrations for creating and managing the database schema. This app acts as the data layer for the project.

The REST API app serves as the core of the project, providing API endpoints to retrieve, create, update, and delete sports data. It utilizes Django REST Framework to facilitate the development of RESTful APIs.

The Frontend app is the user-facing part of the project. It's developed using HTML, CSS, and JavaScript. The frontend communicates with the REST API to fetch and display sports data to the users. It utilizes Bootstrap for responsive and user-friendly UI designs.

## Features

- Data pipeline (ETL) to extract, transform, and load sports data into the database.
- SQLite database for storing sports data.
- REST API with endpoints to retrieve, create, update, and delete sports data.
- Frontend website to display sports data to users.
- Interactive UI with DataTables integration for easy data viewing and searching.

## Installation

1. Clone the project repository.
2. Set up a virtual environment and activate it.
3. Install the required dependencies using pip.
4. Configure the database settings in the settings.py file of the Database app.
5. Run database migrations to create the necessary database schema.
6. Load initial data or run the ETL pipeline to populate the database.
7. Start the Django development server.
8. Access the website through the provided URL.

## Usage

### ETL

1. Execute the ETL pipeline to extract, transform, and load sports data into the database.

### Database

1. Use the provided models and migrations to manage the database schema.
2. Configure the database settings as per your requirements.
3. Run database migrations to create, modify, or delete tables.

### REST API

1. Use the provided API endpoints to interact with the sports data.
2. Refer to the API documentation for available endpoints and request/response formats.
3. Make HTTP requests to retrieve, create, update, or delete sports data.

### Frontend

1. Access the website through the provided URL.
2. Select a team from the dropdown to view their sports data.
3. The table will display the sports data, including ID, Date, Opponent, Result, Score, Opponent Score, Location, Total Wins, Total Losses, Divisional Wins, and Divisional Losses.
4. The table supports searching and sorting functionalities for better data exploration.

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite
- HTML
- CSS
- JavaScript
- Bootstrap

## Roadmap

- Implement user authentication and authorization for secure access to the application.
- Enhance the ETL pipeline to handle real-time updates and automate the data extraction process.
- Implement additional features like team statistics, player profiles, and live game updates.
- Improve frontend UI/UX for a more intuitive and visually appealing website.

