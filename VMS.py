##These are the required modules to ensure smooth functioning of the program
import datetime
import sys
import time
import mysql.connector


##This function prints the output slowly
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./10)

        
## This function is used to return to the main menu at
## any given point in the entire program and is used at multiple places
def menuret():
    choice1 = input("Do you want to return to main menu?(y/n):")
    if choice1 =="y" or choice1 =="Y":
        menu()
    if choice1 =="n" or choice1=="N":
        slowprint("Exiting program...")
        SystemExit(0)


## This function is used to update records into the table in the sql database yolo
## The function is called within itself to create a loop which can be exited by giving input
## n when ur3 is asked as input
def updaterec(sqlu, sqlp, curtab):
    daba= mysql.connector.connect(host="localhost", user = sqlu , passwd= sqlp , database = "yolo")
    dabacursor=daba.cursor()
    print("Enter new record")
    ur1= input("Roll number:")
    ur2= input("Name:")
    ur3= input("Vaccination 1 status:(y/n)")
    if ur3 == 'y' or ur3 =='Y':
        ur41 =str(input("Vaccination 1 date(YYYY-MM-DD):"))
        ur4= "'%s'" % (ur41)
    if ur3 == 'n' or ur3 == 'N':
        ur4 = "NULL"
    ur5= str(input("Vaccination 2 status(y/n):"))
    if ur5 == 'y' or ur5 =='Y':
        ur61 = str(input("Vaccination 2 date(YYYY-MM-DD):"))
        ur6= "'%s'" % (ur61)
        
    if ur5 == 'n' or ur5 == 'N':
        ur6 = "NULL"
        
    finalistr =("INSERT INTO %s VALUES (%s, '%s', '%s', %s, '%s', %s)" %(str(curtab), int(ur1), ur2, ur3, ur4, ur5, ur6))
    
    dabacursor.execute(finalistr)
    daba.commit()
    c1 = input("Do you want to add another record(y/n):")
    if c1 == 'y' or c1 == 'Y':
        updaterec(sqlu, sqlp, curtab)
    else:
        menuret()  
        
    
##This function is written so that the user has an option to
## view all the records in the table created in database yolo   
def viewrec(sqlu, sqlp, curtab):
    print("The records are:")
    daba= mysql.connector.connect(host="localhost", user = sqlu , passwd= sqlp , database = "yolo")
    dabacursor=daba.cursor()
    stringexec= "select * from %s" %(str(curtab))
    dabacursor.execute(stringexec)
    precords = dabacursor.fetchall()
    for x in precords:
        print(x)
    menuret()


##This function prints a daily report, with the details of all vaccinations on the current day.
##It first fetches date from the datetime module, imported in the beginning
##Then it compares this date with dates within the table made by the user in databasse yolo
def dailyrep():
    deets = datetime.datetime.now()
    tday = deets.day
    tmonth = deets.month
    tyear = deets.year
    tdatef = '%s-%s-%s' % (tyear,tmonth, tday)
    print("Today's date is %s" %tdatef)
    daba= mysql.connector.connect(host="localhost", user = sqlu , passwd= sqlp , database = "yolo")
    dabacursor=daba.cursor()
    strexe1 = ("select rollno, name from %s where Vaccine1_date='%s'" % (curtab, tdatef))
    
    print("Your report for today is:")
    print("First Vaccination is due for today for the following:")
    dabacursor.execute(strexe1)
    precords1=dabacursor.fetchall()
    for x in precords1:
        print(x)
    strexe2 = ("select rollno, name from %s where Vaccine2_date='%s'" % (curtab, tdatef))
    
    print("Second Vaccination is due for today for the following:")
    dabacursor.execute(strexe2)
    precords2=dabacursor.fetchall()
    for y in precords2:
        print(y)
    menuret()
    

##This function is used to delete records
## that are unwanted but are present in the user created table
def delrec(sqlu, sqlp, curtab):
    daba= mysql.connector.connect(host="localhost", user = sqlu , passwd= sqlp , database = "yolo")
    dabacursor=daba.cursor()
    print("Enter Roll no of record you want to delete:")
    delrn= input("Rollno:")
    strexe3="DELETE FROM %s WHERE Rollno = %s" %(curtab,delrn)
    print(strexe3)
    dabacursor.execute(strexe3)
    daba.commit()
    print("Record deleted....")
    c3 = input("Do you want to delete another record(y/n):")
    if c3 == 'y' or c3 =='Y':
        delrec(sqlu, sqlp, curtab)
    else:
        menuret()

        
##This function acts as the choice indicator, which is
##constantly called within the function menu() defined below
def opt():
    selection1 = input("ENTER YOUR OPTION:")
    if selection1 == "1":
        updaterec(sqlu, sqlp, curtab)
    if selection1 == "2":
        viewrec(sqlu, sqlp, curtab)
    if selection1 == "3":
        dailyrep()
    if selection1 == "4":
        delrec(sqlu, sqlp, curtab)
    
##this function is the soul of the program and is the main menu
## of the program
def menu():
    print("WELCOME TO VACCINE MANAGEMENT SYSTEM")
    print("CHOOSE THE CORRESPONDING NUMBER TO THE TASK YOU WANT TO ACCOMPLISH")
    print("1: UPDATE RECORDS")  
    print("2: VIEW RECORDS")
    print("3: GET DAILY REPORT")
    print("4: DELETE RECORDS")
    opt()

##These initial data entries from the user gives
##the program the necessary data to work 
curtab= input("Which table do you want to work on:")
sqlu = input("Insert your mysql username:")
sqlp = input("Insert your mysql password:")
def mainalog():
    menu()
    
mainalog()    
