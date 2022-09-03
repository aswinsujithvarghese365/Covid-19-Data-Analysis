# States
def States_and_Districts_option():
    import pandas as pd
    
    states={"Option No.":['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17',
                          '18','19','20','21','22','23','24','25','26','27','28','29','30','31','32',
                          '33','34','35','36'],
            "States":["Andaman & Nicobar Island","Andhra Pradesh","Arunachal Pradesh",
                      "Assam","Bihar","Chandigarh","Chhattisgarh",
                      "Dadra and Nagar Haveli and Daman and Diu","Delhi","Goa","Gujarat",
                      "Haryana","Himachal Pradesh","Jammu & Kashmir","Jharkhand",
                      "Karnataka","Kerala","Ladakh","Lakshadweep","Madhya Pradesh",
                      "Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha",
                      "Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana",
                      "Tripura","Uttar Pradesh","Uttarakhand","West Bengal"]}
    opt_states=pd.DataFrame(states,columns=["States","Option No."])
    opt_states.set_index("Option No.",inplace=True)
    print(opt_states)
    print()

    opt_states_no=""
    while opt_states_no not in states["Option No."]:
        opt_states_no=input("ENTER OPTION NUMBER: ")
        if opt_states_no not in states["Option No."]:
            print("INCORRECT OPTION NUMBER !!! :(")
            print()

    print()
    opt_states_no=int(opt_states_no)
    HJ=opt_states_no-1
    st=opt_states.iloc[HJ]
    selected_state=st["States"]# st is a dataframe. selecting "States" column from st.
    print()
    print(selected_state,"----------------------------------------------",sep="\n")

    if(selected_state=="Andaman & Nicobar Island"):
        districts=pd.read_csv('C:\Aswin\Python Assignments\COVID-19 Data Analysis\Districts\Andaman & Nicobar.csv')
        districts.set_index("Option No.",inplace=True)
        print(districts)
        print()
        opt_districts_no=int(input("ENTER OPTION NUMBER: "))
        NJ=opt_districts_no-1
        dt=districts.iloc[NJ]
        selected_district=dt["Districts"]# dt is a dataframe. selecting "Districts" column from dt.
        print()

    elif(selected_state=="Andhra Pradesh"):
        districts=pd.read_csv('C:\Aswin\Python Assignments\COVID-19 Data Analysis\Districts\Andhra Pradesh.csv')
        districts.set_index("Option No.",inplace=True)
        print(districts)
        print()
        opt_districts_no=int(input("ENTER OPTION NUMBER: "))
        NJ=opt_districts_no-1
        dt=districts.iloc[NJ]
        selected_district=dt["Districts"]# dt is a dataframe. selecting "Districts" column from dt.
        print()

    elif(selected_state=="Arunachal Pradesh"):
        districts=pd.read_csv('C:\Aswin\Python Assignments\COVID-19 Data Analysis\Districts\Arunachal Pradesh.csv')
        districts.set_index("Option No.",inplace=True)
        print(districts)
        print()
        opt_districts_no=int(input("ENTER OPTION NUMBER: "))
        NJ=opt_districts_no-1
        dt=districts.iloc[NJ]
        selected_district=dt["Districts"]# dt is a dataframe. selecting "Districts" column from dt.
        print()

    elif(selected_state=="Assam"):
        districts=pd.read_csv('C:\Aswin\Python Assignments\COVID-19 Data Analysis\Districts\Assam.csv')
        districts.set_index("Option No.",inplace=True)
        print(districts)
        print()
        opt_districts_no=int(input("ENTER OPTION NUMBER: "))
        NJ=opt_districts_no-1
        dt=districts.iloc[NJ]
        selected_district=dt["Districts"]# dt is a dataframe. selecting "Districts" column from dt.
        print()

    elif(selected_state=="Bihar"):
        districts=pd.read_csv('C:\Aswin\Python Assignments\COVID-19 Data Analysis\Districts\Bihar.csv')
        districts.set_index("Option No.",inplace=True)
        print(districts)
        print()
        opt_districts_no=int(input("ENTER OPTION NUMBER: "))
        NJ=opt_districts_no-1
        dt=districts.iloc[NJ]
        selected_district=dt["Districts"]# dt is a dataframe. selecting "Districts" column from dt.
        print()

    elif(selected_state=="Chandigarh"):
        districts="Chandigarh"
        print(districts)
        print()
        selected_district="Chandigarh"
        print()

    elif(selected_state=="Chhattisgarh"):
        districts=pd.read_csv('C:\Aswin\Python Assignments\COVID-19 Data Analysis\Districts\Chhattisgarh.csv')
        districts.set_index("Option No.",inplace=True)
        print(districts)
        print()
        opt_districts_no=int(input("ENTER OPTION NUMBER: "))
        NJ=opt_districts_no-1
        dt=districts.iloc[NJ]
        selected_district=dt["Districts"]# dt is a dataframe. selecting "Districts" column from dt.
        print()

    elif(selected_state=="Dadra and Nagar Haveli and Daman and Diu"):
        districts="Dadra and Nagar Haveli and Daman and Diu"
        print(districts)
        print()
        selected_district="Dadra and Nagar Haveli and Daman and Diu"

    elif(selected_state=="Delhi"):
        districts=pd.read_csv('C:\Aswin\Python Assignments\COVID-19 Data Analysis\Districts\Delhi.csv')
        districts.set_index("Option No.",inplace=True)
        print(districts)
        print()
        opt_districts_no=int(input("ENTER OPTION NUMBER: "))
        NJ=opt_districts_no-1
        dt=districts.iloc[NJ]
        selected_district=dt["Districts"]# dt is a dataframe. selecting "Districts" column from dt.
        print()

    elif(selected_state=="Goa"):
        districts=pd.read_csv('C:\Aswin\Python Assignments\COVID-19 Data Analysis\Districts\Goa.csv')
        districts.set_index("Option No.",inplace=True)
        print(districts)
        print()
        opt_districts_no=int(input("ENTER OPTION NUMBER: "))
        NJ=opt_districts_no-1
        dt=districts.iloc[NJ]
        selected_district=dt["Districts"]# dt is a dataframe. selecting "Districts" column from dt.
        print()

    elif(selected_state=="Gujarat"):
        districts=pd.read_csv('C:\Aswin\Python Assignments\COVID-19 Data Analysis\Districts\Gujarat.csv')
        districts.set_index("Option No.",inplace=True)
        print(districts)
        print()
        opt_districts_no=int(input("ENTER OPTION NUMBER: "))
        NJ=opt_districts_no-1
        dt=districts.iloc[NJ]
        selected_district=dt["Districts"]# dt is a dataframe. selecting "Districts" column from dt.
        print()

    elif(selected_state=="Haryana"):
        districts=pd.read_csv('C:\Aswin\Python Assignments\COVID-19 Data Analysis\Districts\Haryana.csv')
        districts.set_index("Option No.",inplace=True)
        print(districts)
        print()
        opt_districts_no=int(input("ENTER OPTION NUMBER: "))
        NJ=opt_districts_no-1
        dt=districts.iloc[NJ]
        selected_district=dt["Districts"]# dt is a dataframe. selecting "Districts" column from dt.
        print()

    elif(selected_state=="Himachal Pradesh"):
        districts=pd.read_csv('C:\Aswin\Python Assignments\COVID-19 Data Analysis\Districts\Himachal Pradesh.csv')
        districts.set_index("Option No.",inplace=True)
        print(districts)
        print()
        opt_districts_no=int(input("ENTER OPTION NUMBER: "))
        NJ=opt_districts_no-1
        dt=districts.iloc[NJ]
        selected_district=dt["Districts"]# dt is a dataframe. selecting "Districts" column from dt.
        print()

    elif(selected_state=="Jammu & Kashmir"):
        districts=pd.read_csv('C:\Aswin\Python Assignments\COVID-19 Data Analysis\Districts\Jammu & Kashmir.csv')
        districts.set_index("Option No.",inplace=True)
        print(districts)
        print()
        opt_districts_no=int(input("ENTER OPTION NUMBER: "))
        NJ=opt_districts_no-1
        dt=districts.iloc[NJ]
        selected_district=dt["Districts"]# dt is a dataframe. selecting "Districts" column from dt.
        print()

    elif(selected_state=="Jharkhand"):
        districts=pd.read_csv('C:\Aswin\Python Assignments\COVID-19 Data Analysis\Districts\Jharkhand.csv')
        districts.set_index("Option No.",inplace=True)
        print(districts)
        print()
        opt_districts_no=int(input("ENTER OPTION NUMBER: "))
        NJ=opt_districts_no-1
        dt=districts.iloc[NJ]
        selected_district=dt["Districts"]# dt is a dataframe. selecting "Districts" column from dt.
        print()

    elif(selected_state=="Karnataka"):
        districts=pd.read_csv('C:\Aswin\Python Assignments\COVID-19 Data Analysis\Districts\Karnataka.csv')
        districts.set_index("Option No.",inplace=True)
        print(districts)
        print()
        opt_districts_no=int(input("ENTER OPTION NUMBER: "))
        NJ=opt_districts_no-1
        dt=districts.iloc[NJ]
        selected_district=dt["Districts"]# dt is a dataframe. selecting "Districts" column from dt.
        print()

    elif(selected_state=="Kerala"):
        districts=pd.read_csv('C:\Aswin\Python Assignments\COVID-19 Data Analysis\Districts\Kerala.csv')
        districts.set_index("Option No.",inplace=True)
        print(districts)
        print()
        opt_districts_no=int(input("ENTER OPTION NUMBER: "))
        NJ=opt_districts_no-1
        dt=districts.iloc[NJ]
        selected_district=dt["Districts"]# dt is a dataframe. selecting "Districts" column from dt.
        print()

    elif(selected_state=="Ladakh"):
        districts="Ladakh"
        print(districts)
        print()
        selected_district="Ladakh"
        print()

    elif(selected_state=="Lakshadweep"):
        districts="Lakshadweep"
        print(districts)
        print()
        selected_district="Lakshadweep"
        print()

    elif(selected_state=="Madhya Pradesh"):
        districts=pd.read_csv('C:\Aswin\Python Assignments\COVID-19 Data Analysis\Districts\Madhya Pradesh.csv')
        districts.set_index("Option No.",inplace=True)
        pd.set_option('display.max_rows',None)#Shows every rows without default dropping of rows by
        print(districts)                      #python during display
        print()
        opt_districts_no=int(input("ENTER OPTION NUMBER: "))
        NJ=opt_districts_no-1
        dt=districts.iloc[NJ]
        selected_district=dt["Districts"]# dt is a dataframe. selecting "Districts" column from dt.
        print()

    elif(selected_state=="Maharashtra"):
        districts=pd.read_csv('C:\Aswin\Python Assignments\COVID-19 Data Analysis\Districts\Maharashtra.csv')
        districts.set_index("Option No.",inplace=True)
        print(districts)
        print()
        opt_districts_no=int(input("ENTER OPTION NUMBER: "))
        NJ=opt_districts_no-1
        dt=districts.iloc[NJ]
        selected_district=dt["Districts"]# dt is a dataframe. selecting "Districts" column from dt.
        print()

    elif(selected_state=="Manipur"):
        districts=pd.read_csv('C:\Aswin\Python Assignments\COVID-19 Data Analysis\Districts\Manipur.csv')
        districts.set_index("Option No.",inplace=True)
        print(districts)
        print()
        opt_districts_no=int(input("ENTER OPTION NUMBER: "))
        NJ=opt_districts_no-1
        dt=districts.iloc[NJ]
        selected_district=dt["Districts"]# dt is a dataframe. selecting "Districts" column from dt.
        print()

    elif(selected_state=="Meghalaya"):
        districts=pd.read_csv('C:\Aswin\Python Assignments\COVID-19 Data Analysis\Districts\Meghalaya.csv')
        districts.set_index("Option No.",inplace=True)
        print(districts)
        print()
        opt_districts_no=int(input("ENTER OPTION NUMBER: "))
        NJ=opt_districts_no-1
        dt=districts.iloc[NJ]
        selected_district=dt["Districts"]# dt is a dataframe. selecting "Districts" column from dt.
        print()

    elif(selected_state=="Mizoram"):
        districts=pd.read_csv('C:\Aswin\Python Assignments\COVID-19 Data Analysis\Districts\Mizoram.csv')
        districts.set_index("Option No.",inplace=True)
        print(districts)
        print()
        opt_districts_no=int(input("ENTER OPTION NUMBER: "))
        NJ=opt_districts_no-1
        dt=districts.iloc[NJ]
        selected_district=dt["Districts"]# dt is a dataframe. selecting "Districts" column from dt.
        print()

    elif(selected_state=="Nagaland"):
        districts=pd.read_csv("C:\Aswin\Python Assignments\COVID-19 Data Analysis\Districts\#Nagaland.csv")
        districts.set_index("Option No.",inplace=True)
        print(districts)
        print()
        opt_districts_no=int(input("ENTER OPTION NUMBER: "))
        NJ=opt_districts_no-1
        dt=districts.iloc[NJ]
        selected_district=dt["Districts"]# dt is a dataframe. selecting "Districts" column from dt.
        print()

    elif(selected_state=="Odisha"):
        districts=pd.read_csv('C:\Aswin\Python Assignments\COVID-19 Data Analysis\Districts\Odisha.csv')
        districts.set_index("Option No.",inplace=True)
        print(districts)
        print()
        opt_districts_no=int(input("ENTER OPTION NUMBER: "))
        NJ=opt_districts_no-1
        dt=districts.iloc[NJ]
        selected_district=dt["Districts"]# dt is a dataframe. selecting "Districts" column from dt.
        print()

    elif(selected_state=="Puducherry"):
        districts=pd.read_csv('C:\Aswin\Python Assignments\COVID-19 Data Analysis\Districts\Puducherry.csv')
        districts.set_index("Option No.",inplace=True)
        print(districts)
        print()
        opt_districts_no=int(input("ENTER OPTION NUMBER: "))
        NJ=opt_districts_no-1
        dt=districts.iloc[NJ]
        selected_district=dt["Districts"]# dt is a dataframe. selecting "Districts" column from dt.
        print()
    
    elif(selected_state=="Punjab"):
        districts=pd.read_csv('C:\Aswin\Python Assignments\COVID-19 Data Analysis\Districts\Punjab.csv')
        districts.set_index("Option No.",inplace=True)
        print(districts)
        print()
        opt_districts_no=int(input("ENTER OPTION NUMBER: "))
        NJ=opt_districts_no-1
        dt=districts.iloc[NJ]
        selected_district=dt["Districts"]# dt is a dataframe. selecting "Districts" column from dt.
        print()

    elif(selected_state=="Rajasthan"):
        districts=pd.read_csv('C:\Aswin\Python Assignments\COVID-19 Data Analysis\Districts\Rajasthan.csv')
        districts.set_index("Option No.",inplace=True)
        print(districts)
        print()
        opt_districts_no=int(input("ENTER OPTION NUMBER: "))
        NJ=opt_districts_no-1
        dt=districts.iloc[NJ]
        selected_district=dt["Districts"]# dt is a dataframe. selecting "Districts" column from dt.
        print()

    elif(selected_state=="Sikkim"):
        districts=pd.read_csv('C:\Aswin\Python Assignments\COVID-19 Data Analysis\Districts\Sikkim.csv')
        districts.set_index("Option No.",inplace=True)
        print(districts)
        print()
        opt_districts_no=int(input("ENTER OPTION NUMBER: "))
        NJ=opt_districts_no-1
        dt=districts.iloc[NJ]
        selected_district=dt["Districts"]# dt is a dataframe. selecting "Districts" column from dt.
        print()
    
    elif(selected_state=="Tamil Nadu"):
        districts=pd.read_csv('C:\Aswin\Python Assignments\COVID-19 Data Analysis\Districts\Tamil Nadu.csv')
        districts.set_index("Option No.",inplace=True)
        print(districts)
        print()
        opt_districts_no=int(input("ENTER OPTION NUMBER: "))
        NJ=opt_districts_no-1
        dt=districts.iloc[NJ]
        selected_district=dt["Districts"]# dt is a dataframe. selecting "Districts" column from dt.
        print()

    elif(selected_state=="Telangana"):
        districts=pd.read_csv('C:\Aswin\Python Assignments\COVID-19 Data Analysis\Districts\Telangana.csv')
        districts.set_index("Option No.",inplace=True)
        print(districts)
        print()
        opt_districts_no=int(input("ENTER OPTION NUMBER: "))
        NJ=opt_districts_no-1
        dt=districts.iloc[NJ]
        selected_district=dt["Districts"]# dt is a dataframe. selecting "Districts" column from dt.
        print()

    elif(selected_state=="Tripura"):
        districts=pd.read_csv('C:\Aswin\Python Assignments\COVID-19 Data Analysis\Districts\Tripura.csv')
        districts.set_index("Option No.",inplace=True)
        print(districts)
        print()
        opt_districts_no=int(input("ENTER OPTION NUMBER: "))
        NJ=opt_districts_no-1
        dt=districts.iloc[NJ]
        selected_district=dt["Districts"]# dt is a dataframe. selecting "Districts" column from dt.
        print()
    
    elif(selected_state=="Uttar Pradesh"):
        districts=pd.read_csv('C:\Aswin\Python Assignments\COVID-19 Data Analysis\Districts\#Uttar Pradesh.csv')
        districts.set_index("Option No.",inplace=True)
        pd.set_option('display.max_rows',None)#Shows every rows without default dropping of rows by
        print(districts)                      #python during display
        print()
        opt_districts_no=int(input("ENTER OPTION NUMBER: "))
        NJ=opt_districts_no-1
        dt=districts.iloc[NJ]
        selected_district=dt["Districts"]# dt is a dataframe. selecting "Districts" column from dt.
        print()
    
    elif(selected_state=="Uttarakhand"):
        districts=pd.read_csv('C:\Aswin\Python Assignments\COVID-19 Data Analysis\Districts\#Uttarakhand.csv')
        districts.set_index("Option No.",inplace=True)
        print(districts)
        print()
        opt_districts_no=int(input("ENTER OPTION NUMBER: "))
        NJ=opt_districts_no-1
        dt=districts.iloc[NJ]
        selected_district=dt["Districts"]# dt is a dataframe. selecting "Districts" column from dt.
        print()

    elif(selected_state=="West Bengal"):
        districts=pd.read_csv('C:\Aswin\Python Assignments\COVID-19 Data Analysis\Districts\West Bengal.csv')
        districts.set_index("Option No.",inplace=True)
        print(districts)
        print()
        opt_districts_no=int(input("ENTER OPTION NUMBER: "))
        NJ=opt_districts_no-1
        dt=districts.iloc[NJ]
        selected_district=dt["Districts"]# dt is a dataframe. selecting "Districts" column from dt.
        print()

    States_and_Districts_option.selected_state1=selected_state
    States_and_Districts_option.selected_district1=selected_district

