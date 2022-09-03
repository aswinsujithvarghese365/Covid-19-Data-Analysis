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
# if u need to edit the details of the employee, pls contact the system developer

def super_admin():
    mycursor=mydb.cursor()
    mycursor.execute("commit")
    ro=1
    while(ro>0):
        sdaname=str(input("ENTER USERNAME: "))
        sdpassds=getpass.getpass(prompt="ENTER PASSWORD: ")
        mycursor.execute("select count('Admin_Name') from super_admins where Username='"+sdaname+"' and Password='"+sdpassds+"'")
        for vch in mycursor:
            if(vch==(1,)):
                print()
                w0="ACCESS GRANTED"
                print(w0)
                print()
                ro=0
                
            else:
                print()
                print("ACCESS DENIED")
                w0="INVALID USERNAME OR PASSWORD"
                print(w0)
                print()
                    

    if(w0=="ACCESS GRANTED"):
        while True:
            print("____________________________________________________________","\n")
            print("What would you like to do?")
            print("1.Sign up for Admins/Test Agents/Lab Technicians","2.Report Manager","3.Edit Profile","4.Show Profile","5.Contact Us","6.Quit Application",sep="\n")
            print()
            sdah=input("ENTER OPTION NUMBER: ")
            print("____________________________________________________________","\n")

            if(sdah=='1'):
                print("Which one would you like to sign up for?")
                print("1.Admin","2.Test Agent","3.Lab Technician","4.Back",sep='\n')
                print()
                sla=input("ENTER OPTION NUMBER: ")
                print()
                if(sla=='1'):
                    sda_name=input("ENTER NAME OF THE ADMIN: ")
                    sda_name=sda_name.upper()
                    print()
                    print("SELECT ADMIN'S GENDER: ")
                    print("1.Male","2.Female",sep='\n')
                    print()
                    sdlj=""
                    while sdlj not in ['1','2']:
                        sdlj=input("ENTER OPTION NUMBER: ")
                        if(sdlj=='1'):
                            sda_gender="Male"
                        elif(sdlj=='2'):
                            sda_gender="Female"
                        else:
                            print("INCORRECT OPTION NUMBER !!! :(")
                            print()
                    print()                        
                    print("ADMIN'S GENDER IS ",sda_gender)
                    print()
                    sdti=1
                    while(sdti>0):
                        sda_mobile_no=input("ENTER MOBILE NUMBER OF THE ADMIN(format:- 0091xxxxxxxxxx): ")
                        print()
                        if(len(sda_mobile_no)==14):
                            sda_mobile_no=str(sda_mobile_no)
                            sdti=0
                        else:
                            print("INCORRECT FORMAT OF MOBILE NUMBER !!! :(","TRY AGAIN!!!",sep="\n")
                            print()
                    sden=1
                    while(sden>0):
                        sda_email=input("ENTER EMAIL ID OF THE ADMIN: ")
                        print()
                        if("@" in sda_email):
                            sda_email=sda_email.lower()
                            sden=0
                        else:
                            print("EMAIL ID OF THE ADMIN CANNOT BE ACCEPTED !!! :(","TRY AGAIN!!!",sep="\n")
                            print()

                    password_check.Username_checker()
                    print()
                    password_check.Strong_password_checker()
                    print()
                    INDIA.States_and_Districts_option()
                    print("SELECTED STATE IS ",INDIA.States_and_Districts_option.selected_state1)
                    print("SELECTED DISTRICT IS ",INDIA.States_and_Districts_option.selected_district1)
                    print()
                    print("SELECT TEST CENTER OF THE ADMIN: ")
                    print("1.Government Hospital","2.Private Healthcare Center",sep='\n')
                    print()
                    sdmh=""
                    while sdmh not in ['1','2']:
                        sdmh=input("ENTER OPTION NUMBER: ")
                        if(sdmh=='1'):
                            sda_test_center="Government Hospital"
                        elif(sdmh=='2'):
                            sda_test_center="Private Healthcare Center"
                        else:
                            print("INCORRECT OPTION NUMBER !!! :(")
                            print()
                    print()
                    print("SELECTED TEST CENTER OF THE ADMIN IS ",sda_test_center)
                    print()
                    sda_unit_name=str(input("ENTER UNIT NAME OF THE ADMIN: "))
                    print()
                    sdmc="select max(AD_Emp_No) from admins"
                    sdmax_temp=pd.read_sql(sdmc,mydb)
                    sdmg=sdmax_temp["max(AD_Emp_No)"]
                    sda_ta_emp=str(sdmg[0]+1)
                    print("EMPLOYEE NUMBER OF THE ADMIN IS ",sda_ta_emp)
                    print()
                    mycursor.execute("insert into admins values('"+sda_name+"','"+sda_gender+"','"+sda_mobile_no+"','"+sda_email+"','"+sda_ta_emp+"','"+password_check.Username_checker.clear_uname_check+"','"+password_check.Strong_password_checker.clear_check+"','"+INDIA.States_and_Districts_option.selected_state1+"','"+INDIA.States_and_Districts_option.selected_district1+"','"+sda_test_center+"','"+sda_unit_name+"')")
                    mycursor.execute("commit")
                    print("SIGN UP FOR ADMIN HAS BEEN COMPLETED SUCCESSFULLY !!! :)")
                    
                elif(sla=='2'):
                    seta_name=input("ENTER NAME OF THE TEST AGENT: ")
                    seta_name=seta_name.upper()
                    print()
                    print("SELECT TEST AGENT'S GENDER: ")
                    print("1.Male","2.Female",sep='\n')
                    print()
                    slj=""
                    while slj not in ['1','2']:
                        slj=input("ENTER OPTION NUMBER: ")
                        if(slj=='1'):
                            seta_gender="Male"
                        elif(slj=='2'):
                            seta_gender="Female"
                        else:
                            print("INCORRECT OPTION NUMBER !!! :(")
                            print()
                    print()                        
                    print("TEST AGENT'S GENDER IS ",seta_gender)
                    print()
                    sti=1
                    while(sti>0):
                        seta_mobile_no=input("ENTER MOBILE NUMBER OF THE TEST AGENT(format:- 0091xxxxxxxxxx): ")
                        print()
                        if(len(seta_mobile_no)==14):
                            seta_mobile_no=str(seta_mobile_no)
                            sti=0
                        else:
                            print("INCORRECT FORMAT OF MOBILE NUMBER !!! :(","TRY AGAIN!!!",sep="\n")
                            print()
                    sen=1
                    while(sen>0):
                        seta_email=input("ENTER EMAIL ID OF THE TEST AGENT: ")
                        print()
                        if("@" in seta_email):
                            seta_email=seta_email.lower()
                            sen=0
                        else:
                            print("EMAIL ID OF THE TEST AGENT CANNOT BE ACCEPTED !!! :(","TRY AGAIN!!!",sep="\n")
                            print()

                    password_check.Username_checker()
                    print()
                    password_check.Strong_password_checker()
                    print()
                    INDIA.States_and_Districts_option()
                    print("SELECTED STATE IS ",INDIA.States_and_Districts_option.selected_state1)
                    print("SELECTED DISTRICT IS ",INDIA.States_and_Districts_option.selected_district1)
                    print()
                    print("SELECT TEST CENTER OF THE TEST AGENT: ")
                    print("1.Government Hospital","2.Private Healthcare Center","3.Mobile Unit",sep='\n')
                    print()
                    smh=""
                    while smh not in ['1','2','3']:
                        smh=input("ENTER OPTION NUMBER: ")
                        if(smh=='1'):
                            seta_test_center="Government Hospital"
                        elif(smh=='2'):
                            seta_test_center="Private Healthcare Center"
                        elif(smh=='3'):
                            seta_test_center="Mobile Unit"
                        else:
                            print("INCORRECT OPTION NUMBER !!! :(")
                            print()
                    print()
                    print("SELECTED TEST CENTER OF THE TEST AGENT IS ",seta_test_center)
                    print()
                    seta_unit_name=str(input("ENTER UNIT NAME OF THE TEST AGENT: "))
                    print()
                    smc="select max(TA_Emp_No) from test_agents"
                    smax_temp=pd.read_sql(smc,mydb)
                    smg=smax_temp["max(TA_Emp_No)"]
                    seta_ta_emp=str(smg[0]+1)
                    print("EMPLOYEE NUMBER OF THE TEST AGENT IS ",seta_ta_emp)
                    print()
                    mycursor.execute("insert into test_agents values('"+seta_name+"','"+seta_gender+"','"+seta_mobile_no+"','"+seta_email+"','"+seta_ta_emp+"','"+password_check.Username_checker.clear_uname_check+"','"+password_check.Strong_password_checker.clear_check+"','"+INDIA.States_and_Districts_option.selected_state1+"','"+INDIA.States_and_Districts_option.selected_district1+"','"+seta_test_center+"','"+seta_unit_name+"')")
                    mycursor.execute("commit")
                    print("SIGN UP FOR TEST AGENT HAS BEEN COMPLETED SUCCESSFULLY !!! :)")
                        
                elif(sla=='3'):
                    selt_name=input("ENTER NAME OF THE LAB TECHNICIAN: ")
                    selt_name=selt_name.upper()
                    print()
                    print("SELECT LAB TECHNICIAN'S GENDER: ")
                    print("1.Male","2.Female",sep='\n')
                    print()
                    sij=""
                    while sij not in ['1','2']:
                        sij=input("ENTER OPTION NUMBER: ")
                        if(sij=='1'):
                            selt_gender="Male"
                        elif(sij=='2'):
                            selt_gender="Female"
                        else:
                            print("INCORRECT OPTION NUMBER !!! :(")
                            print()
                    print()                
                    print("LAB TECHNICIAN'S GENDER IS ",selt_gender)
                    print()
                    shi=1
                    while(shi>0):
                        selt_mobile_no=input("ENTER MOBILE NUMBER OF THE LAB TECHNICIAN(format:- 0091xxxxxxxxxx): ")
                        print()
                        if(len(selt_mobile_no)==14):
                            selt_mobile_no=str(selt_mobile_no)
                            shi=0
                        else:
                            print("INCORRECT FORMAT OF MOBILE NUMBER !!! :(","TRY AGAIN!!!",sep="\n")
                            print()
                    sefg=1
                    while(sefg>0):
                        selt_email=input("ENTER EMAIL ID OF THE LAB TECHNICIAN: ")
                        print()
                        if("@" in selt_email):
                            selt_email=selt_email.lower()
                            sefg=0
                        else:
                            print("EMAIL ID OF THE LAB TECHNICIAN CANNOT BE ACCEPTED !!! :(","TRY AGAIN!!!",sep="\n")
                            print()

                    password_check.Username_checker()
                    print()
                    password_check.Strong_password_checker()
                    print()
                    INDIA.States_and_Districts_option()
                    print("SELECTED STATE IS ",INDIA.States_and_Districts_option.selected_state1)
                    print("SELECTED DISTRICT IS ",INDIA.States_and_Districts_option.selected_district1)
                    print()
                    print("SELECT TEST CENTER OF THE LAB TECHNICIAN: ")
                    print("1.Government Hospital","2.Private Healthcare Center","3.Mobile Unit",sep='\n')
                    print()
                    skh=""
                    while skh not in ['1','2','3']:
                        skh=input("ENTER OPTION NUMBER: ")
                        if(skh=='1'):
                            selt_test_center="Government Hospital"
                        elif(skh=='2'):
                            selt_test_center="Private Healthcare Center"
                        elif(skh=='3'):
                            selt_test_center="Mobile Unit"
                        else:
                            print("INCORRECT OPTION NUMBER !!! :(")
                            print()
                    print()
                    print("SELECTED TEST CENTER OF THE LAB TECHNICIAN IS ",selt_test_center)
                    print()
                    
                    selt_unit_name=str(input("ENTER UNIT NAME OF THE LAB TECHNICIAN: "))
                    print()
                    skm="select max(LT_Emp_No) from lab_technicians"
                    smax_lemp=pd.read_sql(skm,mydb)
                    skg=smax_lemp["max(LT_Emp_No)"]
                    selt_lt_emp=str(skg[0]+1)
                    print("EMPLOYEE NUMBER OF THE LAB TECHNICIAN IS ",selt_lt_emp)
                    print()
                    mycursor.execute("insert into lab_technicians values('"+selt_name+"','"+selt_gender+"','"+selt_mobile_no+"','"+selt_email+"','"+selt_lt_emp+"','"+password_check.Username_checker.clear_uname_check+"','"+password_check.Strong_password_checker.clear_check+"','"+INDIA.States_and_Districts_option.selected_state1+"','"+INDIA.States_and_Districts_option.selected_district1+"','"+selt_test_center+"','"+selt_unit_name+"')")
                    mycursor.execute("commit")
                    print("SIGN UP FOR LAB TECHNICIAN HAS BEEN COMPLETED SUCCESSFULLY !!! :)")
                    

            elif(sdah=='2'):
                print("How would you like to view the report of the patient?")
                print("1.View report of a particular patient","2.View reports of all the patients","3.View number of positive/negative cases","4.View number of positive/negative cases of a specific date","5.View report of patients by sorting","6.View details of the employees","7.Back",sep='\n')
                print()
                sdou=input("ENTER OPTION NUMBER: ")
                print()
                if(sdou=='1'):
                    print("VIEW REPORT OF THE PATIENT BY:")
                    print("1.Medical record serial number","2.Mobile number of the patient",sep='\n')
                    print()
                    sdkl=input("ENTER OPTION NUMBER: ")
                    print()
                    if(sdkl=='1'):
                        sdmb=input("ENTER MEDICAL RECORD SERIAL NUMBER OF THE PATIENT: ")
                        #sdmb=str(sdmb[:-1])
                        print()
                        mycursor.execute("select count('Record_ID') from patients where Record_ID='"+sdmb+"'")
                        for sdd in mycursor:
                            if(sdd==(1,)):
                                sdh1="select* from patients where Record_ID='"+sdmb+"'"
                                sdp_view_result=pd.read_sql(sdh1,mydb)
                                sdp_view_result=sdp_view_result.drop("Month",axis=1)
                                print(sdp_view_result)

                            else:
                                print("INCORRECT MEDICAL RECORD SERIAL NUMBER !!! :(","TRY AGAIN!!!",sep='\n')
                            
                    elif(sdkl=='2'):
                        sdmf=input("ENTER MOBILE NO. OF THE PATIENT(format:- 0091xxxxxxxxxx): ")
                        print()
                        mycursor.execute("select count('Name') from patients where Mobile_No='"+sdmf+"'")
                        for soo in mycursor:
                            if(soo==(1,)):
                                if(len(sdmf)==14):
                                    sdg1="select* from patients where Mobile_No='"+sdmf+"'"
                                    sdp_view_mresult=pd.read_sql(sdg1,mydb)
                                    sdp_view_mresult=sdp_view_mresult.drop("Month",axis=1)
                                    print(sdp_view_mresult)
                                else:
                                    print("INCORRECT FORMAT OF MOBILE NUMBER !!! :(","TRY AGAIN!!!",sep="\n")

                            else:
                                print("INCORRECT MOBILE NUMBER !!! :(","TRY AGAIN!!!",sep='\n')

                    else:
                        print("INCORRECT OPTION NUMBER !!! :(")
                    
                elif(sdou=='2'):
                    sdoy="select* from patients"
                    sd_entire_results=pd.read_sql(sdoy,mydb)
                    sd_entire_results=sd_entire_results.drop("Month",axis=1)
                    print(sd_entire_results)
                    print()

                elif(sdou=='3'):
                    sdoj="select* from patients where Result='Positive'"
                    sdoc="select* from patients where Result='Negative'"
                    sdoe=pd.read_sql(sdoj,mydb)
                    sdow=pd.read_sql(sdoc,mydb)
                    sdoe=sdoe.drop("Month",axis=1)
                    sdow=sdow.drop("Month",axis=1)
                    sdp_positive=sdoe["Record_ID"].count()
                    sdp_negative=sdow["Record_ID"].count()
                    print('\t',"                                                               POSITIVE RESULTS")
                    print('\t',"                                                               ----------------")
                    print(sdoe,'\n')
                    print('\t',"                                                               NEGATIVE RESULTS")
                    print('\t',"                                                               ----------------")
                    print(sdow,'\n')
                    sdno_of_pcases=[sdp_positive]
                    sdno_of_ncases=[sdp_negative]
                    width=0.3
                    plt.bar("Positive",sdno_of_pcases,width,color="orange",edgecolor="black")
                    plt.bar("Negative",sdno_of_ncases,width,color="blue",edgecolor="black")
                    plt.title("REPORT",fontsize=20)
                    plt.xlabel("Results ->",fontsize=15)
                    plt.ylabel("Number of Cases ->",fontsize=15)
                    plt.grid()
                    plt.show()

                elif(sdou=='4'):
                    spn_date=str(input("ENTER DATE(format:-YYYY-MM-DD): "))
                    print()
                    pn_sdoj="select* from patients where Result='Positive' and Date='"+spn_date+"'"
                    pn_sdoc="select* from patients where Result='Negative' and Date='"+spn_date+"'"
                    pn_sdoe=pd.read_sql(pn_sdoj,mydb)
                    pn_sdow=pd.read_sql(pn_sdoc,mydb)
                    pn_sdoe=pn_sdoe.drop("Month",axis=1)
                    pn_sdoe=pn_sdoe.drop("Date",axis=1)
                    pn_sdow=pn_sdow.drop("Month",axis=1)
                    pn_sdow=pn_sdow.drop("Date",axis=1)
                    pn_sdp_positive=pn_sdoe["Record_ID"].count()
                    pn_sdp_negative=pn_sdow["Record_ID"].count()
                    print('\t',"                                                               POSITIVE RESULTS")
                    print('\t',"                                                               ----------------")
                    print(pn_sdoe,'\n')
                    print('\t',"                                                               NEGATIVE RESULTS")
                    print('\t',"                                                               ----------------")
                    print(pn_sdow,'\n')
                    sdno_of_pcases=[pn_sdp_positive]
                    sdno_of_ncases=[pn_sdp_negative]
                    width=0.3
                    plt.bar("Positive",sdno_of_pcases,width,color="orange",edgecolor="black")
                    plt.bar("Negative",sdno_of_ncases,width,color="blue",edgecolor="black")
                    plt.title("REPORT",fontsize=20)
                    plt.xlabel("Results ->",fontsize=15)
                    plt.ylabel("Number of Cases ->",fontsize=15)
                    plt.grid()
                    plt.show()

                elif(sdou=='5'):
                    print("How would you like to sort the report?")
                    print("1.Age Group","2.Gender","3.Month","4.State",sep='\n')
                    print()
                    sdmv=input("ENTER OPTION NUMBER: ")
                    print()
                    if(sdmv=='1'):
                        sdcg=["0-1","2-11","12-17","18 and above","65 and above"]
                        sdqg=len(sdcg)
                        sdwg=[]
                        sdlh=[]
                        print("                REPORT")
                        print("                ------")
                        print("                          Age Group")
                        for fyd in range(0,sdqg):
                            sdrf=sdcg[fyd]
                            sdrg="select count('Record_ID') from patients where Result='Positive' and Age_Group='"+sdrf+"'"
                            sdew="select count('Record_ID') from patients where Result='Negative' and Age_Group='"+sdrf+"'"
                            sdaw=pd.read_sql(sdrg,mydb)
                            sdlm=pd.read_sql(sdew,mydb)
                            sdtw=sdaw["count('Record_ID')"]
                            sdgt=sdlm["count('Record_ID')"]
                            sdbr=sdtw[0]
                            sdgk=sdgt[0]
                            sdaw.columns=[sdrf]
                            sdlm.columns=["   "]
                            sdaw.index=["No.of Patients(Positive):-"]
                            sdlm.index=["No.of Patients(Negative):-"]
                            sdwg.append(sdbr)
                            sdlh.append(sdgk)
                            print(sdaw)
                            print(sdlm,'\n')                        
                        barWidth = 0.3
                        positive=sdwg
                        negative=sdlh
                        p1=np.arange(len(positive))
                        p2=[x+barWidth for x in p1]
                        plt.bar(p1,positive,color='orange',width=barWidth,edgecolor='black',label='Positive')
                        plt.bar(p2,negative,color='blue',width=barWidth,edgecolor='black',label='Negative')
                        plt.xlabel('Age Groups ->',fontsize=15)
                        plt.ylabel("Number of patients ->",fontsize=15)
                        plt.xticks([p+barWidth for p in range(len(positive))],sdcg)#xticks=(location,label)
                                                                                   #xticks is used for giving location and labels together
                        plt.title('''COVID DATA ANALYSIS
(according to Age Groups)''',fontsize=17)
                        plt.grid()
                        plt.legend()
                        plt.show()
                        
                    elif(sdmv=='2'):
                        dcg=["Male","Female"]
                        dqg=len(dcg)
                        dwg=[]
                        dlh=[]
                        print("                REPORT")
                        print("                ------")
                        print("                          Gender")
                        for byd in range(0,dqg):
                            drf=dcg[byd]
                            drg="select count('Record_ID') from patients where Result='Positive' and Gender='"+drf+"'"
                            dew="select count('Record_ID') from patients where Result='Negative' and Gender='"+drf+"'"
                            daw=pd.read_sql(drg,mydb)
                            dlm=pd.read_sql(dew,mydb)
                            dtw=daw["count('Record_ID')"]
                            dgt=dlm["count('Record_ID')"]
                            dbr=dtw[0]
                            dgk=dgt[0]
                            daw.columns=[drf]
                            dlm.columns=["   "]
                            daw.index=["No.of Patients(Positive):-"]
                            dlm.index=["No.of Patients(Negative):-"]
                            dwg.append(dbr)
                            dlh.append(dgk)
                            print(daw)
                            print(dlm,'\n')                
                        barWidth = 0.3
                        g_positive=dwg
                        g_negative=dlh
                        v1=np.arange(len(g_positive))
                        v2=[x+barWidth for x in v1]
                        plt.bar(v1,g_positive,color='orange',width=barWidth,edgecolor='black',label='Positive')
                        plt.bar(v2,g_negative,color='blue',width=barWidth,edgecolor='black',label='Negative')
                        plt.xlabel('Gender ->',fontsize=15)
                        plt.ylabel("Number of patients ->",fontsize=15)
                        plt.xticks([v+barWidth for v in range(len(g_positive))],dcg)#xticks=(location,label)
                        plt.title('''COVID DATA ANALYSIS
(according to Gender)''',fontsize=17)
                        plt.grid()
                        plt.legend()
                        plt.show()

                    elif(sdmv=='3'):
                        mdcg= ['October','November','December','January','February','March',
                               'April','May','June','July','August','September'] 
                        mdqg=len(mdcg)
                        mdwg=[]
                        mdlh=[]
                        print("                REPORT")
                        print("                ------")
                        print("                            Months")
                        for myd in range(0,mdqg):
                            mdrf=mdcg[myd]
                            mdrg="select count('Record_ID') from patients where Result='Positive' and Month='"+mdrf+"'"
                            mdew="select count('Record_ID') from patients where Result='Negative' and Month='"+mdrf+"'"
                            mdaw=pd.read_sql(mdrg,mydb)
                            mdlm=pd.read_sql(mdew,mydb)
                            mdtw=mdaw["count('Record_ID')"]
                            mdgt=mdlm["count('Record_ID')"]
                            mdbr=mdtw[0]
                            mdgk=mdgt[0]
                            mdaw.columns=[mdrf]
                            mdlm.columns=["   "]
                            mdaw.index=["No.of Patients(Positive):-"]
                            mdlm.index=["No.of Patients(Negative):-"]
                            mdwg.append(mdbr)
                            mdlh.append(mdgk)
                            print(mdaw)
                            print(mdlm,'\n')    
                        barWidth = 0.3
                        m_positive=mdwg
                        m_negative=mdlh
                        f1=np.arange(len(m_positive))
                        f2=[x+barWidth for x in f1]
                        plt.bar(f1,m_positive,color='orange',width=barWidth,edgecolor='black',label='Positive')
                        plt.bar(f2,m_negative,color='blue',width=barWidth,edgecolor='black',label='Negative')
                        plt.plot(f1,m_positive,color='red',label="Positive",marker="*")
                        plt.plot(f2,m_negative,color='green',label="Negative",marker="*")
                        plt.xlabel('Months ->',fontsize=15)
                        plt.ylabel("Number of patients ->",fontsize=15)
                        plt.xticks([f+barWidth for f in range(len(m_positive))],mdcg)#xticks=(location,label)
                        plt.title('''COVID DATA ANALYSIS
(according to Months)''',fontsize=17)
                        plt.grid()
                        plt.legend()
                        plt.show()

                    elif(sdmv=='4'):
                        iscg= ["Andaman & Nicobar Island","Andhra Pradesh","Arunachal Pradesh",
                               "Assam","Bihar","Chandigarh","Chhattisgarh",
                               "Dadra and Nagar Haveli and Daman and Diu","Delhi","Goa","Gujarat",
                               "Haryana","Himachal Pradesh","Jammu & Kashmir","Jharkhand",
                               "Karnataka","Kerala","Ladakh","Lakshadweep","Madhya Pradesh",
                                "Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha",
                               "Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana",
                               "Tripura","Uttar Pradesh","Uttarakhand","West Bengal"] 
                        isqg=len(iscg)
                        iswg=[]
                        islh=[]
                        print("                REPORT")
                        print("                ------")
                        print("                            Months")
                        for iyd in range(0,isqg):
                            isrf=iscg[iyd]
                            isrg="select count('Record_ID') from patients where Result='Positive' and State='"+isrf+"'"
                            isew="select count('Record_ID') from patients where Result='Negative' and State='"+isrf+"'"
                            isaw=pd.read_sql(isrg,mydb)
                            islm=pd.read_sql(isew,mydb)
                            istw=isaw["count('Record_ID')"]
                            isgt=islm["count('Record_ID')"]
                            isbr=istw[0]
                            isgk=isgt[0]
                            isaw.columns=[isrf]
                            islm.columns=["   "]
                            isaw.index=["No.of Patients(Positive):-"]
                            islm.index=["No.of Patients(Negative):-"]
                            iswg.append(isbr)
                            islh.append(isgk)
                            print(isaw)
                            print(islm,'\n')                                
                        barWidth=0.3 
                        s_positive=iswg
                        s_negative=islh
                        y1=np.arange(len(s_positive))
                        y2=y1+0.8
                        plt.barh(y1,s_positive,color='orange',edgecolor='black',label='Positive')
                        plt.barh(y2,s_negative,color='blue',edgecolor='black',label='Negative')
                        plt.xlabel('Number of patients ->',fontsize=15)
                        plt.ylabel("States ->",fontsize=15)
                        plt.yticks([y+barWidth for y in range(len(s_positive))],iscg)#yticks=(location,label)
                        plt.title('''COVID DATA ANALYSIS
(according to States)''',fontsize=17)
                        plt.grid()
                        plt.legend()
                        plt.show()

                    else:
                        print("INCORRECT OPTION NUMBER !!! :(")

                elif(sdou=='6'):
                    print("Which employee would you like to view the details of?")
                    print("1.Admin","2.Test Agent","3.Lab Technician",sep='\n')
                    print()
                    smpl=input("ENTER OPTION NUMBER: ")
                    print()
                    if(smpl=='1'):
                        sapg="select Admin_Name,Gender,Mobile_No,Email_ID,AD_Emp_No,Username,State,District,Test_Center,Unit_Name from admins"
                        strf=pd.read_sql(sapg,mydb)
                        print("                                                                             ADMINS")
                        print("                                                                             ======")
                        print(strf)
                    elif(smpl=='2'):
                        sbpg="select Agent_Name,Gender,Mobile_No,Email_ID,TA_Emp_No,Username,State,District,Test_Center,Unit_Name from test_agents"
                        smnf=pd.read_sql(sbpg,mydb)
                        print("                                                                          TEST AGENTS")
                        print("                                                                          ===========")
                        print(smnf)
                    elif(smpl=='3'):
                        sbmi="select Agent_Name,Gender,Mobile_No,Email_ID,LT_Emp_No,Username,State,District,Test_Center,Unit_Name from lab_technicians"
                        smif=pd.read_sql(sbmi,mydb)
                        print("                                                                         LAB TECHNICIANS")
                        print("                                                                         ===============")
                        print(smif)
                    else:
                        print("INCORRECT OPTION NUMBER !!! :(")
                                    
            elif(sdah=='3'):
                print()
                print("What info would you like to edit?")
                print("1.Email ID","2.Mobile No.","3.State & District","4.Change Password","5.Back",sep="\n")
                print()
                sd_edit_opt=input("ENTER OPTION NUMBER: ")
                print()
                            
                if(sd_edit_opt=='1'):
                    sd_new_email=str(input("ENTER NEW EMAIL ID: "))
                    sd_email_id=sd_new_email.lower()
                    if("@" in sd_email_id):
                        mycursor.execute("update super_admins set Email_ID='"+sd_email_id+"' where Username='"+sdaname+"'")
                        mycursor.execute("commit")
                        print()
                        print("YOUR EMAIL ID HAS BEEN UPDATED")
                    else:
                        print()
                        print("YOUR EMAIL ID CANNOT BE ACCEPTED !!! :(","TRY AGAIN!!!",sep="\n")

                elif(sd_edit_opt=='2'):
                    sd_new_mobile_no=input("ENTER NEW MOBILE NO.(format:- 0091xxxxxxxxxx): ")
                    print()
                    if(len(sd_new_mobile_no)==14):
                        mycursor.execute("update super_admins set Mobile_No='"+sd_new_mobile_no+"' where Username='"+sdaname+"'")
                        mycursor.execute("commit")
                        print("YOUR MOBILE NO. HAS BEEN UPDATED")

                    else:
                        print("INCORRECT FORMAT OF MOBILE NUMBER !!! :(","TRY AGAIN!!!",sep="\n")
                                     
                elif(sd_edit_opt=='3'):
                    INDIA.States_and_Districts_option()
                    mycursor.execute("update super_admins set State='"+INDIA.States_and_Districts_option.selected_state1+"',District='"+INDIA.States_and_Districts_option.selected_district1+"' where Username='"+sdaname+"'")
                    mycursor.execute("commit")
                    print("YOUR SELECTED STATE IS ",INDIA.States_and_Districts_option.selected_state1)
                    print("YOUR SELECTED DISTRICT IS ",INDIA.States_and_Districts_option.selected_district1)
                    print()
                    print("YOUR STATE AND DISTRICT HAS BEEN UPDATED")

                elif(sd_edit_opt=='4'):
                    sd_email=input("ENTER EMAIL ID TO VERIFY: ")
                    sd_email=sd_email.lower()
                    sd_mobile_no=input("ENTER MOBILE NO. TO VERIFY(format:- 0091xxxxxxxxxx): ")
                    print()
                    if(len(sd_mobile_no)==14):
                        mycursor.execute("select count('Admin_Name') from super_admins where Email_ID='"+sd_email+"' and Mobile_No='"+sd_mobile_no+"' and Username='"+sdaname+"'")
                        for sdk in mycursor:
                            if(sdk==(1,)):
                                password_check.Strong_password_checker()
                                mycursor.execute("update super_admins set Password='"+password_check.Strong_password_checker.clear_check+"' where Email_ID='"+sd_email+"' and Mobile_No='"+sd_mobile_no+"' and Username='"+sdaname+"'")
                                mycursor.execute("commit")
                                print()
                                print("YOUR PASSWORD HAS BEEN CHANGED")
    
                            else:
                                print()
                                print("INCORRECT EMAIL ID OR MOBILE NO. !!! :(","TRY AGAIN!!!",sep="\n")
                    else:
                        print()
                        print("INCORRECT EMAIL ID OR MOBILE NO. !!! :(","TRY AGAIN!!!",sep="\n")

            elif(sdah=='4'):
                spme=str(input("ENTER YOUR EMPLOYEE NUMBER: "))
                mycursor.execute("select count('Admin_Name') from super_admins where Username='"+sdaname+"' and SA_Emp_No='"+spme+"'")
                print()
                for snuh in mycursor:
                    if(snuh==(1,)):
                        print("Profile")
                        print("=======")
                        print("____________________________________________________________","\n")
                        sdui="select* from super_admins where Username='"+sdaname+"' and SA_Emp_No='"+spme+"'"
                        df_sadmin_profile=pd.read_sql(sdui,mydb)
                        sd_profile=df_sadmin_profile.to_dict(orient="list")
                        for key,value in sd_profile.items():
                            print(key,":","\t",value)
                    else:
                        print("INCORRECT EMPLOYEE NUMBER !!! :(","TRY AGAIN!!!",sep='\n')
                
            elif(sdah=='5'):
                Contact_us.contact_DHR()
                
            elif(sdah=='6'):
                quit()
                    
            else:
                print("INCORRECT OPTION NUMBER !!! :(")
                    
