import os 
from dotenv import load_dotenv
import requests 

load_dotenv() 
api_key = os.getenv("api_key")  




import tkinter as tk 
from tkinter import ttk
import requests
import json
def data_get():
 city = city_name.get().strip()
 
 url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

 

 response= requests.get(url) 
 data = response.json()
 w_label1.config(text=data["weather"][0]["main"])

 wd_label1.config(text=data["weather"][0]["description"])

 temp_label1.config(text=str(data["main"]["temp"]) + "°C")
 pres_label1.config(text=data["main"]["pressure"])

 payload = json.loads(response.text)
 print(payload) 



win = tk.Tk()
win.title("Weather App") 
win.config(bg = "blue")
win.geometry("600x600")

name_label = tk.Label(win, text = "Weather App", 
                   font = ("Aptos",30,"bold"))
name_label.place(x=25,y=50,height = 50,width = 450)
city_name = tk.StringVar()

list_name = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
    "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
    "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
    "Uttar Pradesh", "Uttarakhand", "West Bengal"]
combo = ttk.Combobox(win, text = "Weather App", values = list_name,textvariable= city_name) 
combo.set("Select City" )            
combo.place(x=50,y= 150, width = 450)




w_label = tk.Label(win,text= "Weather Climate", 
                   font= ("Aptos" , 18, "bold"))
w_label.place(y=270, x= 50, height= 50, width = 250)

w_label1 = tk.Label(win,text= "", 
                   font= ("Aptos" , 18, "bold"))
w_label1.place(y=270, x= 320, height= 50, width = 250)




wd_label = tk.Label(win,text = "Weather Description", 
                    font= ("Aptos", 18,"bold")) 
wd_label.place(y= 350, x = 50, height= 50, width = 250)  

wd_label1 = tk.Label(win,text = "", 
                    font= ("Aptos", 18,"bold")) 
wd_label1.place(y= 350, x = 320, height= 50, width = 250)  





temp_label= tk.Label(win,text = "Temperature", 
                    font= ("Aptos", 18,"bold"))
temp_label.place(y=420,x=50, height=50,width=250 ) 

temp_label1= tk.Label(win,text = "", 
                    font= ("Aptos", 18,"bold"))
temp_label1.place(y=420,x=320, height=50,width=250 ) 




pres_label= tk.Label(win,text = "Pressure", 
                    font= ("Aptos", 18,"bold"))
pres_label.place(x=50, y= 490, height= 50, width=250) 

pres_label1= tk.Label(win,text = "", 
                    font= ("Aptos", 18,"bold"))
pres_label1.place(x=320, y= 490, height= 50, width=250) 



done_button = tk.Button(win, text = "Done", 
                   font = ("Aptos",30,"bold"),command=data_get)
done_button.place(y = 200, x = 200, height = 50, width = 100) 




 
win.mainloop() 