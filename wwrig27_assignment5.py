#1, 'Kristen', 'Klein', '2002-11-03', 'North Cynthiafurt', 'AZ', '50788'

import sqlalchemy as db 
import csv 
from datetime import datetime
from dateutil.relativedelta import relativedelta


student_name = "William Wright"

def main():
    engine = db.create_engine('sqlite:///../input/cutomer-sqlite/customer.sqlite')
    connection = engine.connect()
    results = connection.execute(db.text("select * from customer"))

    file = open("wwrig27_assignment5.csv", "w")
    customer_writer = csv.writer(file)
    customer_writer.writerow(['Customer ID', 'Name', 'Age'])
    
    for row in results:
        #print(full_name(row[1],row[2]), age(row[3]))
        customer_writer.writerow([customer_id(row[0]), full_name(row[1],row[2]), age(row[3])])

    file.close()
    
def full_name(first_name, last_name):
    return first_name + ' ' + last_name
    
def age(d):
    dob = datetime.strptime(d, '%Y-%m-%d')
    today = datetime.today()
    age = relativedelta(today, dob)
    return age.years

def customer_id(id):
    return id 

main()