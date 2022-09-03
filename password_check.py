import re
import mysql.connector
import sqlalchemy
from sqlalchemy import create_engine
cnx=create_engine('mysql+mysqlconnector://root:ash@503.#@localhost:3306/Covid_Data_Analysis')

mydb=mysql.connector.connect(host="localhost",
                            user="root",
                            password="ash@503.#",
                            database="Covid_Data_Analysis")
mycursor=mydb.cursor()
def Strong_password_checker():
    print("THE PASSWORD MUST HAVE ATLEAST 8 CHARACTERS.")
    print("THE PASSWORD MUST INCLUDE ALPHABETS AND DIGITS.")
    print("THE PASSWORD MUST HAVE SPECIAL CHARACTERS.")
    print()

    while True:
        print()
        str1=input("ENTER PASSWORD    : ")
        if(len(str1)>=8):
            lowerReg=re.compile(r'[a-z]')
            upperReg=re.compile(r'[A-Z]')
            numberReg=re.compile(r'\d')
            specialReg=re.compile(r'[\!\@\#\$\%\^\&\*\(\)\-\_\=\+\[\]\{\}\;\:\'\"\,\<\.\>\/\?\\\|\`\~]')
            if(lowerReg.search(str1))or(upperReg.search(str1)):
                if(numberReg.search(str1)):
                    if(specialReg.search(str1)):
                        check_str1=input("RE-ENTER PASSWORD : ")
                        if(str1==check_str1):
                            print()
                            print("PASSWORD ACCEPTED")
                            break
                        else:
                            print()
                            print("PASSWORD DOESN'T MATCH...","TRY AGAIN!!! :(",sep="\n")
                    
                    else:
                        print("THE PASSWORD MUST HAVE SPECIAL CHARACTERS.")
                        print()
                else:
                    print("THE PASSWORD MUST HAVE ATLEAST A DIGIT IN IT.")
                    print()
            else:
                print("THE PASSWORD MUST INCLUDE LETTERS.")
                print()
        else:
            print("THE PASSWORD MUST HAVE ATLEAST 8 CHARACTERS.")
            print()

    Strong_password_checker.clear_check=check_str1
    
def Username_checker():
    print("THE USERNAME MUST HAVE ATLEAST 6 CHARACTERS.")
    print("THE USERNAME MUST INCLUDE ALPHABETS AND DIGITS.")
    print()
    k=1
    while(k>0):
        print()
        str6=input("ENTER USERNAME    : ")
        if(len(str6)>=6):
            lowerReg=re.compile(r'[a-z]')
            upperReg=re.compile(r'[A-Z]')
            numberReg=re.compile(r'\d')
            if(lowerReg.search(str6))or(upperReg.search(str6)):
                if(numberReg.search(str6)):
                    check_str6=input("RE-ENTER USERNAME : ")
                    if(str6==check_str6):
                        print()
                        print("USERNAME ACCEPTED")
                        break
                    else:
                        print()
                        print("USERNAME DOESN'T MATCH...","TRY AGAIN!!! :(",sep="\n")
                else:
                    print("THE USERNAME MUST HAVE ATLEAST A DIGIT IN IT.")
                    print()
            else:
                print("THE USERNAME MUST INCLUDE LETTERS.")
                print()
        else:
            print("THE USERNAME MUST HAVE ATLEAST 6 CHARACTERS.")
            print()

    Username_checker.clear_uname_check=check_str6

    
