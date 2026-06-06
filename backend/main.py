
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import mysql.connector
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_conn():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        user=os.environ.get("DB_USER", "root"),
        password=os.environ.get("DB_PASSWORD", "12345678"),
        database=os.environ.get("DB_NAME", "payroll_db")
    )

class FullTimeEmployee(BaseModel):
    name:str
    id:int
    monthlySalary:float

class PartTimeEmployee(BaseModel):
    name:str
    id:int
    hoursWorked:int
    hourlyRate:float

@app.get("/")
def root():
    return {"status": "API is running"}

@app.get("/employees")
def employees():
    conn=get_conn()
    cur=conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM employees")
    data=cur.fetchall()
    conn.close()
    return data

@app.post("/employees/fulltime")
def add_fulltime(emp:FullTimeEmployee):
    salary=emp.monthlySalary
    conn=get_conn()
    cur=conn.cursor()
    cur.execute(
        "INSERT INTO employees(id,name,type,salary) VALUES(%s,%s,%s,%s)",
        (emp.id,emp.name,"FULLTIME",salary)
    )
    conn.commit()
    conn.close()
    return {"message":"added"}

@app.post("/employees/parttime")
def add_parttime(emp:PartTimeEmployee):
    salary=emp.hoursWorked * emp.hourlyRate
    conn=get_conn()
    cur=conn.cursor()
    cur.execute(
        "INSERT INTO employees(id,name,type,salary) VALUES(%s,%s,%s,%s)",
        (emp.id,emp.name,"PARTTIME",salary)
    )
    conn.commit()
    conn.close()
    return {"message":"added"}

@app.delete("/employees/{emp_id}")
def delete(emp_id:int):
    conn=get_conn()
    cur=conn.cursor()
    cur.execute("DELETE FROM employees WHERE id=%s",(emp_id,))
    conn.commit()
    conn.close()
    return {"message":"deleted"}
