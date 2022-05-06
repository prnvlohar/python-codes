import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',database='login',user='prnvlohar',password='Pranav@19')
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
    while True:
        print("1.log in")
        print("2.register")
        print("3.exit")
        n=int(input("enter choice:"))
        if n==1:
            c1=connection.cursor()
            c1.execute("select * from users")
            r=cursor.fetchall()
            username=input("enter username")
            password=input("enter password")
            for row in r:
                if username==row[1]:
                    if password==row[2]:
                        print("||||||||||||||||||---succesfully log in---||||||||||||||||||||||")
                        break
            else:
                print("wrong username or password")
        elif n==2:
            name=input("enter name")
            username=input("enter username")
            password=input("enter password")
            q1="insert into users(name, username, password)values(%s,%s,%s)"
            q2=(name,username,password)
            c2=connection.cursor()
            c2.execute(q1,q2)
            connection.commit()
        elif n==3:
            break
        else:
            print("invalid choice")
        
                    
except Error as e:
    print("error",e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("connection closed")
