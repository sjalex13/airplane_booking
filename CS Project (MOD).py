import mysql.connector as mys,sys,datetime

mycon = mys.connect(host="localhost",user="",passwd="")
mycursor = mycon.cursor()
q = "create database if not exists Airline_Booking"
mycursor.execute(q)
q = "use Airline_Booking"
mycursor.execute(q)

def create_flight():
   q = '''CREATE TABLE flight(
Flight_no INT PRIMARY KEY,
ORIGIN VARCHAR(20),
DESTINATION VARCHAR(20),
DEPARTURE DATETIME,
ARRIVAL DATETIME);'''
   mycursor.execute(q)
   mycon.commit()

create_flight()

def create_customer():
   q = '''CREATE TABLE customer(
cust_id INT PRIMARY KEY,
cust_name VARCHAR(30));'''
   mycursor.execute(q)
   mycon.commit()

create_customer()

def create_booking():
   q = '''CREATE TABLE booking(
flight_no INT, 
date DATETIME,
cust_id INT);'''
   mycursor.execute(q)
   mycon.commit()

create_booking()

def insert_into_flight():
    ch = 'y'
    while ch in "Yy":
        flight_no = int(input("Enter FLIGHT NO :"))
        from_ = input("Enter FROM :")
        to_ = input("Enter TO :")
        departure = input("Enter DEPARTURE :")
        arrival = input("Enter ARRIVAL :")
        q = "INSERT INTO flight VALUES({},'{}','{}','{}','{}')".format(flight_no,from_,to_,departure,arrival)
        mycursor.execute(q)
        print(mycursor.rowcount,"record inserted")
        ch = input("\nAdd more flights(y/n) :")
    mycon.commit()

def insert_into_customer():
    ch = 'y'
    while ch in "Yy":
        cust_no = int(input("Enter CUST ID :"))
        name = input("Enter NAME :")
        q = "INSERT INTO customer VALUES({},'{}')".format(cust_no,name)
        mycursor.execute(q)
        print(mycursor.rowcount,"record inserted")
        ch = input("\nAdd more customers(y/n) :")
    mycon.commit()

def delete_from_flight():
    ch = "y"
    while ch in "Yy":
        flight_no = int(input("Enter FLIGHT NO :"))
        q = "delete from flight where Flight_no = {}".format(flight_no)
        mycursor.execute(q)
        if mycursor.rowcount == 0:
            print("\nNo flight found")
        else:
            mycon.commit()
            print("\nDeleted")
            print(mycursor.rowcount,"Record deleted")
        ch = input("\nDelete more flights(y/n) :")

def delete_from_customer():
    ch = "y"
    while ch in "Yy":
        cust_no = int(input("Enter CUST NO :"))
        q = "delete from customer where cust_id = {}".format(cust_no)
        mycursor.execute(q)
        if mycursor.rowcount == 0:
            print("No customer found")
        else:
            mycon.commit()
            print("\nDeleted")
            print(mycursor.rowcount,"Record deleted")
        ch = input("\nDelete more customers(y/n):")

def update_flight():
    ch = "y"
    while ch in "Yy":
        flight_no = int(input("Enter FLIGHT NO to be updated :"))
        q = "select * from flight where Flight_no = {}".format(flight_no)
        mycursor.execute(q)
        data = mycursor.fetchone()
        if data == None:
            print("\nFlight not found")
        else:
            from_ = input("Enter FROM :")
            to_ = input("Enter TO :")
            departure = input("Enter DEPARTURE :")
            arrival = input("Enter ARRIVAL :")
            q = "UPDATE flight SET ORIGIN = '{}',DESTINATION = '{}',DEPARTURE = '{}',ARRIVAL = '{}' where Flight_no = {}".format(from_,to_,departure,arrival,flight_no)
            mycursor.execute(q)
            mycon.commit()
            print(mycursor.rowcount,"Record updated")
        ch=input("\nDo you wish to continue(y/n):")

def update_customer():
    ch = "y"
    while ch in "Yy":
        cust_no = int(input("Enter CUST ID to be updated :"))
        q = "select * from customer where cust_id = {}".format(cust_no)
        mycursor.execute(q)
        data = mycursor.fetchone()
        if data == None:
            print("Customer not found")
        else:
            name = input("Enter NAME :")
            q = "UPDATE customer SET cust_name = '{}' where cust_id = {}".format(name,cust_no)
            mycursor.execute(q)
            mycon.commit()
            print(mycursor .rowcount,"Record updated")
        ch = input("\nDo you wish to continue(y/n):")

def search_flights():
    ch = 'y'
    while ch in 'Yy':
        from_ = input("Enter ORIGIN :")
        to_ = input("Enter DESTINATION :")
        q = "select * from flight where ORIGIN = '{}'and DESTINATION = '{}'".format(from_,to_)
        mycursor.execute(q)
        data = mycursor.fetchall()
        if data == []:
            print("\nNo flights found")
        else:
            print("FLIGHT NO\tORIGIN\tDESTINATION\tDEPARTURE\tARRIVAL")
            for i in data:
                print(i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4])
        ch = input("\nDo you wish to search more(y/n) :")

def view_all_flights():
    q = "select * from flight"
    mycursor.execute(q)
    data = mycursor.fetchall()
    if data == []:
        print("\nNo flights found")
    else:
        print("FLIGHT NO\tORIGIN\tDESTINATION\tDEPARTURE\tARRIVAL")
        for i in data:
            print(i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4])

def view_all_customers():
    q = "select * from customer"
    mycursor.execute(q)
    data = mycursor.fetchall()
    if data == []:
        print("\nNo customer found")
    else:
        print("CUST ID\tCUST NAME")
        for i in data:
            print(i[0],"\t",i[1])

def view_all_bookings():
    q = "select * from booking"
    mycursor.execute(q)
    data = mycursor.fetchall()
    if data == []:
        print("\nNo bookings found")
    else:
        print("FLIGHT NO\tDATE OF BOOKING\tCUST ID")
        for i in data:
            print(i[0],"\t",i[1],"\t",i[2])

def booking_flight():
    ch='y'
    while ch in 'Yy':
        fl_no = int(input("Enter the Flight number to book :"))
        date = str(datetime.datetime.today()).split()[0]
        cust_id = int(input("Enter CUST ID :"))
        q = "INSERT INTO booking VALUES({},'{}',{})".format(fl_no,date,cust_id)
        s = mycursor.execute(q)
        print("\nFlight Booked ")
        ch = input("\nDo you wish to book more(y/n) :")
    mycon.commit()

def cancel_booking():
    ch='y'
    while ch in 'Yy':
        fl_no = int(input("Enter the Flight number to book :"))
        cust_id = int(input("Enter CUST ID :"))
        q = "DELETE FROM booking WHERE flight_no = {} and cust_id = {}".format(fl_no,cust_id)
        mycursor.execute(q)
        
        if mycursor.rowcount == 0:
            print("\nNo bookings found")
        else:
            mycon.commit()
            print("\nBooking cancelled")
        ch = input("\nDo you wish to cancel more(y/n) :")
    mycon.commit()
    
             
def main():
    while True:
        print("\nEnter role")
        print("1.Admin")
        print("2.Customer")
        print("3.Exit")
        ch1 = int(input("\nEnter your choice: "))
        if ch1 == 2:
            ch3 = "y"
            while ch3 in "Yy":
                print("\n1.Search Flights")
                print("2.Book Flight")
                print("3.Cancel booking")
                ch2 = int(input("\nEnter your choice:  "))
                if ch2 == 2:
                    booking_flight()
                elif ch2 == 1:
                    search_flights()
                elif ch2 == 3:
                    cancel_booking()
                else:
                    print("\nInvalid choice")
                ch3 = input("\nContinue with customer tasks(y/n) :")
        elif ch1 == 1:
            ch2 = "y"
            while ch2 in "Yy":
                print("1.Add A Flight")
                print("2.Add A Customer")
                print("3.Delete Flight")
                print("4.Delete Customer")
                print("5.Modify Flight")
                print("6.Modify Customer")
                print("7.View all flights")
                print("8.View all customers")
                print("9.View all bookings")
                ch3 = int(input("\nEnter your choice: "))
                if ch3 == 1:
                    insert_into_flight()
                elif ch3 == 2:
                    insert_into_customer()
                elif ch3 == 3:
                    delete_from_flight()
                elif ch3 == 4:
                    delete_from_customer()
                elif ch3 == 5:
                    update_flight()
                elif ch3 == 6:
                    update_customer()
                elif ch3 == 7:
                    view_all_flights()
                elif ch3 == 8:
                    view_all_customers()
                elif ch3 == 9:
                    view_all_bookings()
                else:
                    print("\nInvalid choice")
                ch2 = input("\nContinue with admin tasks(y/n) :")
        elif ch1 == 3:
            sys.exit()
        else:
            print("\nInvalid choice")
main()                 

                      

