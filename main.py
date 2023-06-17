import mysql.connector as ps

def insert_rec(mycon,cur):
    idd=int(input("Enter customer id: "))
    name=input("Name of the customer: ")
    mem=int(input("No. of family members: "))
    phone=int(input("Enter phone no.: "))
    check_in=input("Enter date of check-in (YYYY-MM-DD): ")
    room=int(input("Enter room no.: "))
    check_out=input("Enter date of check-out (YYYY-MM-DD): ")
    cur.execute("insert into hotel values({},'{}',{},'{}','{}',{},'{}')".format(idd,name,mem,phone,check_in,room,check_out))
    mycon.commit()
    print()
    print("Invoice details:")
    print("---------------------------------------")
    room_cost=int(input("Enter accomodation costs: "))
    b=int(input("Enter total breakfast bill: "))
    l=int(input("Enter total lunch bill: "))
    s=int(input("Enter total snacks bill: "))
    d=int(input("Enter total dinner bill: "))
    laun=int(input("Enter laundry bill: "))
    rs=int(input("Enter room services bill: "))
    add=int(input("Enter additional services bill: "))
    total=room_cost+b+l+s+d+laun+rs+add
    cur.execute("insert into invoice values({},{},{},{},{},{},{},{},{},{})".format(idd,room_cost,b,l,s,d,laun,rs,add,total))
    mycon.commit()
    print("Values inserted")

def show_all(mycon,cur):
    cur.execute("select * from hotel")
    data=cur.fetchall()
    print("Customer id","name","members","phone","check-in","room","check-out",sep="\t")
    for rec in data:
        for d in rec:
            print(d,end="\t")
        print()
        
def modify_rec(mycon,cur):
    r=int(input("Enter customer id: "))
    print()
    print("----------OPTIONS----------")
    print("1. Change registration name")
    print("2. Change number of family members")
    print("3. Change phone number")
    print("4. Change room number")
    print()
    ch="y"
    while ch=="y":
        opt=int(input("Enter choice: "))
        if opt==1:
            name_n=input("Enter new name: ")
            st1="update hotel set name='{}' where id={}".format(name_n,r)
            cur.execute(st1)
            mycon.commit()
        elif opt==2:
            no_n=input("Enter no of family members: ")
            st2="update hotel set members={} where id={}".format(no_n,r)
            cur.execute(st2)
            mycon.commit()
        elif opt==3:
            phone_n=input("Enter new phone number: ")
            st3="update hotel set phone='{}' where id={}".format(phone_n,r)
            cur.execute(st3)
            mycon.commit()
        elif opt==4:
            room_n=int(input("Enter new room no: "))
            st4="update hotel set room={} where id={}".format(room_n,r)
            cur.execute(st4)
            mycon.commit()
        else:
            print("Enter valid option: ")
        ch=input("More changes? (y/n): ")
    print("Record updated")
    
def delete_rec(mycon,cur):
    r=int(input("Enter the customer id to be deleted: "))
    st="delete from hotel where id={}".format(r)
    st1="delete from invoice where id={}".format(r)
    cur.execute(st)
    cur.execute(st1)
    mycon.commit()
    print("Record deleted")
    
def show_one(mycon,cur):
    r=int(input("Enter customer id: "))
    st="select * from hotel where id={}".format(r)
    cur.execute(st)
    data=cur.fetchall()
    print("Customer id","name","members","phone","check-in","room","check-out",sep="\t")
    for rec in data:
        for d in rec:
            print(d,end="\t")
        print()
    print("---------------INVOICE---------------")
    st1="select * from invoice where id={}".format(r)
    cur.execute(st1)
    data=cur.fetchall()
    l=["room_cost","breakfast","lunch","snacks","dinner","laundry","room_service","additional_service","total"]
    i=0
    while i<len(l):
        for rec in data:
            print(l[i],":",rec[i+1],sep="\t")
        i+=1

print("--------------------------------------WELCOME TO HOTEL PICALLY--------------------------------------")
print()
print()
print("THIS APPLICATION WILL HELP YOU TO PRODUCE CUSTOMER DETAILS AND THE INVOICE AT THE TIME OF CHECKOUT")
print()
mycon=ps.connect(host="localhost",user="root",passwd="<your-system-password>")  
cur=mycon.cursor()
cur.execute("create database hotel_dbms") 
print("Database created")
cur.execute("use hotel_dbms")
cur.execute("create table hotel(id int primary key, name varchar(20),members int, phone varchar(10) unique, checkin date, room int, checkout date)")
cur.execute("create table invoice(id int primary key, room_cost int, breakfast int, lunch int, snacks int, dinner int, laundry int, room_service int, additional_services int,total_cost int)")
print("Tables created")
print("Choose the desired option")
print()
print("1. Insert record")
print("2. Show all records")
print("3. Modify record")
print("4. Delete record")
print("5. Show specific record")
print()
ch="y"
while ch=="y":
    opt=int(input("Choose an option: "))
    print()
    if opt==1:
        insert_rec(mycon,cur)
    elif opt==2:
        show_all(mycon,cur)
    elif opt==3:
        modify_rec(mycon,cur)
    elif opt==4:
        delete_rec(mycon,cur)
    elif opt==5:
        show_one(mycon,cur)
    else:
        print("Enter valid option")
    ch=input("Choose again? (y/n)")
mycon.close()
print()
print("--------------THANK YOU FOR VISITING--------------")
print("----------HOPE TO SEE YOU NEXT TIME TOO!----------")
