import re
import getpass
import INDIA
import password_check
import Contact_us
import matplotlib.pyplot as plt
import mysql.connector
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
cnx=create_engine('mysql+mysqlconnector://root:ash@503.#@localhost:3306/Covid_Data_Analysis')

mydb=mysql.connector.connect(host="localhost",
                            user="root",
                            password="ash@503.#",
                            database="Covid_Data_Analysis")

# if you wish to sign up, pls contact the super admin team # default code for admin 1111

def admins():
    mycursor=mydb.cursor()
    mycursor.execute("commit")
    l=1
    while(l>0):
        aname=str(input("ENTER USERNAME: "))
        passds=getpass.getpass(prompt="ENTER PASSWORD: ")
        mycursor.execute("select count('Admin_Name') from admins where Username='"+aname+"' and Password='"+passds+"'")
        for ch in mycursor:
            if(ch==(1,)):
                print()
                z="ACCESS GRANTED"
                print(z)
                print()
                l=0
                
            else:
                print()
                print("ACCESS DENIED")
                z="INVALID USERNAME OR PASSWORD"
                print(z)
                print()                        

    if(z=="ACCESS GRANTED"):
        while True:
            print("____________________________________________________________","\n")
            print("What would you like to do?")
            print("1.Sign up for Test Agents or Lab Technicians","2.Report Manager","3.Edit Profile","4.Show Profile","5.Contact Us","6.Quit Application",sep="\n")
            print()
            ah=input("ENTER OPTION NUMBER: ")
            print("____________________________________________________________","\n")

            if(ah=='1'):
                print("Which one would you like to sign up for?")
                print("1.Test Agent","2.Lab Technician","3.Back",sep='\n')
                print()
                la=input("ENTER OPTION NUMBER: ")
                ui="select* from admins where Username='"+aname+"'"
                df_admin_profile=pd.read_sql(ui,mydb)
                le=df_admin_profile["State"]
                li=df_admin_profile["District"]
                lo=df_admin_profile["Test_Center"]
                lu=df_admin_profile["Unit_Name"]
                a_state=str(le[0])
                a_district=str(li[0])
                a_test_center=str(lo[0])
                a_unit_name=str(lu[0])
                print()
                if(la=='1'):
                    eta_name=input("ENTER NAME OF THE TEST AGENT: ")
                    eta_name=eta_name.upper()
                    print()
                    print("SELECT TEST AGENT'S GENDER: ")
                    print("1.Male","2.Female",sep='\n')
                    print()
                    lj=""
                    while lj not in ['1','2']:
                        lj=input("ENTER OPTION NUMBER: ")
                        if(lj=='1'):
                            eta_gender="Male"
                        elif(lj=='2'):
                            eta_gender="Female"
                        else:
                            print("INCORRECT OPTION NUMBER !!! :(")
                            print()
                    print()                        
                    print("TEST AGENT'S GENDER IS ",eta_gender)
                    print()
                    ti=1
                    while(ti>0):
                        eta_mobile_no=input("ENTER MOBILE NUMBER OF THE TEST AGENT(format:- 0091xxxxxxxxxx): ")
                        print()
                        if(len(eta_mobile_no)==14):
                            eta_mobile_no=str(eta_mobile_no)
                            ti=0
                        else:
                            print("INCORRECT FORMAT OF MOBILE NUMBER !!! :(","TRY AGAIN!!!",sep="\n")
                            print()
                    en=1
                    while(en>0):
                        eta_email=input("ENTER EMAIL ID OF THE TEST AGENT: ")
                        print()
                        if("@" in eta_email):
                            eta_email=eta_email.lower()
                            en=0
                        else:
                            print("EMAIL ID OF THE TEST AGENT CANNOT BE ACCEPTED !!! :(","TRY AGAIN!!!",sep="\n")
                            print()

                    password_check.Username_checker()
                    print()
                    password_check.Strong_password_checker()
                    print()
                    print("SELECT TEST CENTER OF THE TEST AGENT: ")
                    print("1."+a_test_center,"2.Mobile Unit",sep='\n')
                    print()
                    mh=""
                    while mh not in ['1','2']:
                        mh=input("ENTER OPTION NUMBER: ")
                        if(mh=='1'):
                            eta_test_center=a_test_center
                        elif(mh=='2'):
                            eta_test_center="Mobile Unit"
                        else:
                            print("INCORRECT OPTION NUMBER !!! :(")
                            print()
                    print()
                    print("SELECTED TEST CENTER OF THE TEST AGENT IS ",eta_test_center)
                    print()
                    mc="select max(TA_Emp_No) from test_agents"
                    max_temp=pd.read_sql(mc,mydb)
                    mg=max_temp["max(TA_Emp_No)"]
                    eta_ta_emp=str(mg[0]+1)
                    print("EMPLOYEE NUMBER OF THE TEST AGENT IS ",eta_ta_emp)
                    print()
                    mycursor.execute("insert into test_agents values('"+eta_name+"','"+eta_gender+"','"+eta_mobile_no+"','"+eta_email+"','"+eta_ta_emp+"','"+password_check.Username_checker.clear_uname_check+"','"+password_check.Strong_password_checker.clear_check+"','"+a_state+"','"+a_district+"','"+eta_test_center+"','"+a_unit_name+"')")
                    mycursor.execute("commit")
                    print("SIGN UP FOR TEST AGENT HAS BEEN COMPLETED SUCCESSFULLY !!! :)")
                        
                elif(la=='2'):
                    elt_name=input("ENTER NAME OF THE LAB TECHNICIAN: ")
                    elt_name=elt_name.upper()
                    print()
                    print("SELECT LAB TECHNICIAN'S GENDER: ")
                    print("1.Male","2.Female",sep='\n')
                    print()
                    ij=""
                    while ij not in ['1','2']:
                        ij=input("ENTER OPTION NUMBER: ")
                        if(ij=='1'):
                            elt_gender="Male"
                        elif(ij=='2'):
                            elt_gender="Female"
                        else:
                            print("INCORRECT OPTION NUMBER !!! :(")
                            print()
                    print()                        
                    print("LAB TECHNICIAN'S GENDER IS ",elt_gender)
                    print()
                    hi=1
                    while(hi>0):
                        elt_mobile_no=input("ENTER MOBILE NUMBER OF THE LAB TECHNICIAN(format:- 0091xxxxxxxxxx): ")
                        print()
                        if(len(elt_mobile_no)==14):
                            elt_mobile_no=str(elt_mobile_no)
                            hi=0
                        else:
                            print("INCORRECT FORMAT OF MOBILE NUMBER !!! :(","TRY AGAIN!!!",sep="\n")
                            print()
                    efg=1
                    while(efg>0):
                        elt_email=input("ENTER EMAIL ID OF THE LAB TECHNICIAN: ")
                        print()
                        if("@" in elt_email):
                            elt_email=elt_email.lower()
                            efg=0
                        else:
                            print("EMAIL ID OF THE LAB TECHNICIAN CANNOT BE ACCEPTED !!! :(","TRY AGAIN!!!",sep="\n")
                            print()

                    password_check.Username_checker()
                    print()
                    password_check.Strong_password_checker()
                    print()
                    print("SELECT TEST CENTER OF THE TEST AGENT: ")
                    print("1."+a_test_center,"2.Mobile Unit",sep='\n')
                    print()
                    kh=""
                    while kh not in ['1','2']:
                        kh=input("ENTER OPTION NUMBER: ")
                        if(kh=='1'):
                            elt_test_center=a_test_center
                        elif(kh=='2'):
                            elt_test_center="Mobile Unit"
                        else:
                            print("INCORRECT OPTION NUMBER !!! :(")
                            print()
                    print()
                    print("SELECTED TEST CENTER OF THE TEST AGENT IS ",elt_test_center)
                    print()    
                    km="select max(LT_Emp_No) from lab_technicians"
                    max_lemp=pd.read_sql(km,mydb)
                    kg=max_lemp["max(LT_Emp_No)"]
                    elt_lt_emp=str(kg[0]+1)
                    print("EMPLOYEE NUMBER OF THE LAB TECHNICIAN IS ",elt_lt_emp)
                    print()
                    mycursor.execute("insert into lab_technicians values('"+elt_name+"','"+elt_gender+"','"+elt_mobile_no+"','"+elt_email+"','"+elt_lt_emp+"','"+password_check.Username_checker.clear_uname_check+"','"+password_check.Strong_password_checker.clear_check+"','"+a_state+"','"+a_district+"','"+elt_test_center+"','"+a_unit_name+"')")
                    mycursor.execute("commit")
                    print("SIGN UP FOR LAB TECHNICIAN HAS BEEN COMPLETED SUCCESSFULLY !!! :)")
                    

            elif(ah=='2'):
                print("How would you like to view the report of the patient?")
                print("1.View report of a particular patient","2.View reports of all the patients","3.View number of positive/negative cases","4.View number of positive/negative cases of a specific date","5.Check Activity of Test Agents/Lab Technicians","6.View details of the employees","7.Back",sep='\n')
                print()
                hu="select* from admins where Username='"+aname+"'"
                df_view=pd.read_sql(hu,mydb)
                dkd=df_view["Unit_Name"]
                alt_unit_name=str(dkd[0])
                ou=input("ENTER OPTION NUMBER: ")
                print()
                if(ou=='1'):
                    print("VIEW REPORT OF THE PATIENT BY:")
                    print("1.Medical record serial number","2.Mobile number of the patient",sep='\n')
                    print()
                    kl=input("ENTER OPTION NUMBER: ")
                    print()
                    if(kl=='1'):
                        mb=input("ENTER MEDICAL RECORD SERIAL NUMBER OF THE PATIENT: ")
                        #mb=str(mb[:-1])
                        print()
                        mycursor.execute("select count('Record_ID') from patients where Record_ID='"+mb+"' and Unit_Name='"+alt_unit_name+"'")
                        for dd in mycursor:
                            if(dd==(1,)):
                                h1="select Record_ID,Name,Email_ID,State,District,Address,Mobile_No,Age_Group,Gender,Date,TA_Emp_No,LT_Emp_No,Test_Type,Result from patients where Record_ID='"+mb+"' and Unit_Name='"+alt_unit_name+"'"
                                p_view_result=pd.read_sql(h1,mydb)
                                print(p_view_result)

                            else:
                                print("INCORRECT MEDICAL RECORD SERIAL NUMBER !!! :(","TRY AGAIN!!!",sep='\n')
                        
                    elif(kl=='2'):
                        mf=input("ENTER MOBILE NO. OF THE PATIENT(format:- 0091xxxxxxxxxx): ")
                        print()
                        mycursor.execute("select count('Name') from patients where Mobile_No='"+mf+"' and Unit_Name='"+alt_unit_name+"'")
                        for oo in mycursor:
                            if(oo==(1,)):
                                if(len(mf)==14):
                                    g1="select Record_ID,Name,Email_ID,State,District,Address,Mobile_No,Age_Group,Gender,Date,TA_Emp_No,LT_Emp_No,Test_Type,Result from patients where Mobile_No='"+mf+"' and Unit_Name='"+alt_unit_name+"'"
                                    p_view_mresult=pd.read_sql(g1,mydb)
                                    print(p_view_mresult)
                                else:
                                    print("INCORRECT FORMAT OF MOBILE NUMBER !!! :(","TRY AGAIN!!!",sep="\n")
                            else:
                                print("INCORRECT MOBILE NUMBER !!! :(","TRY AGAIN!!!",sep='\n')
                    else:
                        print("INCORRECT OPTION NUMBER !!! :(")
                
                elif(ou=='2'):
                    oy="select Record_ID,Name,Email_ID,State,District,Address,Mobile_No,Age_Group,Gender,Date,TA_Emp_No,LT_Emp_No,Test_Type,Result from patients where Unit_Name='"+alt_unit_name+"'"
                    entire_results=pd.read_sql(oy,mydb)
                    print(entire_results)
                    print()

                elif(ou=='3'):
                    oj="select Record_ID,Name,Email_ID,State,District,Address,Mobile_No,Age_Group,Gender,Date,TA_Emp_No,LT_Emp_No,Test_Type,Result from patients where Result='Positive' and Unit_Name='"+alt_unit_name+"'"
                    oc="select Record_ID,Name,Email_ID,State,District,Address,Mobile_No,Age_Group,Gender,Date,TA_Emp_No,LT_Emp_No,Test_Type,Result from patients where Result='Negative' and Unit_Name='"+alt_unit_name+"'"
                    oe=pd.read_sql(oj,mydb)
                    ow=pd.read_sql(oc,mydb)
                    p_positive=oe["Record_ID"].count()
                    p_negative=ow["Record_ID"].count()
                    print('\t',"                                                               POSITIVE RESULTS")
                    print('\t',"                                                               ----------------")
                    print(oe,'\n')
                    print('\t',"                                                               NEGATIVE RESULTS")
                    print('\t',"                                                               ----------------")
                    print(ow,'\n')
                    no_of_pcases=[p_positive]
                    no_of_ncases=[p_negative]
                    width=0.3
                    plt.bar("Positive",no_of_pcases,width,color="orange",edgecolor="black")
                    plt.bar("Negative",no_of_ncases,width,color="blue",edgecolor="black")
                    plt.title("REPORT",fontsize=20)
                    plt.xlabel("Results ->",fontsize=15)
                    plt.ylabel("Number of Cases ->",fontsize=15)
                    plt.grid()
                    plt.show()

                elif(ou=='4'):
                    pn_date=str(input("ENTER DATE(format:-YYYY-MM-DD): "))
                    print()
                    pnoj="select Record_ID,Name,Email_ID,State,District,Address,Mobile_No,Age_Group,Gender,TA_Emp_No,LT_Emp_No,Test_Type,Result from patients where Result='Positive' and Unit_Name='"+alt_unit_name+"' and Date='"+pn_date+"'"
                    pnoc="select Record_ID,Name,Email_ID,State,District,Address,Mobile_No,Age_Group,Gender,TA_Emp_No,LT_Emp_No,Test_Type,Result from patients where Result='Negative' and Unit_Name='"+alt_unit_name+"' and Date='"+pn_date+"'"
                    pnoe=pd.read_sql(pnoj,mydb)
                    pnow=pd.read_sql(pnoc,mydb)
                    pn_positive=pnoe["Record_ID"].count()
                    pn_negative=pnow["Record_ID"].count()
                    print('\t',"                                                               POSITIVE RESULTS")
                    print('\t',"                                                               ----------------")
                    print(pnoe,'\n')
                    print('\t',"                                                               NEGATIVE RESULTS")
                    print('\t',"                                                               ----------------")
                    print(pnow,'\n')
                    no_of_pcases=[pn_positive]
                    no_of_ncases=[pn_negative]
                    width=0.3
                    plt.bar("Positive",no_of_pcases,width,color="orange",edgecolor="black")
                    plt.bar("Negative",no_of_ncases,width,color="blue",edgecolor="black")
                    plt.title("REPORT",fontsize=20)
                    plt.xlabel("Results ->",fontsize=15)
                    plt.ylabel("Number of Cases ->",fontsize=15)
                    plt.grid()
                    plt.show()

                elif(ou=='5'):
                    print("Which employee would you like to check the activity of?")
                    print("1.Test Agent","2.Lab Technician",sep='\n')
                    print()
                    mv=input("ENTER OPTION NUMBER: ")
                    print()
                    print("SELECT TIME LIMIT TO CHECK THE ACTIVITY OF THE EMPLOYEE: ")
                    print("1.Specific date","2.Today","3.Last one week","4.This month",sep='\n')
                    print()
                    lg=input("ENTER OPTION NUMBER: ")
                    print()
                    ui="select* from admins where Username='"+aname+"'"
                    df_admin_profile=pd.read_sql(ui,mydb)
                    lu=df_admin_profile["Unit_Name"]
                    a_unit_name=str(lu[0])
                    if(mv=='1'):
                        cg="select distinct(TA_Emp_No) from patients where Unit_Name='"+a_unit_name+"'"
                        bg=pd.read_sql(cg,mydb)
                        ag=bg['TA_Emp_No'].tolist()
                        qg=len(ag)
                        wg=[]
                        lh=[]
                        if(lg=='1'):
                            date=str(input("ENTER DATE(format:-YYYY-MM-DD): "))
                            print()
                            print("                  Test Agent Emp.No.") 
                            for yd in range(0,qg):
                                rf=str(ag[yd])
                                lh.append(rf)
                                rg="select count('Record_ID') from patients where TA_Emp_No='"+rf+"' and Date='"+date+"'"
                                aw=pd.read_sql(rg,mydb)
                                tw=aw["count('Record_ID')"]
                                br=tw[0]
                                aw.columns=[rf]
                                aw.index=["Patients Treated"]
                                wg.append(br)
                                print(aw)
                                plt.bar(lh,wg,width=0.2,color="red",edgecolor="black")
                            plt.title("ACTIVITY OF TEST AGENTS ON '"+date+"'",fontsize=17)
                            plt.xlabel("Employee No.s ->",fontsize=15)
                            plt.ylabel("Number of patients treated ->",fontsize=15)
                            plt.grid()
                            plt.show()
                        elif(lg=='2'):
                            print("                  Test Agent Emp.No.")
                            for yd in range(0,qg):
                                rf=str(ag[yd])
                                lh.append(rf)
                                rg="select count('Record_ID') from patients where TA_Emp_No='"+rf+"' and Date=date(curdate())"
                                aw=pd.read_sql(rg,mydb)
                                tw=aw["count('Record_ID')"]
                                br=tw[0]
                                aw.columns=[rf]
                                aw.index=["Patients Treated"]
                                wg.append(br)
                                print(aw)
                                plt.bar(lh,wg,width=0.2,color="red",edgecolor="black")
                            plt.title("ACTIVITY OF TEST AGENTS FOR TODAY",fontsize=17)
                            plt.xlabel("Employee No.s ->",fontsize=15)
                            plt.ylabel("Number of patients treated ->",fontsize=15)
                            plt.grid()
                            plt.show()
                        elif(lg=='3'):
                            print("                  Test Agent Emp.No.")
                            for yd in range(0,qg):
                                rf=str(ag[yd])
                                lh.append(rf)
                                rg="select count('Record_ID') from patients where TA_Emp_No='"+rf+"' and Date between date(curdate()-7) and date(curdate())"
                                aw=pd.read_sql(rg,mydb)
                                tw=aw["count('Record_ID')"]
                                br=tw[0]
                                aw.columns=[rf]
                                aw.index=["Patients Treated"]
                                wg.append(br)
                                print(aw)
                                plt.bar(lh,wg,width=0.2,color="red",edgecolor="black")
                            plt.title('''ACTIVITY OF TEST AGENTS
DURING LAST WEEK''',fontsize=17)
                            plt.xlabel("Employee No.s ->",fontsize=15)
                            plt.ylabel("Number of patients treated ->",fontsize=15)
                            plt.grid()
                            plt.show()
                        elif(lg=='4'):
                            print("                  Test Agent Emp.No.")
                            for yd in range(0,qg):
                                rf=str(ag[yd])
                                lh.append(rf)
                                rg="select count('Record_ID') from patients where TA_Emp_No='"+rf+"' and Month=monthname(curdate())"
                                aw=pd.read_sql(rg,mydb)
                                tw=aw["count('Record_ID')"]
                                br=tw[0]
                                aw.columns=[rf]
                                aw.index=["Patients Treated"]
                                wg.append(br)
                                print(aw)
                                plt.bar(lh,wg,width=0.2,color="red",edgecolor="black")
                            plt.title('''ACTIVITY OF TEST AGENTS
DURING THIS MONTH''',fontsize=17)
                            plt.xlabel("Employee No.s ->",fontsize=15)
                            plt.ylabel("Number of patients treated ->",fontsize=15)
                            plt.grid()
                            plt.show()
                        else:
                            print("INCORRECT OPTION NUMBER !!! :(")

                    elif(mv=='2'):
                        kcg="select distinct(LT_Emp_No) from patients where Unit_Name='"+a_unit_name+"'"
                        kbg=pd.read_sql(kcg,mydb)
                        kag=kbg['LT_Emp_No'].tolist()
                        kqg=len(kag)
                        kwg=[]
                        klh=[]
                        if(lg=='1'):
                            kdate=str(input("ENTER DATE(format:-YYYY-MM-DD): "))
                            print()
                            print("                  Lab Technicians Emp.No.") 
                            for kyd in range(0,kqg):
                                krf=str(kag[kyd])
                                klh.append(krf)
                                krg="select count('Record_ID') from patients where LT_Emp_No='"+krf+"' and Date='"+kdate+"'"
                                kaw=pd.read_sql(krg,mydb)
                                ktw=kaw["count('Record_ID')"]
                                kbr=ktw[0]
                                kaw.columns=[krf]
                                kaw.index=["Patients Treated"]
                                kwg.append(kbr)
                                print(kaw)
                                plt.bar(klh,kwg,width=0.2,color="red",edgecolor="black")
                            plt.title("ACTIVITY OF LAB TECHNICIANS ON '"+kdate+"'",fontsize=17)
                            plt.xlabel("Employee No.s ->",fontsize=15)
                            plt.ylabel("Number of patients treated ->",fontsize=15)
                            plt.grid()
                            plt.show()
                        elif(lg=='2'):
                            print("                  Lab Technicians Emp.No.")
                            for kyd in range(0,kqg):
                                krf=str(kag[kyd])
                                klh.append(krf)
                                krg="select count('Record_ID') from patients where LT_Emp_No='"+krf+"' and Date=date(curdate())"
                                kaw=pd.read_sql(krg,mydb)
                                ktw=kaw["count('Record_ID')"]
                                kbr=ktw[0]
                                kaw.columns=[krf]
                                kaw.index=["Patients Treated"]
                                kwg.append(kbr)
                                print(kaw)
                                plt.bar(klh,kwg,width=0.2,color="red",edgecolor="black")
                            plt.title("ACTIVITY OF LAB TECHNICIANS FOR TODAY",fontsize=17)
                            plt.xlabel("Employee No.s ->",fontsize=15)
                            plt.ylabel("Number of patients treated ->",fontsize=15)
                            plt.grid()
                            plt.show()
                        elif(lg=='3'):
                            print("                  Lab Technicians Emp.No.")
                            for kyd in range(0,kqg):
                                krf=str(kag[kyd])
                                klh.append(krf)
                                krg="select count('Record_ID') from patients where LT_Emp_No='"+krf+"' and Date between date(curdate()-7) and date(curdate())"
                                kaw=pd.read_sql(krg,mydb)
                                ktw=kaw["count('Record_ID')"]
                                kbr=ktw[0]
                                kaw.columns=[krf]
                                kaw.index=["Patients Treated"]
                                kwg.append(kbr)
                                print(kaw)
                                plt.bar(klh,kwg,width=0.2,color="red",edgecolor="black")
                            plt.title('''ACTIVITY OF LAB TECHNICANS
DURING LAST WEEK''',fontsize=17)
                            plt.xlabel("Employee No.s ->",fontsize=15)
                            plt.ylabel("Number of patients treated ->",fontsize=15)
                            plt.grid()
                            plt.show()
                        elif(lg=='4'):
                            print("                  Lab Technicians Emp.No.")
                            for kyd in range(0,kqg):
                                krf=str(kag[kyd])
                                klh.append(krf)
                                krg="select count('Record_ID') from patients where LT_Emp_No='"+krf+"' and Month=monthname(curdate())"
                                kaw=pd.read_sql(krg,mydb)
                                ktw=kaw["count('Record_ID')"]
                                kbr=ktw[0]
                                kaw.columns=[krf]
                                kaw.index=["Patients Treated"]
                                kwg.append(kbr)
                                print(kaw)
                                plt.bar(klh,kwg,width=0.2,color="red",edgecolor="black")
                            plt.title('''ACTIVITY OF LAB TECHNICIANS
DURING THIS MONTH''',fontsize=17)
                            plt.xlabel("Employee No.s ->",fontsize=15)
                            plt.ylabel("Number of patients treated ->",fontsize=15)
                            plt.grid()
                            plt.show()
                        else:
                            print("INCORRECT OPTION NUMBER !!! :(")
                    else:
                        print("INCORRECT OPTION NUMBER !!! :(")
                        
                elif(ou=='6'):
                    print("Which employee would you like to view the details of?")
                    print("1.Test Agent","2.Lab Technicians",sep='\n')
                    print()
                    mpl=input("ENTER OPTION NUMBER: ")
                    ui="select* from admins where Username='"+aname+"'"
                    df_admin_profile=pd.read_sql(ui,mydb)
                    lu=df_admin_profile["Unit_Name"]
                    a_unit_name=str(lu[0])
                    print()
                    if(mpl=='1'):
                        bpg="select Agent_Name,Gender,Mobile_No,Email_ID,TA_Emp_No,Username,State,District,Test_Center from test_agents where Unit_Name='"+a_unit_name+"'"
                        mnf=pd.read_sql(bpg,mydb)
                        print("                                                          TEST AGENTS")
                        print("                                                          ===========")
                        print(mnf)
                    elif(mpl=='2'):
                        bmi="select Agent_Name,Gender,Mobile_No,Email_ID,LT_Emp_No,Username,State,District,Test_Center from lab_technicians where Unit_Name='"+a_unit_name+"'"
                        mif=pd.read_sql(bmi,mydb)
                        print("                                                         LAB TECHNICIANS")
                        print("                                                         ===============")
                        print(mif)
                    else:
                        print("INCORRECT OPTION NUMBER !!! :(")
                            
            elif(ah=='3'):
                print()
                print("What info would you like to edit?")
                print("1.Email ID","2.Mobile No.","3.State & District","4.Change Password","5.Back",sep="\n")
                print()
                an_edit_opt=input("ENTER OPTION NUMBER: ")
                print()
                        
                if(an_edit_opt=='1'):
                    an_new_email=str(input("ENTER NEW EMAIL ID: "))
                    an_email_id=an_new_email.lower()
                    if("@" in an_email_id):
                        mycursor.execute("update admins set Email_ID='"+an_email_id+"' where Username='"+aname+"'")
                        mycursor.execute("commit")
                        print()
                        print("YOUR EMAIL ID HAS BEEN UPDATED")
                    else:
                        print()
                        print("YOUR EMAIL ID CANNOT BE ACCEPTED !!! :(","TRY AGAIN!!!",sep="\n")

                elif(an_edit_opt=='2'):
                    an_new_mobile_no=input("ENTER NEW MOBILE NO.(format:- 0091xxxxxxxxxx): ")
                    print()
                    if(len(an_new_mobile_no)==14):
                        mycursor.execute("update admins set Mobile_No='"+an_new_mobile_no+"' where Username='"+aname+"'")
                        mycursor.execute("commit")
                        print("YOUR MOBILE NO. HAS BEEN UPDATED")

                    else:
                        print("INCORRECT FORMAT OF MOBILE NUMBER !!! :(","TRY AGAIN!!!",sep="\n")
                                     
                elif(an_edit_opt=='3'):
                    INDIA.States_and_Districts_option()
                    mycursor.execute("update admins set State='"+INDIA.States_and_Districts_option.selected_state1+"',District='"+INDIA.States_and_Districts_option.selected_district1+"' where Username='"+aname+"'")
                    mycursor.execute("commit")
                    print("YOUR SELECTED STATE IS ",INDIA.States_and_Districts_option.selected_state1)
                    print("YOUR SELECTED DISTRICT IS ",INDIA.States_and_Districts_option.selected_district1)
                    print()
                    print("YOUR STATE AND DISTRICT HAS BEEN UPDATED")

                elif(an_edit_opt=='4'):
                    an_email=input("ENTER EMAIL ID TO VERIFY: ")
                    an_email=an_email.lower()
                    an_mobile_no=input("ENTER MOBILE NO. TO VERIFY(format:- 0091xxxxxxxxxx): ")
                    print()
                    if(len(an_mobile_no)==14):
                        mycursor.execute("select count('Admin_Name') from admins where Email_ID='"+an_email+"' and Mobile_No='"+an_mobile_no+"' and Username='"+aname+"'")
                        for dk in mycursor:
                            if(dk==(1,)):
                                password_check.Strong_password_checker()
                                mycursor.execute("update admins set Password='"+password_check.Strong_password_checker.clear_check+"' where Email_ID='"+an_email+"' and Mobile_No='"+an_mobile_no+"' and Username='"+aname+"'")
                                mycursor.execute("commit")
                                print()
                                print("YOUR PASSWORD HAS BEEN CHANGED")
        
                            else:
                                print()
                                print("INCORRECT EMAIL ID OR MOBILE NO. !!! :(","TRY AGAIN!!!",sep="\n")
                    else:
                        print()
                        print("INCORRECT EMAIL ID OR MOBILE NO. !!! :(","TRY AGAIN!!!",sep="\n")

            elif(ah=='4'):
                apme=str(input("ENTER YOUR EMPLOYEE NUMBER: "))
                mycursor.execute("select count('Admin_Name') from admins where Username='"+aname+"' and AD_Emp_No='"+apme+"'")
                print()
                for anuh in mycursor:
                    if(anuh==(1,)):
                        print("Profile")
                        print("=======")
                        print("____________________________________________________________","\n")
                        ui="select* from admins where Username='"+aname+"' and AD_Emp_No='"+apme+"'"
                        df_admin_profile=pd.read_sql(ui,mydb)
                        prof=df_admin_profile.to_dict(orient="list")
                        for key,value in prof.items():
                            print(key,":","\t",value)
                    else:
                        print("INCORRECT EMPLOYEE NUMBER !!! :(","TRY AGAIN!!!",sep='\n')
                
            elif(ah=='5'):
                Contact_us.contact_DHR()
                
            elif(ah=='6'):
                quit()

            else:
                print("INCORRECT OPTION NUMBER !!! :(")
