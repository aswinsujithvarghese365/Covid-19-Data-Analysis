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


def lab_techs():
    mycursor=mydb.cursor()
    mycursor.execute("commit")
    j=1
    while(j>0):
        # Getting Login Credential from User
        tname=str(input("ENTER USERNAME: "))
        password=getpass.getpass(prompt="ENTER PASSWORD: ")
        mycursor.execute("select count('Agent_Name') from lab_technicians where Username='"+tname+"' and Password='"+password+"'")
        for q in mycursor:
            if(q==(1,)):
                print()
                y="ACCESS GRANTED"
                print(y)
                print()
                j=0
                
            else:
                print()
                print("ACCESS DENIED")
                y="INVALID USERNAME OR PASSWORD"
                print(y)
                print()
                        

    if(y=="ACCESS GRANTED"):
        while True:
            hg="select LT_Emp_No from lab_technicians where Username='"+tname+"'"
            mp=pd.read_sql(hg,mydb)
            emp=mp["LT_Emp_No"]
            ltemp=str(emp[0])
            # Menu according to the rights of the user
            print("____________________________________________________________","\n")
            print("What would you like to do?")
            print("1.Add/View Results of Patients","2.Edit Profile","3.Show Profile","4.Contact Us",
                  "5.Quit Application",sep="\n")
            print()
            lh=input("ENTER OPTION NUMBER: ")
            print("____________________________________________________________","\n")

            if(lh=='1'):
                print("What data would you like to enter?")
                print("1.Add test-type and result of the patient","2.View report of the patient","3.Back",sep="\n")
                print()
                fd=input("ENTER OPTION NUMBER: ")
                print()

                if(fd=='1'):
                    lp_record_id=input("ENTER MEDICAL RECORD SERIAL NUMBER OF THE PATIENT: ")
                    #lp_record_id=str(lp_record_id[:-1])
                    lb="select* from lab_technicians where Username='"+tname+"'"
                    df3=pd.read_sql(lb,mydb)
                    kb=df3["Unit_Name"]
                    unit_tname=str(kb[0])
                    mycursor.execute("select count('Name') from patients where Record_ID='"+lp_record_id+"' and Unit_Name='"+unit_tname+"'")
                    print()
                    for qc in mycursor:
                        if(qc==(1,)):
                            # Entering Test type of the patient
                            mycursor.execute("select* from patients where Record_ID='"+lp_record_id+"' and Unit_Name='"+unit_tname+"'")
                            for lop in mycursor:
                                if("Positive" in lop)or("Negative" in lop):
                                    print("THE RESULT OF THE PATIENT HAS ALREADY BEEN ENTERED AND IT CANNOT BE CHANGED AGAIN")
                                else:
                                    lops="select Record_ID,Name,Email_ID,State,District,Address,Mobile_No,Age_Group,Gender,Date,Test_Type,Result from patients where Record_ID='"+lp_record_id+"' and Unit_Name='"+unit_tname+"'"
                                    dflpa=pd.read_sql(lops,mydb)
                                    print(dflpa)
                                    print()
                                    print("SELECT TEST-TYPE FOR THE PATIENT:")
                                    print("1.PCR test","2.Serology test","3.Isothermal nucleic acid amplification test","4.Antigen test","5.Imaging",
                                          "6.Rapid diagnostic test (RDT)","7.Enzyme-linked immunosorbent assay (ELISA)","8.Neutralization assay",
                                          "9.Chemiluminescent Immunoassay",sep='\n')
                                    print()
                                    tnt=""
                                    while tnt not in ['1','2','3','4','5','6','7','8','9']:
                                        tnt=input("ENTER OPTION NUMBER: ")
                                        if(tnt=='1'):
                                            test_type="PCR test"
                                        elif(tnt=='2'):
                                            test_type="Serology test"
                                        elif(tnt=='3'):
                                            test_type="Isothermal nucleic acid amplification test"
                                        elif(tnt=='4'):
                                            test_type="Antigen test"
                                        elif(tnt=='5'):
                                            test_type="Imaging"
                                        elif(tnt=='6'):
                                            test_type="RDT"
                                        elif(tnt=='7'):
                                            test_type="ELISA"
                                        elif(tnt=='8'):
                                            test_type="Neutralization assay"
                                        elif(tnt=='9'):
                                            test_type="Chemiluminescent Immunoassay"
                                        else:
                                            print("INCORRECT OPTION NUMBER !!! :(")
                                            print()
                                            
                                    print()    
                                    print("THE TEST DONE FOR YOUR PATIENT IS ",test_type)
                                    print()
                                    print("SELECT RESULT OF THE PATIENT:")
                                    print("1.Positive","2.Negative",sep='\n')
                                    print()
                                    pr=""
                                    while pr not in ['1','2']:
                                        # Entering Test result of the patient
                                        pr=input("ENTER OPTION NUMBER: ")
                                        if(pr=='1'):
                                            result="Positive"
                                        elif(pr=='2'):
                                            result="Negative"
                                        else:
                                            print("INCORRECT OPTION NUMBER !!! :(")
                                            print()

                                    print()
                                    mycursor.execute("update patients set Result='"+result+"',Test_Type='"+test_type+"',LT_Emp_No='"+ltemp+"' where Record_ID='"+lp_record_id+"' and Unit_Name='"+unit_tname+"'")
                                    mycursor.execute("commit")
                                    print("PATIENT'S RESULT HAS BEEN ENTERED AS ",result)
                                    print()
                                    lop="select Record_ID,Name,Email_ID,State,District,Address,Mobile_No,Age_Group,Gender,Date,Test_Type,Result from patients where Record_ID='"+lp_record_id+"' and Unit_Name='"+unit_tname+"'"
                                    dflpa=pd.read_sql(lop,mydb)
                                    print(dflpa)
                                    print()
                                
                        else:
                            print("INCORRECT MEDICAL RECORD SERIAL NUMBER !!! :(","TRY AGAIN!!!",sep='\n')

                elif(fd=='2'):
                    # to view report of a patient
                    print("VIEW REPORT OF THE PATIENT BY:")
                    print("1.Medical record serial number","2.Mobile number of the patient","3.Back",sep='\n')
                    print()
                    pk=input("ENTER OPTION NUMBER: ")
                    lb="select* from lab_technicians where Username='"+tname+"'"
                    df3=pd.read_sql(lb,mydb)
                    kb=df3["Unit_Name"]
                    unit_tname=str(kb[0])
                    print()
                    if(pk=='1'):
                        mrsn=input("ENTER MEDICAL RECORD SERIAL NUMBER OF THE PATIENT: ")
                        #mrsn=str(mrsn[:-1])
                        print()
                        mycursor.execute("select count('Record_ID') from patients where Record_ID='"+mrsn+"' and Unit_Name='"+unit_tname+"'")
                        for pv in mycursor:
                            if(pv==(1,)):
                                dl="select Record_ID,Name,Email_ID,State,District,Address,Mobile_No,Age_Group,Gender,Date,Test_Type,Result from patients where Record_ID='"+mrsn+"' and Unit_Name='"+unit_tname+"'"
                                view_mrsn_result=pd.read_sql(dl,mydb)
                                print(view_mrsn_result)

                            else:
                                print("INCORRECT MEDICAL RECORD SERIAL NUMBER !!! :(","TRY AGAIN!!!",sep='\n')
                            
                    elif(pk=='2'):
                        mnp=input("ENTER MOBILE NO. OF THE PATIENT(format:- 0091xxxxxxxxxx): ")
                        print()
                        mycursor.execute("select count('Name') from patients where Mobile_No='"+mnp+"' and Unit_Name='"+unit_tname+"'")
                        for mv in mycursor:
                            if(mv==(1,)):
                                if(len(mnp)==14):
                                    el="select Record_ID,Name,Email_ID,State,District,Address,Mobile_No,Age_Group,Gender,Date,Test_Type,Result from patients where Mobile_No='"+mnp+"' and Unit_Name='"+unit_tname+"'"
                                    view_mnp_result=pd.read_sql(el,mydb)
                                    print(view_mnp_result)
                                else:
                                    print("INCORRECT FORMAT OF MOBILE NUMBER !!! :(","TRY AGAIN!!!",sep="\n")

                            else:
                                print("INCORRECT MOBILE NUMBER !!! :(","TRY AGAIN!!!",sep='\n')
                           
            elif(lh=='2'):
                # Edit profile details
                print()
                print("What info would you like to edit?")
                print("1.Email ID","2.Mobile No.","3.State & District","4.Change Password","5.Back",sep="\n")
                print()
                lt_edit_opt=input("ENTER OPTION NUMBER: ")
                print()
                            
                if(lt_edit_opt=='1'):
                    l_new_email=input("ENTER NEW EMAIL ID: ")
                    l_new_email=l_new_email.lower()
                    if("@" in l_new_email):
                        mycursor.execute("update lab_technicians set Email_ID='"+l_new_email+"' where Username='"+tname+"'")
                        mycursor.execute("commit")
                        print()
                        print("YOUR EMAIL ID HAS BEEN UPDATED")
                    else:
                        print()
                        print("YOUR EMAIL ID CANNOT BE ACCEPTED !!! :(","TRY AGAIN!!!",sep="\n")

                elif(lt_edit_opt=='2'):
                    l_new_mobile_no=input("ENTER NEW MOBILE NO.(format:- 0091xxxxxxxxxx): ")
                    print()
                    if(len(l_new_mobile_no)==14):
                        mycursor.execute("update lab_technicians set Mobile_No='"+l_new_mobile_no+"' where Username='"+tname+"'")
                        mycursor.execute("commit")
                        print("YOUR MOBILE NO. HAS BEEN UPDATED")

                    else:
                        print("INCORRECT FORMAT OF MOBILE NUMBER !!! :(","TRY AGAIN!!!",sep="\n")
                                     
                elif(lt_edit_opt=='3'):
                    INDIA.States_and_Districts_option()
                    mycursor.execute("update lab_technicians set State='"+INDIA.States_and_Districts_option.selected_state1+"',District='"+INDIA.States_and_Districts_option.selected_district1+"' where Username='"+tname+"'")
                    mycursor.execute("commit")
                    print("YOUR SELECTED STATE IS ",INDIA.States_and_Districts_option.selected_state1)
                    print("YOUR SELECTED DISTRICT IS ",INDIA.States_and_Districts_option.selected_district1)
                    print()
                    print("YOUR STATE AND DISTRICT HAS BEEN UPDATED")

                elif(lt_edit_opt=='4'):
                    l_email=input("ENTER EMAIL ID TO VERIFY: ")
                    l_email=l_email.lower()
                    l_mobile_no=input("ENTER MOBILE NO. TO VERIFY(format:- 0091xxxxxxxxxx): ")
                    print()
                    if(len(l_mobile_no)==14):
                        mycursor.execute("select count('Agent_Name') from lab_technicians where Email_ID='"+l_email+"' and Mobile_No='"+l_mobile_no+"' and Username='"+tname+"'")
                        for w in mycursor:
                            if(w==(1,)):
                                password_check.Strong_password_checker()
                                mycursor.execute("update lab_technicians set Password='"+password_check.Strong_password_checker.clear_check+"' where Email_ID='"+l_email+"' and Mobile_No='"+l_mobile_no+"' and Username='"+tname+"'")
                                mycursor.execute("commit")
                                print()
                                print("YOUR PASSWORD HAS BEEN CHANGED")
        
                            else:
                                print()
                                print("INCORRECT EMAIL ID OR MOBILE NO. !!! :(","TRY AGAIN!!!",sep="\n")
                    else:
                        print()
                        print("INCORRECT EMAIL ID OR MOBILE NO. !!! :(","TRY AGAIN!!!",sep="\n")

            elif(lh=='3'):
                # viewing profile
                lpme=str(input("ENTER YOUR EMPLOYEE NUMBER: "))
                mycursor.execute("select count('Agent_Name') from lab_technicians where Username='"+tname+"' and LT_Emp_No='"+lpme+"'")
                print()
                for lnuh in mycursor:
                    if(lnuh==(1,)):
                        print("Profile")
                        print("=======")
                        print("____________________________________________________________","\n")
                        so="select* from lab_technicians where Username='"+tname+"' and LT_Emp_No='"+lpme+"'"
                        df_show_lprofile=pd.read_sql(so,mydb)
                        l_profile=df_show_lprofile.to_dict(orient="list")
                        for key,value in l_profile.items():
                            print(key,":","\t",value)
                    else:
                        print("INCORRECT EMPLOYEE NUMBER !!! :(","TRY AGAIN!!!",sep='\n')
                
            elif(lh=='4'):
                # contact us page
                Contact_us.contact_DHR()
                
            elif(lh=='5'):
                quit()
                
            else:
                print("INCORRECT OPTION NUMBER !!! :(")
