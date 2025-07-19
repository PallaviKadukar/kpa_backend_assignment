KPA Backend Assignment
📌 Overview
This project implements two REST APIs using FastAPI (Python) and MySQL as part of the KPA Form Data assignment.
The APIs are designed to:

Add a user (via POST /add-user).

Fetch all users (via GET /users).

Both APIs adhere to the required request/response structure and can be tested via Swagger UI or Postman.

🚀 Tech Stack
Language: Python 3.13

Framework: FastAPI

ASGI Server: Uvicorn

Database: MySQL (via mysql-connector-python)

Testing Tools: Swagger UI & Postman

⚙️ Setup Instructions
1. Clone or Download the Repository

git clone https://github.com/<your-username>/kpa_backend_assignment.git
cd kpa_backend_assignment
(Or download the ZIP and extract.)

2. Install Dependencies
Ensure Python and pip are installed.
Run:


pip install fastapi uvicorn mysql-connector-python
3. Configure MySQL Database
Run these SQL commands in MySQL Workbench:


CREATE DATABASE 

kpa_db;

USE kpa_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    
phone VARCHAR(20) UNIQUE,
   
password VARCHAR(50)

);

Update main.py with your MySQL credentials:


user="root",

password="pallavi@19",


4. Run the FastAPI Server

uvicorn main:app --reload

If successful, you’ll see:


Uvicorn running on http://127.0.0.1:8000

🧪 Testing the APIs

Swagger UI

Visit:

http://127.0.0.1:8000/docs

Use the Try it out feature to test /add-user and /users.

Postman

Import the collection:

KPA Backend APIs.postman_collection.json

Test:

POST /add-user

Request body:


{
  "phone": "7760873976",
  "password": "to_share@123"
}
GET /users
Fetches all users in the database.

📂 Project Structure

kpa_backend_assignment/
│
├── main.py                         # FastAPI code

├── README.md                       # Project documentation

└── KPA Backend APIs.postman_collection.json  # Postman collection

🌟 Implemented APIs

1. POST /add-user
   
Description: Add a new user to the database.

Request Body:


{ "phone": "1234567890", "password": "mypassword" }
Response:


{ "message": "User added successfully" }

2. GET /users
   
Description: Fetch all users from the database.

Response:


{ "users": [[1, "1234567890"]] }
