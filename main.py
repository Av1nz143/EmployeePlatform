from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()
db = []

class Employee(BaseModel):
   id: int
   name: str
   department: str
   designation: str
   salary: int

@app.post("/employee")
def create(employee: Employee):
   db.append(employee.dict())
   return db

@app.get("/employeelist")
def get_all_employees_data():
   return db

@app.get("/employee/{id}")
def get_employee_data(id: int):
   return db[id]

@app.put("/employee/{id}")
def create(id: int, employee: Employee):
   db[id-1] = employee
   return db

@app.delete("/employee/{id}")
def delete_employee(id: int):
   db.pop(id-1)
   return db