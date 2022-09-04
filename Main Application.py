import Super_Admins
import Admins
import Test_Agents
import Lab_Technicians
import re
import PySimpleGUI as sg
import password_check
import INDIA
import Contact_us
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector
import sqlalchemy
from sqlalchemy import create_engine

cnx=create_engine('mysql+mysqlconnector://root:ash@503.#@localhost:3306/Covid_Data_Analysis')

mydb=mysql.connector.connect(host="localhost",
                            user="root",
                            password="ash@503.#",
                            database="Covid_Data_Analysis")

mycursor = mydb.cursor()
mycursor.execute("commit")


i = 1
buttonsize = (10,4)

    
sg.theme('DarkTeal10')
layout = [[sg.Text(" ",size = (5, 1))],[sg.Text('COVID ANALYSIS', size = (40,1), font = ('Andale Mono', 20))],
        [sg.Submit("HOME")],
        [sg.Submit("USER MANUAL")],
        [sg.Submit("ABOUT US")],
        [sg.Submit("LOGIN")],
        [sg.Submit("EXIT")]]
window = sg.Window("Covid Analysis", layout, size=(325,300))
while(i):
    event, a = window.read()
    option = event
    print(option)
    if(option == "HOME"):
        sg.popup(" Welcome to the Covid Data Analysis Home page. Here at the Data Analysis page, we have"
                " developed a dynamic tool, invaluable for today's need. A really constructive source,"
                  " it will be of great convenience when it comes to administration of the high amount of "
                  " covid related data and its effective analysis. Being a growing tool, this vital product"
              " is currently limited to the region of India.")
    elif(option == "USER MANUAL"):
        sg.popup("This page basically serves as a crucial source of information for three categories of people,",
                 "",
                 "Administrators: The administrators of the web page are given several privileges over"
              "     the other two consumers in the list. He/she has unrestricted access to a large amount"
              "     of data. He/she is given the ability to analyse the number of results in a specific"
              "     state/district, gender or age, whether it be positive or negative. He/she will also be"
              "     provided a direct admin access to the employee data, i.e. test agents and lab technicians."
            
                 "",
                "Lab technicians: Lab technicians are inclined to the sole purpose of entering "
              "     the test result data of the patients.",
                 "",
                 "Test agent: Test agents are also dedicated to the work of entering the details of the"
              "     patients for future data analysis. They are also allowed to enter the result data,"
              "     provided that it was tested in a mobile unit."
                 )
    elif(option == "ABOUT US"):
            sg.popup("About us",
                     "Get In Touch With Us",
                     "",
                     "For Technical Support"
              " Contact: +91 799 8877666"
              " Email: helpdesk@dhr.in",
              "Office of Secretary DHR :"
              " Department of Health Research"
              " 2nd Floor,IRCS Building,"
              " 1,Red Cross Road, New Delhi - 110001",
                     "",
                     "Web Information Managers :",
              " Shri Aswin Sujith Varghese,Shri Adarsh A,Shri Vignesh,"
              " Under Secretary, Department of Health Research"
              " Email : depthealthresearch@dhr.in"
              " Office No. :+91 755 9988111"
            )

    elif(option == "LOGIN"):
        window.close()
        i = 0;
        layout = [[sg.Text("Please Enter the user type ")], 
                  [sg.Submit("ADMIN")],
                  [sg.Submit("SUPER ADMIN")],
                  [sg.Submit("TEST AGENT")],
                  [sg.Submit("LAB TECHNICIAN")],
                  [sg.Submit("BACK")]]
        window = sg.Window("Covid Analysis", layout, size = (200,200))
        event, values = window.read()
        option = event
        window.close()
        window.close()
        if (option == "ADMIN"):
            Admins.admins()
            

        elif (option == "SUPER ADMIN"):
            Super_Admins.super_admin()
            

        elif (option == "TEST AGENT"):
            Test_Agents.test_agents()
            
            
        elif ( option == "LAB TECHNICIAN"):
            Lab_Technicians.lab_techs()
            
            
        else:
            i = 1
            window.close()

        
    else:
        quit()
