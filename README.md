# 🏥 Clinic Booking System — Final Project

This repository contains the full solution for Week 8 Final Project:

## ✅ Question 1: MySQL Database Schema

- Located in `schema/clinic_booking_system.sql`
- Includes tables for:
  - Patients
  - Doctors
  - Appointments
  - Prescriptions
  - Specialties
- Constraints: PRIMARY KEY, FOREIGN KEY, UNIQUE, ENUM

## ✅ Question 2: FastAPI CRUD App

- Located in `app/main.py`
- Built with FastAPI
- Connects to MySQL database
- Implements:
  - Create patient
  - Read patients

## 🚀 How to Run

1. Install MySQL and create the database using the SQL file
2. Install FastAPI:
   ```bash
   pip install fastapi uvicorn mysql-connector-python
