
##These modules are imported to ensure smooth functioning of program
import mysql.connector


##This is used to create the initial connection to mysql,
##To create a database named yolo, to store the table
## on second runs of the program, or if the database already exists
##it will not create a new database
##also if false credentials for initial connection are submitted
##the program will prompt it again and again until the correct input is entered
def logininput():
    sqlu=input("Insert your sql username:")
    sqlp=input("Insert your sql pw:")
    
    try:
        daba= mysql.connector.connect(host="localhost", user = sqlu , passwd= sqlp)
        confirm = daba.is_connected()
        if confirm == True:
            print("Connection successful!")
        dacursor = daba.cursor()
        try:
            dabacursor.execute("CREATE DATABASE yolo")
        except:
            pass
             
        
    except:
        print("You have entered incorrect credentials, try again please")
        logininput()

##Here, we start our initial data entry.
##If the data is already existing, users can type 2 and continue to the second file
##If fresh table is being created, the table is named and created and then we continue to the second file

    print("DO YOU WANT TO CREATE A NEW TABLE OR ACCESS AN EXISTING ONE?")
    while True:
        try:
            print("Type '1' to create a new TABLE. Type '2' to access an existing one:")
            choicea = input("Enter your choice:")
            if choicea == "1":
                print("You have chosen to create a new TABLE.")
                print("Give your new TABLE a name:")
                tabname = input("Name:")
                daba= mysql.connector.connect(host="localhost", user = sqlu , passwd= sqlp , database = "yolo")
                dabacursor=daba.cursor()
                dabacursor.execute("CREATE TABLE %s(Rollno int(3) NOT NULL PRIMARY KEY,\
Name varchar(30) NOT NULL, \
Vaccine1_status char(1), Vaccine1_date date, \
Vaccine2_status char(1), Vaccine2_date date)" % (tabname))
            from VMS import functions
            daba= mysql.connector.connect(host="localhost", user = sqlu , passwd= sqlp , database = "yolo")
            dabacursor=daba.cursor()
            mainalog()
            break
        
                
                
                
            if choicea == "2":
                from VMS import functions
                mainalog()
        except ValueError:
            print("enter valid input:")
            continue

logininput()




       




