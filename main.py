from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",             # <-- Replace with your MySQL username
    password="pallavi@19",  # <-- Replace with your MySQL password
    database="kpa_db"
)
cursor = conn.cursor()

# Model for POST request
class User(BaseModel):
    phone: str
    password: str

# POST API - Add user
@app.post("/add-user")
def add_user(user: User):
    try:
        cursor.execute(
            "INSERT INTO users (phone, password) VALUES (%s, %s)",
            (user.phone, user.password)
        )
        conn.commit()
        return {"message": "User added successfully"}
    except Exception as e:
        return {"error": str(e)}

# GET API - Fetch users
@app.get("/users")
def get_users():
    cursor.execute("SELECT id, phone FROM users")
    rows = cursor.fetchall()
    return {"users": rows}
