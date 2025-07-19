KPA Backend Assignment
Overview
This project implements two backend APIs using FastAPI (Python) and MySQL for the KPA Form Data assignment.
The APIs allow you to:

Add a user (POST /add-user)

Fetch all users (GET /users)

Tech Stack
Language: Python 3.13
Framework: FastAPI
Server: Uvicorn
Database: MySQL (via mysql-connector-python)
Testing: Postman & Swagger UI

Setup Instructions
1. Clone or Download the Project
Extract the kpa_backend folder (contains main.py) from the zip file.

2. Install Dependencies
Run the following commands:
pip install fastapi uvicorn mysql-connector-python

3. Setup MySQL Database
Open MySQL Workbench.
Run the following SQL commands:
CREATE DATABASE kpa_db;
USE kpa_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    phone VARCHAR(20) UNIQUE,
    password VARCHAR(50)
);

Update your MySQL credentials in main.py:
user="root",
password="pallavi@19",

4. Run the Server
uvicorn main:app --reload
You’ll see:
Uvicorn running on http://127.0.0.1:8000

5. Test the APIs
Using Swagger UI
Go to: http://127.0.0.1:8000/docs

Using Postman
Import the file: KPA Backend APIs.postman_collection.json.

Test:

POST /add-user
{
  "phone": "7760873976",
  "password": "to_share@123"
}
GET /users
Returns all users.

Implemented APIs
POST /add-user

Adds a new user to the database.

Input: JSON (phone, password).

Response: { "message": "User added successfully" }.

GET /users

Fetches all users.

Response: { "users": [[1, "phone"], [2, "phone"]] }.
