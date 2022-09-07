import Super_Admins
import Admins
import Test_Agents
import Lab_Technicians
import re
import password_check
import INDIA
import Contact_us
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector
import sqlalchemy
from sqlalchemy import create_engine
cnx=create_engine('mysql+mysqlconnector://root:ash@503.#@localhost:3306/Covid_Data_Analysis')

mydb=mysql.connector.connect(host="localhost",
                            user="root",
                            password="ash@503.#",
                            database="Covid_Data_Analysis")
mycursor=mydb.cursor()
mycursor.execute("commit")
print("\n")
print()
print("+--------------------------------------------------------------------------------------+")
print("|                               COVID-19 DATA ANALYSIS                                 |")
print("|                               ~~~~~~~~~~~~~~~~~~~~~~                                 |")
print("+--------------------------------------------------------------------------------------+")
print()
print("                             DEPARTMENT OF HEALTH RESEARCH                                   ")
print("                             =============================                                   ")
print("----------------------------------------------------------------------------------------","\n")
print(" Home")
print("________________________________________________________________________________________","\n")
print(" Welcome to the Covid Data Analysis Home page. Here at the Data Analysis page, we have",
      " developed a dynamic tool, invaluable for today's need. A really constructive source,",
      " it will be of great convenience when it comes to administration of the high amount of ",
      " covid related data and its effective analysis. Being a growing tool, this vital product",
      " is currently limited to the region of India.",sep="\n")
print()
# if you wish to sign up, pls contact the super admin team # default code for admin 1111

i=1
while(i>0):
    print("A. HOME","B. USER MANUAL","C. ABOUT US","D. LOGIN",sep="\n")
    y=input("ENTER OPTION LETTER: ")
    print()
    if(y=="a")or(y=="A"):
        print(" Home")
        print("________________________________________________________________________________________","\n")
        print(" Welcome to the Covid Data Analysis Home page. Here at the Data Analysis page, we have",
              " developed a dynamic tool, invaluable for today's need. A really constructive source,",
              " it will be of great convenience when it comes to administration of the high amount of ",
              " covid related data and its effective analysis. Being a growing tool, this vital product",
              " is currently limited to the region of India." ,sep="\n")
        print()

    elif(y=="b")or(y=="B"):
        print(" User Manual")
        print("________________________________________________________________________________________","\n")
        print(" This page basically serves as a crucial source of information for three categories of people,",
              " mainly: ",sep='\n')
        print()
        print(" >>> Administrators: The administrators of the web page are given several privileges over",
              "     the other two consumers in the list. He/she has unrestricted access to a large amount",
              "     of data. He/she is given the ability to analyse the number of results in a specific",
              "     state/district, gender or age, whether it be positive or negative. He/she will also be",
              "     provided a direct admin access to the employee data, i.e. test agents and lab technicians.",
              "     (DEFAULT CODE:- 1111 )",sep="\n")
        print()
        print(" >>> Lab technicians: Lab technicians are inclined to the sole purpose of entering ",
              "     the test result data of the patients.",sep="\n")
        print()
        print(" >>> Test agent: Test agents are also dedicated to the work of entering the details of the",
              "     patients for future data analysis. They are also allowed to enter the result data,",
              "     provided that it was tested in a mobile unit.",sep="\n")
        print()

    elif(y=="c")or(y=="C"):
        print(" About us")
        print("________________________________________________________________________________________","\n")
        print(" Get In Touch With Us")
        print(" ====================")
        print(" For Technical Support",
              " Contact: +91 799 8877666",
              " Email: helpdesk@dhr.in",sep="\n")
        print("____________________________________________________________","\n")
        print(" Office of Secretary DHR :",
              " Department of Health Research",
              " 2nd Floor,IRCS Building,",
              " 1,Red Cross Road, New Delhi - 110001",sep="\n")
        print("------------------------------------------------------------","\n")
        print(" Web Information Managers :",
              " Shri Aswin Sujith Varghese,Shri Adarsh A,Shri Vignesh,",
              " Under Secretary, Department of Health Research",
              " Email : depthealthresearch@dhr.in",
              " Office No. :+91 755 9988111",sep="\n")
        print()

    elif(y=="d")or(y=="D"):
        print("Login as:","a.Admin","(or)","b.Test Agent","(or)","c.Lab Technician",sep="\n")
        i=0
    else:
        print("INCORRECT OPTION LETTER !!! :(")
        print()

u=input("ENTER OPTION LETTER: ")
print()
if(u=="a")or(u=="A"):
    ln=input("ENTER CODE FOR LOGGING IN AS ADMIN: ")
    print()
    if(ln=='1111'):
        Admins.admins()

    elif(ln=='2004'):
        Super_Admins.super_admin()
                
elif(u=="b")or(u=="B"):
    Test_Agents.test_agents()

elif(u=="c")or(u=="C"):
    Lab_Technicians.lab_techs()

else:
    quit()
