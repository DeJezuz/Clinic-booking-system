from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import mysql.connector

app = FastAPI()

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootpass",
    database="clinic_booking_system"
)
cursor = conn.cursor()

# Models
class Patient(BaseModel):
    full_name: str
    date_of_birth: str
    email: str
    phone: str

@app.post("/patients/")
def create_patient(patient: Patient):
    query = "INSERT INTO patients (full_name, date_of_birth, email, phone) VALUES (%s, %s, %s, %s)"
    values = (patient.full_name, patient.date_of_birth, patient.email, patient.phone)
    cursor.execute(query, values)
    conn.commit()
    return {"message": "Patient created successfully"}

@app.get("/patients/")
def get_patients():
    cursor.execute("SELECT * FROM patients")
    rows = cursor.fetchall()
    return {"patients": rows}
