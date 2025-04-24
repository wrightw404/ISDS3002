import sqlalchemy as db
import csv
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta
import sqlite3


#1, 'Kristen', 'Klein', '2002-11-03', 'North Cynthiafurt', 'AZ', '50788'

class Customer():

    student_name = 'William Wright'
    
    def __init__(self, cust_id, first_name, last_name, date, city, state, zip_code): 
        self.id = cust_id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = date
        self.city = city 
        self.state = state
        self.zip = zip_code
        
    def full_name(self):
        return self.first_name + " " + self.last_name
        return("First Last")
        
    
    def age(self):
        dob = datetime.strptime(self.dob, "%Y-%m-%d").date()
        today = datetime.today()
        age = today.year - dob.year
        return age 
        
    def adult(self):
        return self.age() >= 18
    
    def to_json(self):
       return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "dob": self.dob,
            "city": self.city,
            "state": self.state,
            "zip": self.zip,
            "age": self.age(),
            "full_name": self.full_name(),
            "adult": "true" if self.adult() else "false"
        }

engine = db.create_engine("sqlite:///../input/cutomer-sqlite/customer.sqlite")
connection = engine.connect()

results = connection.execute(db.text("SELECT * FROM customer"))
rows = results.fetchall()

for row in rows:
    customer = Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
    print(customer.to_json())
        
connection.close()
