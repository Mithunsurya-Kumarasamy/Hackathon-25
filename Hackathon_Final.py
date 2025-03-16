from customtkinter import *
from PIL import Image
import mysql.connector
import smtplib
import tkinter as tk
from tkinter import ttk
from geopy.distance import geodesic
from collections import Counter

import time
from geopy.geocoders import Nominatim



conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mithun@1313"
)

cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS disaster_db")
conn.commit()

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mithun@1313",
    database="disaster_db"
)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Inventory(
        item_id INT PRIMARY KEY AUTO_INCREMENT,
        item_name VARCHAR(255) NOT NULL,
        quantity INT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Chennai_Inventory(
        item_id INT PRIMARY KEY AUTO_INCREMENT,
        item_name VARCHAR(255) NOT NULL,
        quantity INT NOT NULL
    )
''')

cursor.execute('''  
    CREATE TABLE IF NOT EXISTS Bangalore_Inventory(
        item_id INT PRIMARY KEY AUTO_INCREMENT,
        item_name VARCHAR(255) NOT NULL,
        quantity INT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Mumbai_Inventory(
        item_id INT PRIMARY KEY AUTO_INCREMENT,
        item_name VARCHAR(255) NOT NULL,
        quantity INT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Requests(
        request_id INT PRIMARY KEY AUTO_INCREMENT,
        item_name VARCHAR(255) NOT NULL,
        quantity_needed INT NOT NULL,
        priority INT NOT NULL,
        location VARCHAR(255) NOT NULL,
        volunteer INT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Allocations(
        alloc_id INT PRIMARY KEY AUTO_INCREMENT,
        request_id INT,
        item_name VARCHAR(255) NOT NULL,
        allocated_to VARCHAR(255) NOT NULL,
        FOREIGN KEY (request_id) REFERENCES Requests(request_id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Volunteers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        age INT,
        location VARCHAR(255),
        email VARCHAR(255),
        assigned_location VARCHAR(255)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Locations (
        location_id INT PRIMARY KEY AUTO_INCREMENT,
        city_name VARCHAR(255) NOT NULL,
        latitude FLOAT NOT NULL,
        longitude FLOAT NOT NULL
    )
''')

locations=[
    ("Chennai", 13.08, 80.27), ("Coimbatore", 11.01, 76.95), ("Madurai", 9.92, 78.11),
    ("Tiruchirappalli", 10.79, 78.70), ("Salem", 11.66, 78.14), ("Tirunelveli", 8.71, 77.75),
    ("Erode", 11.34, 77.71), ("Vellore", 12.91, 79.13), ("Thoothukudi", 8.76, 78.13),
    ("Tiruppur", 11.10, 77.34), ("Kanchipuram", 12.83, 79.70), ("Dindigul", 10.36, 77.97),
    ("Thanjavur", 10.78, 79.13), ("Karur", 10.96, 78.07), ("Nagapattinam", 10.76, 79.83)
]

cursor.executemany('''
    INSERT IGNORE INTO Locations (city_name, latitude, longitude) 
    VALUES (%s, %s, %s)
''', locations)



conn.commit()

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mithun@1313",
    database="disaster_db"
)
cursor = conn.cursor()

items = [
    ("Rice", 100, "Food"), 
    ("Wheat Flour", 80, "Food"), 
    ("Bottled Water", 200, "General"), 
    ("First Aid Kit", 50, "Medical"), 
    ("Canned Food", 120, "Food"),
    ("Blankets", 75, "General"),
    ("Painkillers", 90, "Medical"),
    ("Milk Powder", 60, "Food"),
    ("Torch", 30, "General"),
    ("Sanitary Pads", 110, "Medical")
]


inventories = ["Inventory", "Chennai_Inventory", "Bangalore_Inventory", "Mumbai_Inventory"]

# Insert data only if the table is empty
for inventory in inventories:
    cursor.execute(f"SELECT COUNT(*) FROM {inventory}")
    count = cursor.fetchone()[0]  # Get row count
    
    if count == 0:
        query = f"INSERT INTO {inventory} (item_name, quantity, item_type) VALUES (%s, %s, %s)"
        cursor.executemany(query, items)  # Batch insert all 10 items
        conn.commit()
        print(f"Added sample data to {inventory} successfully!")
    else:
        print(f"{inventory} already has data. Skipping insertion.")

cursor.close()
conn.close()

print("Database population complete!")


#main


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mithun@1313",
    database="disaster_db"
)
cursor = conn.cursor()
disaster_list=[]
fetched_lst=[]
resource_list=[]
cursor.execute("SELECT * FROM inventory")
fetched_lst=cursor.fetchall()
def submit_info(popup,textbox,disaster,severity,no_of_people,urgency):
    disaster_list.append({"Disaster":disaster,"Address":textbox.get("1.0","end-1c"),"Severity":severity,"People":no_of_people,"Urgency":urgency})
    print(disaster_list)
    popup.destroy()
    need_resource()
def disaster_info():
    popup=CTk()
    popup.geometry('500x500')
    popup.title('Collecting Information')
    options1 = ["EarthQuake", "Flood", "Tsunami", "Volcano eruption","landslides"]
    disaster=options1[0]
    severity=0
    no_of_people=0
    urgency=0

    def choose_disaster(selection):
        nonlocal disaster
        disaster=selection
        print(disaster)

    def choose_severity(selection):
        nonlocal severity
        severity=int(selection[0])
        print(type(severity))

    def choose_population(selection):
        nonlocal no_of_people
        no_of_people=int(selection[0])
        print(no_of_people)

    def choose_urgency(selection):
        nonlocal urgency
        urgency=int(selection[0])
        
    CTkLabel(popup,text="Disaster").place(x=30,y=50)
    dropdown1=CTkOptionMenu(master=popup,values=options1,width=300,command=choose_disaster)
    dropdown1.set("Choose")
    dropdown1.place(x=30,y=75)
    CTkLabel(popup,text="Location").place(x=30,y=120)
    textbox=CTkTextbox(popup,width=300,height=30)
    textbox.place(x=30,y=145)

    
    CTkLabel(popup,text="Severity").place(x=30,y=190)
    options2=["1 (Life-Threatening)","2 (Serious but not critical)","3 (Manageable)"]
    dropdown2=CTkOptionMenu(master=popup,values=options2,width=190,command=choose_severity)
    dropdown2.set("Choose")
    dropdown2.place(x=30,y=215)


    CTkLabel(popup,text="Number of people affected").place(x=250,y=190)
    options3=["1 (Thousands)","2 (Hundreds)","3 (Few people)"]
    dropdown3=CTkOptionMenu(master=popup,values=options3,width=190,command=choose_population)
    dropdown3.set("Choose")
    dropdown3.place(x=250,y=215)


    CTkLabel(popup,text="Urgency").place(x=30,y=260)
    options4=["1 (Immediate action required)","2 (Needs action soon)","3 (Can wait)"]
    dropdown4=CTkOptionMenu(master=popup,values=options4,width=220,command=choose_urgency)
    dropdown4.set("Choose")
    dropdown4.place(x=30,y=285)
    submit_button=CTkButton(popup,text="Submit",command=lambda:submit_info(popup,textbox,disaster,severity,no_of_people,urgency))
    submit_button.place(x=30,y=320)
    print(disaster_list)
    popup.mainloop()

def get_specific_list(to_get_from_db):
    global fetched_lst
    to_get_from_db=tuple(to_get_from_db.split(","))
    placeholders = ", ".join(["%s"] * len(to_get_from_db))
    query = f"SELECT * FROM inventory WHERE type IN ({placeholders})"
    cursor.execute(query, to_get_from_db)
    print(f"'{to_get_from_db}'")
    fetched_lst=cursor.fetchall()
    need_resource_frame.destroy()
    need_resource()

def add_resource(textboxes_list,volunteer_textbox):
    global resource_list
    if len(resource_list)<len(disaster_list):
        temp_dict={}
        for i in textboxes_list:
            if (i[1].get("1.0","end-1c")!=""):
                temp_dict[i[0]]=int(i[1].get("1.0","end-1c"))
        temp_dict["volunteer"]=int(volunteer_textbox.get("1.0","end-1c"))
        resource_list.append(temp_dict)
    else:
        for i in textboxes_list:
            if (i[1].get("1.0","end-1c")!=""):
                resource_list[len(resource_list)-1][i[0]]=int(i[1].get("1.0","end-1c"))
        resource_list[len(resource_list)-1]["volunteer"]=int(volunteer_textbox.get("1.0","end-1c"))
    print(resource_list)

            
def get_full_list():
    global fetched_lst
    cursor.execute("SELECT * FROM inventory")
    fetched_lst=cursor.fetchall()
    need_resource_frame.destroy()
    need_resource()
def get_list(to_get_from_db):
    global fetched_lst
    print(to_get_from_db)
    cursor.execute("SELECT * FROM inventory WHERE item_name LIKE %s", (f"%{to_get_from_db}%",))
    fetched_lst=cursor.fetchall()
    if fetched_lst==[]:
        messagebox.showinfo("Error", "No Items Found!!")
        cursor.execute("SELECT * FROM inventory")
        fetched_lst=cursor.fetchall()
    need_resource_frame.destroy()
    need_resource()
def go_back():
    need_resource_frame.destroy()
def need_resource():
    global need_resource_frame
    global fetched_list
    need_resource_frame=CTkFrame(main_frame,width=2000,height=700,fg_color="blue")
    need_resource_frame.place(x=0,y=0)

    
    background_img=CTkImage(Image.open(r'D:\__pycache__\Mithhhh.png'),size=(2300,800))
    img_label=CTkLabel(need_resource_frame,image=background_img,text="")
    img_label.place(x=0,y=0)
    CTkLabel(need_resource_frame,text="RESOURCES",font=("Georgia",40,"bold"),bg_color="blue").place(x=500,y=40)


    shortcut_panel_frame=CTkFrame(need_resource_frame,width=200,height=400,fg_color="white")
    shortcut_panel_frame.place(x=30,y=200)
    CTkLabel(shortcut_panel_frame,text="Shortcut Panel",font=("Georgia",16,"bold"),text_color="black").place(x=40,y=30)
    radio_var=IntVar() 
    print(radio_var)
    CTkRadioButton(shortcut_panel_frame,text="Food",text_color="black",variable=radio_var,value=1,command=lambda:get_specific_list("food")).place(x=20,y=100)
    CTkRadioButton(shortcut_panel_frame,text="General items",text_color="black",variable=radio_var,value=2,command=lambda:get_specific_list("medical,other")).place(x=20,y=140)
    CTkRadioButton(shortcut_panel_frame,text="Medical needs",text_color="black",variable=radio_var,value=3,command=lambda:get_specific_list("medical")).place(x=30,y=180)
    CTkRadioButton(shortcut_panel_frame,text="Other needs",text_color="black",variable=radio_var,value=4,command=lambda:get_specific_list("other")).place(x=30,y=220)
    CTkLabel(shortcut_panel_frame,text="Volunteers Required-",font=("Georgia",16,"bold"),text_color="black").place(x=10,y=300)
    volunteer_textbox=CTkTextbox(shortcut_panel_frame,width=100,height=2,fg_color="grey")
    volunteer_textbox.place(x=10,y=340)
    
    border_frame=CTkFrame(need_resource_frame,width=650,height=360)
    border_frame.place(x=350,y=200)
    resource_main_frame=CTkScrollableFrame(border_frame,width=650,height=360)
    resource_main_frame.pack(pady=20,padx=20,fill="both",expand=True)

    search_frame=CTkFrame(need_resource_frame,width=712,height=50)
    search_frame.place(x=350,y=130)
    CTkLabel(search_frame,text="Search:\t      Name:",font=("Georigia",21,"bold")).place(x=5,y=11)
    searchbox=CTkTextbox(search_frame,width=100,height=3,fg_color="white",text_color="black")
    searchbox.place(x=210,y=11)

    select_button=CTkButton(search_frame,text="Search",width=30,command=lambda:get_list(searchbox.get("1.0","end-1c")))
    select_button.place(x=330,y=12)
    clear_button=CTkButton(search_frame,text="Clear",width=30,command=get_full_list)
    clear_button.place(x=400,y=12)

    CTkLabel(resource_main_frame,text="S.no",font=("Georgia",20,"bold")).grid(column=0,row=0,pady=10,padx=70)
    CTkLabel(resource_main_frame,text="Item",font=("Georgia",20,"bold")).grid(column=2,row=0,pady=10,padx=70)
    CTkLabel(resource_main_frame,text="Request Quantity",font=("Georgia",20,"bold")).grid(column=4,row=0,pady=10,padx=70)

    count=0
    textboxes_list=[]
    for i in fetched_lst:
        count+=1
        CTkLabel(resource_main_frame,text=f"{count}",text_color="white").grid(row=count+1,column=0,pady=10,padx=70)
        CTkLabel(resource_main_frame,text=f"{i[1].upper()}",text_color="white").grid(row=count+1,column=2,pady=10,padx=70)
        textbox=CTkTextbox(resource_main_frame,width=150,height=1)
        textbox.grid(row=count+1,column=4,pady=10,padx=70)
        textboxes_list.append([i[1],textbox])

    submit_button_frame=CTkFrame(need_resource_frame,width=200,height=50,fg_color="black")
    submit_button_frame.place(x=890,y=610)
    add_button=CTkButton(submit_button_frame,text="ADD",width=150,height=40,fg_color="black",command=lambda:add_resource(textboxes_list,volunteer_textbox))
    add_button.pack(padx=10)
    back_button=CTkButton(need_resource_frame,text="< BACK",width=150,height=40,fg_color="black",command=go_back)
    back_button.place(x=1060,y=610)
        
def find_closest_city(user_cities1, related_list1):
    user_cities=user_cities1
    related_list=related_list1
    locations=[
    ("Mumbai",19.07,72.87),("Delhi",28.61,77.23),("Bangalore",12.97,77.59),
    ("Hyderabad",17.38,78.48),("Chennai",13.08,80.27),("Kolkata",22.57,88.36),
    ("Ahmedabad",23.03,72.58),("Pune",18.52,73.85),("Jaipur",26.91,75.79),
    ("Surat",21.17,72.83),("Lucknow",26.85,80.94),("Chandigarh",30.74,76.79),
    ("Visakhapatnam",17.69,83.21),("Bhopal",23.25,77.41),("Patna",25.59,85.13)
                    ]

    city_crds={city:(lat,lon)for city,lat,lon in locations}
    closest_counts=Counter()
    
    for city,(lat1,lon1) in city_crds.items():
        min_distance=0
        closest_city=city
        
        for other_city,(lat2,lon2) in city_crds.items():
            distance=geodesic((lat1,lon1),(lat2,lon2)).kilometers
            if distance<min_distance or closest_city==city:
                min_distance=distance
                closest_city=other_city
        
        closest_counts[closest_city]+=1

    sorted_requests=sorted(user_cities,key=lambda x:closest_counts.get(x["Address"],0),reverse=True)

    # Sorting related_list based on the same order as sorted_requests
    sorted_related_list=[related_list[user_cities.index(item)]for item in sorted_requests]

    return sorted_requests,sorted_related_list



def priority(disaster_lst1,related_lst1):
    lst1=[]
    disaster_lst=disaster_lst1
    related_lst=related_lst1
    for i in disaster_lst:
        lst1.append(i["Severity"]+i["People"]+i["Urgency"])
    for i in range(len(disaster_lst)-1):
        for j in range(i+1,len(disaster_lst)):
            if(lst1[i]>lst1[j]):
                a=lst1[i]
                lst1[i]=lst1[j]
                lst1[j]=a
                a=disaster_lst[i]
                disaster_lst[i]=disaster_lst[j]
                disaster_lst[j]=a
                a=related_lst[i]
                related_lst[i]=related_lst[j]
                related_lst[j]=a
    lst=[]
    count=0
    running=[i for i in range(len(disaster_lst)-1)]

    i=0
    while(i<len(disaster_lst)-1):
        while(lst1[i]==lst1[i+1]):
            
            
            i+=1
            if(i==len(disaster_lst)-1):
                
                break
            
        for j in range(count,i):
            for k in range(j+1,i+1):
                if(disaster_lst[j]["People"]>disaster_lst[k]["People"]):
                    a=disaster_lst[j]
                    disaster_lst[j]=disaster_lst[k]
                    disaster_lst[k]=a
                    a=related_lst[j]
                    related_lst[j]=related_lst[k]
                    related_lst[k]=a
        i+=1
    return disaster_lst,related_lst

def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="city_distance_calculator")
    location = geolocator.geocode(city_name)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None

def closestVolunteer(aLoc,volunteers):
    
    print(volunteers)
    minDis=float('inf')
    closestVol=None
    aLoc = get_coordinates(aLoc)
    
    for vId,vLoc,assigned_location in volunteers:
        if(assigned_location==''):
            vLoc = get_coordinates(vLoc)
            dist=geodesic(aLoc, vLoc).kilometers
            if minDis>dist:
                minDis=dist
                closestVol=vId
    print(closestVol,"hello",aLoc)
    return closestVol

def find_closest_inventory(user_city):
    city_crds={"Chennai":(13.08, 80.27),"Bangalore": (12.97, 77.59),"Mumbai": (19.07, 72.87)}
    if user_city in city_crds:
        user_crds=city_crds[user_city]
    else:
        return ["Chennai_Inventory", "Bangalore_Inventory", "Mumbai_Inventory"]
    
    sorted_inventories=sorted(city_crds.keys(),key=lambda city:geodesic(user_crds,city_crds[city]).kilometers)
    return [f"{city}_Inventory" for city in sorted_inventories]

def fcfsAlloc(disaster_lst,resource_lst):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mithun@1313",
        database="disaster_db"
    )
    cursor = conn.cursor()
    counting=0
    
    for r in resource_lst:
        volunteer = r["volunteer"]
        print(volunteer)
        

        for i in range(0,volunteer):
            cursor.execute("SELECT id,location,assigned_location FROM Volunteers WHERE assigned_location IS NULL OR assigned_location=''")
            volunteers=cursor.fetchall()
            closest_volunteer=closestVolunteer(disaster_lst[counting]["Address"],volunteers)
            if closest_volunteer:
                
                cursor.execute("UPDATE Volunteers SET assigned_location=%s WHERE id=%s",(disaster_lst[counting]["Address"],closest_volunteer))
                conn.commit()
                print("Hi")
        inventories=find_closest_inventory(disaster_lst[counting]["Address"])
        for item_name, quantity_needed in r.items():
            if item_name == "volunteer":
                continue

            allocated_quantity = 0
            for inventory in inventories:
                if allocated_quantity >= quantity_needed:
                    break
                cursor.execute(f"SELECT quantity FROM {inventory} WHERE item_name=%s", (item_name,))
                data = cursor.fetchone()
                
                if data:
                    available_quantity = data[0]
                    if available_quantity > 0:
                        to_allocate = min(quantity_needed - allocated_quantity, available_quantity)
                        allocated_quantity += to_allocate

                        cursor.execute(f"UPDATE {inventory} SET quantity = quantity - %s WHERE item_name = %s", 
                                       (to_allocate, item_name))
                        conn.commit()
                        print(f"Allocated {to_allocate} of {item_name} from {inventory}")

            if allocated_quantity < quantity_needed:
               import smtplib
               s = smtplib.SMTP('smtp.gmail.com', 587)
               s.starttls()
               s.login("24pd24@psgtech.ac.in", "Mithun1313@psgtech")
               message = f"STOCK ALERT: {item_name} is running low!"
               s.sendmail("24pd24@psgtech.ac.in", "24pd21@psgtech.ac.in", message)
               s.quit()
            conn.commit()
        counting+=1
    conn.close()

#allocation

def show_fifo(new_win,value):
    if (len(resource_list)==0):
        messagebox.showinfo("Error", "Nothing has been allocated")
    else:
        
        border_frame=CTkFrame(new_win,width=400,height=400)
        border_frame.place(x=0,y=0)
        scolling_frame=CTkScrollableFrame(border_frame,width=400,height=400)
        scolling_frame.pack(pady=20,padx=20,fill="both",expand=True)
        if value==1:
            dis,res=disaster_list,resource_list
        if value==2:
            dis,res=priority(disaster_list,resource_list)
        if  value==3:
            dis,res=find_closest_city(disaster_list,resource_list)
        allocate=CTkButton(new_win,text="Allocate",command=lambda:fcfsAlloc(dis,res))
        allocate.place(x=200,y=450)
        count=1
        for i in range(len(dis)):
            CTkLabel(scolling_frame,text=f"{count}.").pack(pady=5)
            CTkLabel(scolling_frame,text=f"Disaster:{dis[i]['Disaster']}").pack(pady=5)
            CTkLabel(scolling_frame,text=f"Location:{dis[i]['Address']}").pack(pady=5)
            CTkLabel(scolling_frame,text=f"Severity:{dis[i]['Severity']}\tPeople Affected:{dis[i]['People']}").pack(pady=5)
            CTkLabel(scolling_frame,text=f"Urgency:{dis[i]['Urgency']}").pack(pady=5)
            
            for j in res[i]:
                CTkLabel(scolling_frame,text=f"{j}:{res[i][j]}").pack(pady=5)
            count+=1

def allocate_resource():
    new_win=CTk()
    new_win.geometry("500x500")
    new_win.title("Allocation of resource")
    CTkLabel(new_win,text="View Results",font=("Georgia",26,"bold")).place(x=150,y=30)
    fifo_button=CTkButton(new_win,text="FIFO method",command=lambda:show_fifo(new_win,1))
    fifo_button.place(x=150,y=100)
    
    priority_button=CTkButton(new_win,text="Priority method",command=lambda:show_fifo(new_win,2))
    priority_button.place(x=150,y=150)
    location_button=CTkButton(new_win,text="Location method",command=lambda:show_fifo(new_win,3))
    location_button.place(x=150,y=200)
    new_win.mainloop()

# Tkinter GUI for Volunteer Registration
def volunteer_adding():
    root = CTk()
    root.title("Volunteer Registration")
    root.geometry("400x400")


    frame = CTkFrame(root,width=400,height=400)
    frame.pack()

    CTkLabel(frame, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    name_entry = CTkTextbox(frame, width=100,height=30)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    CTkLabel(frame, text="Age:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    age_entry = CTkTextbox(frame, width=100,height=30)
    age_entry.grid(row=1, column=1, padx=5, pady=5)

    CTkLabel(frame, text="Location:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
    location_entry = CTkTextbox(frame, width=100,height=30)
    location_entry.grid(row=2, column=1, padx=5, pady=5)

    CTkLabel(frame, text="Email:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
    email_entry = CTkTextbox(frame, width=100,height=30)
    email_entry.grid(row=3, column=1, padx=5, pady=5)

    def volMail(location,email):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("24pd24@psgtech.ac.in", "Mithun1313@psgtech")
        message = "\nYou have been registered as a volunteer!\nThankyou!"
        s.sendmail("24pd24@psgtech.ac.in", email, message)
        s.quit()

    def reg():
        name = name_entry.get("1.0","end-1c")
        age = age_entry.get("1.0","end-1c")
        location = location_entry.get("1.0","end-1c")
        email = email_entry.get("1.0","end-1c")
        
        assigned_loc = ""
        cursor.execute("INSERT INTO Volunteers (name, age, location, email, assigned_location) VALUES (%s, %s, %s, %s, %s)",
                       (name, age, location, email, assigned_loc))
        conn.commit()
        #volMail(location,email)
        
    register_button = CTkButton(root, text="Register", command=reg)
    register_button.pack(pady=10)

    root.mainloop()


def stock_renewal(item_name, quantity, item_type, inv_name):
    if inv_name not in ["Chennai_Inventory", "Bangalore_Inventory", "Mumbai_Inventory"]:
        return
    cursor.execute(f"SELECT quantity FROM {inv_name} WHERE item_name = %s", (item_name,))
    data = cursor.fetchone()

    if data:
        new_quantity = data[0] + quantity
        cursor.execute(f"UPDATE {inv_name} SET quantity = %s WHERE item_name = %s", (new_quantity, item_name))
    else:
        cursor.execute(f"INSERT INTO {inv_name} (item_name, quantity, type) VALUES (%s, %s, %s)", 
                       (item_name, quantity, item_type))
    
    conn.commit() 
    cursor.execute("SELECT quantity FROM Inventory WHERE item_name = %s", (item_name,))
    inv_data = cursor.fetchone()

    if inv_data:
        new_inv_quantity = inv_data[0] + quantity
        cursor.execute("UPDATE Inventory SET quantity = %s WHERE item_name = %s", (new_inv_quantity, item_name))
    else:
    
        cursor.execute("INSERT INTO Inventory (item_name, quantity, type) VALUES (%s, %s, %s)",(item_name, quantity, item_type))

    conn.commit()
def submit_info2(popup, textbox, database, quantity_entry,item_type):
    stock_renewal(textbox.get("1.0","end-1c"), int(quantity_entry.get("1.0","end-1c")), item_type, database)
    popup.destroy()
    
def add_resource_to_stock():
    
    options1 = ["Chennai_Inventory","Bangalore_Inventory","Mumbai_Inventory"]
    database=options1[0]
    quantity_entry=0
    item_type=0
    
    popup = CTk()
    popup.geometry('500x500')
    popup.title('Collecting Information')
    
    def choose_database(selection):
        nonlocal database
        database = selection
        print(database)
    
    def choose_type(selection):
        nonlocal item_type
        selection=selection.partition(" ")
        item_type = selection[2].rstrip(")")
        item_type = item_type.lstrip("(")
        print(item_type)
        
    CTkLabel(popup, text="Inventory").place(x=30, y=50)
    dropdown1 = CTkOptionMenu(popup, values=options1, width=300, command=choose_database)
    dropdown1.set("Choose")
    dropdown1.place(x=30, y=75)
    
    CTkLabel(popup, text="Item").place(x=30, y=120)
    textbox = CTkTextbox(popup, width=300, height=30)
    textbox.place(x=30, y=145)
    
    CTkLabel(popup, text="Quantity").place(x=30, y=190)
    quantity_entry = CTkTextbox(popup, width=300, height=30)
    quantity_entry.place(x=30, y=215)
    
    CTkLabel(popup, text="Item Type").place(x=30, y=260)
    options4 = ["1 (Food Item)", "2 (Medicinal Item)", "3 (Others)"]
    dropdown4 = CTkOptionMenu(popup, values=options4, width=220, command=choose_type)
    dropdown4.set("Choose")
    dropdown4.place(x=30, y=285)
    
    submit_button = CTkButton(popup, text="Submit",
                                  command=lambda: submit_info2(popup, textbox, database, quantity_entry,item_type))
    submit_button.place(x=165, y=420)
   
    
    popup.mainloop()
     
global main_frame
main_page=CTk()
main_page.geometry('2000x700')
main_page.title('Disaster Relief Suppy System')
main_frame=CTkFrame(main_page,width=2000,height=700,fg_color="blue")
main_frame.place(x=0,y=0)
need_resource()
background_img=CTkImage(Image.open(r'D:\__pycache__\Mithhhh.png'),size=(2000,700))
img_label=CTkLabel(main_frame,image=background_img,text="")
img_label.place(x=0,y=0)
title_label = CTkLabel(main_frame, text="Emergency Resource Management System", font=("Arial", 40, "bold"))
title_label.place(x=350,y=40)
need_resourse_button=CTkButton(main_frame,text="Need Resourse",width=170,height=100,text_color="white",font=("Arial", 16, "bold"),command=disaster_info)
need_resourse_button.place(x=450,y=350)
add_resource_button = CTkButton(main_frame, text="Add Resource", width=170, height=100,text_color="white", font=("Arial", 16, "bold"), command=add_resource_to_stock)

add_resource_button.place(x=625, y=350)
volunteer_button=CTkButton(main_frame,text="Volunteer",width=170,height=100,text_color="white",font=("Arial", 16, "bold"),command=volunteer_adding)
volunteer_button.place(x=800,y=350)
allocate_resource_button=CTkButton(main_frame,text="Allocate Resource",width=170,height=100,text_color="white",font=("Arial", 16, "bold"),command=allocate_resource)
allocate_resource_button.place(x=625,y=500)
main_page.mainloop()
