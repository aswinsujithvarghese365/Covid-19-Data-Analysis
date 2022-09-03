import re
import getpass
import password_check
import INDIA
import Contact_us
import pandas as pd
import mysql.connector
import sqlalchemy
from sqlalchemy import create_engine
cnx=create_engine('mysql+mysqlconnector://root:ash@503.#@localhost:3306/Covid_Data_Analysis')

mydb=mysql.connector.connect(host="localhost",
                            user="root",
                            password="ash@503.#",
                            database="Covid_Data_Analysis")


def test_agents():
    mycursor=mydb.cursor()
    mycursor.execute("commit")
    i=1
    while(i>0):
        uname=input("ENTER USERNAME: ")
        passwd=getpass.getpass(prompt="ENTER PASSWORD: ")
        mycursor.execute("select count('Agent_Name') from test_agents where Username='"+uname+"' and Password='"+passwd+"'")
        for b in mycursor:
            if(b==(1,)):
                print()
                x="ACCESS GRANTED"
                print(x)
                print()
                i=0
                
            else:
                print()
                print("ACCESS DENIED")
                x="INVALID USERNAME OR PASSWORD"
                print(x)
                print()
                        

    if(x=="ACCESS GRANTED"):
        while True:
            print("____________________________________________________________","\n")
            print("What would you like to do?")
            print("1.Add/Edit details or Results of Patients","2.View report of the patient","3.Edit Profile","4.Show Profile","5.Contact Us",
                  "6.Quit Application",sep="\n")
            print()
            th=input("ENTER OPTION NUMBER: ")
            print("____________________________________________________________","\n")

            if(th=='1'):
                print("What data would you like to enter?")
                print("1.Enter details of the patient","2.Edit details of a patient","3.Add test-type and result of the patient","4.Back",sep="\n")
                print()
                ed=input("ENTER OPTION NUMBER: ")
                print()
                if(ed=='1'):
                    p_name=input("ENTER PATIENT'S NAME: ")
                    p_name=p_name.upper()
                    p_email=input("ENTER PATIENT'S EMAIL ID: ")
                    p_email=p_email.lower()
                    print()
                    INDIA.States_and_Districts_option()
                    p_state=INDIA.States_and_Districts_option.selected_state1
                    p_district=INDIA.States_and_Districts_option.selected_district1
                    print("YOUR PATIENT'S STATE IS ",p_state)
                    print("YOUR PATIENT'S DISTRICT IS ",p_district)
                    print()
                    p_address=input("ENTER PATIENT'S ADDRESS: ")
                    print()
                    p_mobile=""
                    while(len(p_mobile)>14)or(len(p_mobile)<14):
                        p_mobile=input("ENTER PATIENT'S MOBILE NUMBER(format:-0091xxxxxxxxxx): ")
                        if(len(p_mobile)>14)or(len(p_mobile)<14):
                            print("INCORRECT FORMAT OF MOBILE NUMBER !!! :(","TRY AGAIN!!!",sep="\n")
                            print()
                    print()
                    print("SELECT AGE GROUP OF THE PATIENT: ")
                    print("1. 0-1","2. 2-11","3. 12-17","4. 18 and above","5. 65 and above",sep='\n')
                    print()
                    sa=""
                    while sa not in ['1','2','3','4','5']:
                        sa=input("ENTER OPTION NUMBER: ")
                        if(sa=='1'):
                            p_age="0-1"
                        elif(sa=='2'):
                            p_age="2-11"
                        elif(sa=='3'):
                            p_age="12-17"
                        elif(sa=='4'):
                            p_age="18 and above"
                        elif(sa=='5'):
                            p_age="65 and above"
                        else:
                            print("INCORRECT OPTION NUMBER !!! :(")
                            print()

                    print()
                    print("YOUR PATIENT'S AGE GROUP IS ",p_age)
                    print()
                    print("SELECT PATIENT'S GENDER: ")
                    print("1.Male","2.Female",sep='\n')
                    print()
                    sg=""
                    while sg not in ['1','2']:
                        sg=input("ENTER OPTION NUMBER: ")
                        if(sg=='1'):
                            p_gender="Male"
                        elif(sg=='2'):
                            p_gender="Female"
                        else:
                            print("INCORRECT OPTION NUMBER !!! :(")
                            print()

                    print()    
                    print("YOUR PATIENT'S GENDER IS ",p_gender)
                    
                    ok="select* from test_agents where Username='"+uname+"'"
                    df_show_tprofile=pd.read_sql(ok,mydb)
                    de=df_show_tprofile["TA_Emp_No"]
                    p_TA_emp_no=str(de[0])

                    om="select* from test_agents where Username='"+uname+"'"
                    df4=pd.read_sql(om,mydb)
                    dk=df4["Unit_Name"]
                    unit_name=str(dk[0])

                    tc="select max(Record_ID) from patients"
                    max_r_id=pd.read_sql(tc,mydb)
                    tg=max_r_id["max(Record_ID)"]
                    r_id=str(tg[0]+1)
                    print()
                    print("YOUR PATIENT'S MEDICAL RECORD SERIAL NUMBER IS ",r_id)

                    mycursor.execute("insert into patients(Record_ID,Name,Email_ID,State,District,Address,Mobile_No,Age_Group,Gender,Date,Month,TA_Emp_No,Unit_Name) values('"+r_id+"','"+p_name+"','"+p_email+"','"+p_state+"','"+p_district+"','"+p_address+"','"+p_mobile+"','"+p_age+"','"+p_gender+"',date(curdate()),monthname(curdate()),'"+p_TA_emp_no+"','"+unit_name+"')")
                    mycursor.execute("commit")
                    print()
                    DJ={"Record ID":r_id,"Patient Name":p_name,"Email ID":p_email,"State":p_state,
                        "District":p_district,"Address":p_address,"Mobile No.":p_mobile,"Age Group":p_age,
                        "Gender":p_gender,"Employee no. of Test Agent":p_TA_emp_no}
                    enter_patients_details=pd.DataFrame(DJ,index=[0])
                    print(enter_patients_details)
                    print()
                    print("PATIENT'S DETAILS HAS BEEN ENTERED")

                elif(ed=='2'):
                    p_record_id=str(input("ENTER MEDICAL RECORD SERIAL NUMBER OF THE PATIENT: "))
                    #p_record_id=str(p_record_id[:-1])
                    om="select* from test_agents where Username='"+uname+"'"
                    df4=pd.read_sql(om,mydb)
                    dk=df4["Unit_Name"]
                    unit_name=str(dk[0])
                    mycursor.execute("select count('Name') from patients where Record_ID='"+p_record_id+"' and Unit_Name='"+unit_name+"'")
                    print()
                    for ab in mycursor:
                        if(ab==(1,)):
                            op="select Record_ID,Name,Email_ID,State,District,Address,Mobile_No,Age_Group,Gender,Date,Test_Type,Result from patients where Record_ID='"+p_record_id+"' and Unit_Name='"+unit_name+"'"
                            dfpa=pd.read_sql(op,mydb)
                            print(dfpa)
                            print()
                            print("What info of the patient would you like to edit?")
                            print("1.Name","2.Email ID","3.State & District","4.Address","5.Mobile_No","6.Age Group","7.Gender","8.Back",sep='\n')
                            print()
                            p_edit_opt=input("ENTER OPTION NUMBER: ")
                            print()
                            if(p_edit_opt=='1'):
                                ep_name=input("ENTER NEW NAME OF THE PATIENT: ")
                                ep_name=ep_name.upper()
                                mycursor.execute("update patients set Name='"+ep_name+"' where Record_ID='"+p_record_id+"' and Unit_Name='"+unit_name+"'")
                                mycursor.execute("commit")
                                print()
                                print("PATIENT'S NAME HAS BEEN UPDATED")
                                
                            elif(p_edit_opt=='2'):
                                ep_email=input("ENTER NEW EMAIL ID OF THE PATIENT: ")
                                ep_email=ep_email.lower()
                                mycursor.execute("update patients set Email_ID='"+ep_email+"' where Record_ID='"+p_record_id+"' and Unit_Name='"+unit_name+"'")
                                mycursor.execute("commit")
                                print()
                                print("PATIENT'S EMAIL ID HAS BEEN UPDATED")

                            elif(p_edit_opt=='3'):
                                INDIA.States_and_Districts_option()
                                mycursor.execute("update patients set State='"+INDIA.States_and_Districts_option.selected_state1+"',District='"+INDIA.States_and_Districts_option.selected_district1+"' where Record_ID='"+p_record_id+"' and Unit_Name='"+unit_name+"'")
                                mycursor.execute("commit")
                                print()
                                print("SELECTED STATE IS ",INDIA.States_and_Districts_option.selected_state1)
                                print("SELECTED DISTRICT IS ",INDIA.States_and_Districts_option.selected_district1)
                                print()
                                print("PATIENT'S STATE AND DISTRICT HAS BEEN UPDATED")

                            elif(p_edit_opt=='4'):
                                ep_address=input("ENTER NEW ADDRESS OF THE PATIENT: ")
                                mycursor.execute("update patients set Address='"+ep_address+"' where Record_ID='"+p_record_id+"' and Unit_Name='"+unit_name+"'")
                                mycursor.execute("commit")
                                print()
                                print("PATIENT'S ADDRESS HAS BEEN UPDATED")

                            elif(p_edit_opt=='5'):
                                ep_mobile=""
                                while(len(ep_mobile)>14)or(len(ep_mobile)<14):
                                    ep_mobile=input("ENTER PATIENT'S MOBILE NUMBER(format:-0091xxxxxxxxxx): ")
                                    if(len(ep_mobile)>14)or(len(ep_mobile)<14):
                                        print("INCORRECT FORMAT OF MOBILE NUMBER !!! :(","TRY AGAIN!!!",sep="\n")
                                        print()
                                mycursor.execute("update patients set Mobile_No='"+ep_mobile+"' where Record_ID='"+p_record_id+"' and Unit_Name='"+unit_name+"'")
                                mycursor.execute("commit")
                                print()
                                print("PATIENT'S MOBILE NUMBER HAS BEEN UPDATED")

                            elif(p_edit_opt=='6'):
                                print("SELECT AGE GROUP OF THE PATIENT TO EDIT: ")
                                print("1. 0-1","2. 2-11","3. 12-17","4. 18 and above","5. 65 and above",sep='\n')
                                print()
                                pa=""
                                while pa not in ['1','2','3','4','5']:
                                    pa=input("ENTER OPTION NUMBER: ")
                                    if(pa=='1'):
                                        ep_age="0-1"
                                    elif(pa=='2'):
                                        ep_age="2-11"
                                    elif(pa=='3'):
                                        ep_age="12-17"
                                    elif(pa=='4'):
                                        ep_age="18 and above"
                                    elif(pa=='5'):
                                        ep_age="65 and above"
                                    else:
                                        print("INCORRECT OPTION NUMBER !!! :(")
                                        print()

                                mycursor.execute("update patients set Age_Group='"+ep_age+"' where Record_ID='"+p_record_id+"' and Unit_Name='"+unit_name+"'")
                                mycursor.execute("commit")
                                print()
                                print("PATIENT'S AGE HAS BEEN UPDATED")

                            elif(p_edit_opt=='7'):
                                print("SELECT PATIENT'S GENDER TO EDIT: ")
                                print("1.Male","2.Female",sep='\n')
                                print()
                                pg=""
                                while pg not in ['1','2']:
                                    pg=input("ENTER OPTION NUMBER: ")
                                    if(pg=='1'):
                                        ep_gender="Male"
                                    elif(pg=='2'):
                                        ep_gender="Female"
                                    else:
                                        print("INCORRECT OPTION NUMBER !!! :(")
                                        print()
                                print()        
                                print("PATIENT'S GENDER HAS BEEN UPDATED")
                                
                                mycursor.execute("update patients set Gender='"+ep_gender+"' where Record_ID='"+p_record_id+"' and Unit_Name='"+unit_name+"'")
                                mycursor.execute("commit")
                            print()
                            op="select Record_ID,Name,Email_ID,State,District,Address,Mobile_No,Age_Group,Gender,Date,Test_Type,Result from patients where Record_ID='"+p_record_id+"' and Unit_Name='"+unit_name+"'"
                            dfpa=pd.read_sql(op,mydb)
                            print(dfpa)
                            print()
                        
                        else:
                           print("INCORRECT MEDICAL RECORD SERIAL NUMBER !!! :(",
                                 "TRY AGAIN!!!",sep='\n')
                           
                elif(ed=='3'):
                    mycursor.execute("select* from test_agents where Username='"+uname+"'")
                    for mu in mycursor:
                        if("Mobile Unit" in mu):
                            p_record_id=str(input("ENTER MEDICAL RECORD SERIAL NUMBER OF THE PATIENT: "))
                            #p_record_id=str(p_record_id[:-1])
                            om="select* from test_agents where Username='"+uname+"'"
                            df4=pd.read_sql(om,mydb)
                            dk=df4["Unit_Name"]
                            unit_name=str(dk[0])
                            mycursor.execute("select count('Name') from patients where Record_ID='"+p_record_id+"' and Unit_Name='"+unit_name+"'")
                            print()
                            for bc in mycursor:
                                if(bc==(1,)):
                                    mycursor.execute("select* from patients where Record_ID='"+p_record_id+"' and Unit_Name='"+unit_name+"'")
                                    for pol in mycursor:
                                        if("Positive" in pol)or("Negative" in pol):
                                            print("THE RESULT OF THE PATIENT HAS ALREADY BEEN ENTERED AND IT CANNOT BE CHANGED AGAIN")
                                        else:
                                            op="select Record_ID,Name,Email_ID,State,District,Address,Mobile_No,Age_Group,Gender,Date,Test_Type,Result from patients where Record_ID='"+p_record_id+"' and Unit_Name='"+unit_name+"'"
                                            dfpa=pd.read_sql(op,mydb)
                                            print(dfpa)
                                            print()
                                            print("SELECT TEST-TYPE FOR THE PATIENT:")
                                            print("1.PCR test","2.Serology test","3.Isothermal nucleic acid amplification test","4.Antigen test","5.Imaging",
                                                  "6.Rapid diagnostic test (RDT)","7.Enzyme-linked immunosorbent assay (ELISA)","8.Neutralization assay",
                                                  "9.Chemiluminescent Immunoassay",sep='\n')
                                            print()
                                            tt=""
                                            while tt not in ['1','2','3','4','5','6','7','8','9']:
                                                tt=input("ENTER OPTION NUMBER: ")
                                                if(tt=='1'):
                                                    ep_test_type="PCR test"
                                                elif(tt=='2'):
                                                    ep_test_type="Serology test"
                                                elif(tt=='3'):
                                                    ep_test_type="Isothermal nucleic acid amplification test"
                                                elif(tt=='4'):
                                                    ep_test_type="Antigen test"
                                                elif(tt=='5'):
                                                    ep_test_type="Imaging"
                                                elif(tt=='6'):
                                                    ep_test_type="RDT"
                                                elif(tt=='7'):
                                                    ep_test_type="ELISA"
                                                elif(tt=='8'):
                                                    ep_test_type="Neutralization assay"
                                                elif(tt=='9'):
                                                    ep_test_type="Chemiluminescent Immunoassay"
                                                else:
                                                    print("INCORRECT OPTION NUMBER !!! :(")
                                                    print()
                                                    
                                            print()
                                            print("THE TEST DONE FOR YOUR PATIENT IS ",ep_test_type)
                                            print()
                                            print("SELECT RESULT OF THE PATIENT:")
                                            print("1.Positive","2.Negative",sep='\n')
                                            print()
                                            par=""
                                            while par not in ['1','2']:
                                                par=input("ENTER OPTION NUMBER: ")
                                                if(par=='1'):
                                                    ep_result="Positive"
                                                elif(par=='2'):
                                                    ep_result="Negative"
                                                else:
                                                    print("INCORRECT OPTION NUMBER !!! :(")
                                                    print()

                                            ok="select* from test_agents where Username='"+uname+"'"
                                            df_show_tprofile=pd.read_sql(ok,mydb)
                                            de=df_show_tprofile["TA_Emp_No"]
                                            p_TA_emp_no=str(de[0])
                                            print()
                                            mycursor.execute("update patients set Result='"+ep_result+"',Test_Type='"+ep_test_type+"',LT_Emp_No='"+p_TA_emp_no+"' where Record_ID='"+p_record_id+"' and Unit_Name='"+unit_name+"'")
                                            mycursor.execute("commit")
                                            print("PATIENT'S RESULT HAS BEEN ENTERED AS ",ep_result)
                                            print()
                                            op="select Record_ID,Name,Email_ID,State,District,Address,Mobile_No,Age_Group,Gender,Date,Test_Type,Result from patients where Record_ID='"+p_record_id+"'"
                                            dfpa=pd.read_sql(op,mydb)
                                            print(dfpa)
                                            print()

                                else:
                                    print("INCORRECT MEDICAL RECORD SERIAL NUMBER !!! :(","TRY AGAIN!!!",sep='\n') 
                        else:
                            print("THIS FEATURE IS NOT AVAILABLE FOR YOUR ACCOUNT TYPE")

            elif(th=='2'):
                print("VIEW REPORT OF THE PATIENT BY:")
                print("1.Medical record serial number","2.Mobile number of the patient","3.Back",sep='\n')
                print()
                rt=input("ENTER OPTION NUMBER: ")
                om="select* from test_agents where Username='"+uname+"'"
                df4=pd.read_sql(om,mydb)
                dk=df4["Unit_Name"]
                unit_name=str(dk[0])
                print()
                if(rt=='1'):
                    mr=str(input("ENTER MEDICAL RECORD SERIAL NUMBER OF THE PATIENT: "))
                    #mr=str(mr[:-1])
                    print()
                    mycursor.execute("select count('Record_ID') from patients where Record_ID='"+mr+"' and Unit_Name='"+unit_name+"'")
                    for cv in mycursor:
                        if(cv==(1,)):
                            bl="select Record_ID,Name,Email_ID,State,District,Address,Mobile_No,Age_Group,Gender,Date,Test_Type,Result from patients where Record_ID='"+mr+"' and Unit_Name='"+unit_name+"'"
                            view_result=pd.read_sql(bl,mydb)
                            print(view_result)

                        else:
                            print("INCORRECT MEDICAL RECORD SERIAL NUMBER !!! :(","TRY AGAIN!!!",sep='\n')
                            
                elif(rt=='2'):
                    mn=input("ENTER MOBILE NO. OF THE PATIENT(format:- 0091xxxxxxxxxx): ")
                    print()
                    mycursor.execute("select count('Name') from patients where Mobile_No='"+mn+"' and Unit_Name='"+unit_name+"'")
                    for dv in mycursor:
                        if(dv==(1,)):
                            if(len(mn)==14):
                                cl="select Record_ID,Name,Email_ID,State,District,Address,Mobile_No,Age_Group,Gender,Date,Test_Type,Result from patients where Mobile_No='"+mn+"' and Unit_Name='"+unit_name+"'"
                                view_mresult=pd.read_sql(cl,mydb)
                                print(view_mresult)
                            else:
                                print("INCORRECT FORMAT OF MOBILE NUMBER !!! :(","TRY AGAIN!!!",sep="\n")

                        else:
                            print("INCORRECT MOBILE NUMBER !!! :(","TRY AGAIN!!!",sep='\n')
                                    
            elif(th=='3'):
                print()
                print("What info would you like to edit?")
                print("1.Email ID","2.Mobile No.","3.State & District","4.Change Password","5.Back",sep="\n")
                print()
                edit_opt=input("ENTER OPTION NUMBER: ")
                print()
                            
                if(edit_opt=='1'):
                    new_email=str(input("ENTER NEW EMAIL ID: "))
                    email_id=new_email.lower()
                    if("@" in email_id):
                        mycursor.execute("update test_agents set Email_ID='"+email_id+"' where Username='"+uname+"'")
                        mycursor.execute("commit")
                        print()
                        print("YOUR EMAIL ID HAS BEEN UPDATED")
                    else:
                        print()
                        print("YOUR EMAIL ID CANNOT BE ACCEPTED !!! :(","TRY AGAIN!!!",sep="\n")

                elif(edit_opt=='2'):
                    new_mobile_no=input("ENTER NEW MOBILE NO.(format:- 0091xxxxxxxxxx): ")
                    print()
                    if(len(new_mobile_no)==14):
                        mycursor.execute("update test_agents set Mobile_No='"+new_mobile_no+"' where Username='"+uname+"'")
                        mycursor.execute("commit")
                        print("YOUR MOBILE NO. HAS BEEN UPDATED")

                    else:
                        print("INCORRECT FORMAT OF MOBILE NUMBER !!! :(","TRY AGAIN!!!",sep="\n")
                                     
                elif(edit_opt=='3'):
                    INDIA.States_and_Districts_option()
                    mycursor.execute("update test_agents set State='"+INDIA.States_and_Districts_option.selected_state1+"',District='"+INDIA.States_and_Districts_option.selected_district1+"' where Username='"+uname+"'")
                    mycursor.execute("commit")
                    print("YOUR SELECTED STATE IS ",INDIA.States_and_Districts_option.selected_state1)
                    print("YOUR SELECTED DISTRICT IS ",INDIA.States_and_Districts_option.selected_district1)
                    print()
                    print("YOUR STATE AND DISTRICT HAS BEEN UPDATED")

                elif(edit_opt=='4'):
                    email=input("ENTER EMAIL ID TO VERIFY: ")
                    email=email.lower()
                    mobile_no=input("ENTER MOBILE NO. TO VERIFY(format:- 0091xxxxxxxxxx): ")
                    print()
                    if(len(mobile_no)==14):
                        mycursor.execute("select count('Agent_Name') from test_agents where Email_ID='"+email+"' and Mobile_No='"+mobile_no+"' and Username='"+uname+"'")
                        for d in mycursor:
                            if(d==(1,)):
                                password_check.Strong_password_checker()
                                mycursor.execute("update test_agents set Password='"+password_check.Strong_password_checker.clear_check+"' where Email_ID='"+email+"' and Mobile_No='"+mobile_no+"' and Username='"+uname+"'")
                                mycursor.execute("commit")
                                print()
                                print("YOUR PASSWORD HAS BEEN CHANGED")
        
                            else:
                                print()
                                print("INCORRECT EMAIL ID OR MOBILE NO. !!! :(","TRY AGAIN!!!",sep="\n")
                    else:
                        print()
                        print("INCORRECT EMAIL ID OR MOBILE NO. !!! :(","TRY AGAIN!!!",sep="\n")

            elif(th=='4'):
                pme=str(input("ENTER YOUR EMPLOYEE NUMBER: "))
                mycursor.execute("select count('Agent_Name') from test_agents where Username='"+uname+"' and TA_Emp_No='"+pme+"'")
                print()
                for nuh in mycursor:
                    if(nuh==(1,)):
                        print("Profile")
                        print("=======")
                        print("____________________________________________________________","\n")
                        sp="select* from test_agents where Username='"+uname+"' and TA_Emp_No='"+pme+"'"
                        df_show_profile=pd.read_sql(sp,mydb)
                        profile=df_show_profile.to_dict(orient="list")
                        for key,value in profile.items():
                            print(key,":","\t",value)
                    else:
                        print("INCORRECT EMPLOYEE NUMBER !!! :(","TRY AGAIN!!!",sep='\n')
                        
                
            elif(th=='5'):
                Contact_us.contact_DHR()
                
            elif(th=='6'):
                quit()

            else:
                print("INCORRECT OPTION NUMBER !!! :(")



        
