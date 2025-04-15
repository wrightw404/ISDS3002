import sqlalchemy as db 
import csv 

student_name = "William Wright"

def main():
    engine = db.create_engine('sqlite:///../input/cutomer-sqlite/customer.sqlite')
    connection = engine.connect()
    results = connection.execute(db.text("select * from customer"))

main()