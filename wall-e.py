import time
import datetime
import smtplib
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pyautogui as pg

s=Service('chromedriver.exe')
currentTime = datetime.datetime.now()
currentTime.hour
if currentTime.hour < 12:
    now="Good morning"
elif 12 <= currentTime.hour < 17:
    now="Good afternoon "
else:
    now="Good evening "
print("")
print(f"Hello Sir ... {now}! ")
print("I'm Wall-E ;) \nA small scale assistant created by Adarsh Gupta \n")

def github():
    driver=webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get('https://github.com/login')
    time.sleep(1)
    user=driver.find_element('id','login_field')
    user.click()
    user.send_keys('adgupta183@gmail.com')
    paswd=driver.find_element("id",'password')
    paswd.click()
    paswd.send_keys('yourgithubPasswd')
    submit=driver.find_element('name','commit')
    submit.click()

def whatsapp():
    driver=webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get('https://web.whatsapp.com/')

def youtube():
    driver=webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get('https://youtube.com/')

def javaonlinec():
    driver=webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get('https://www.onlinegdb.com/online_java_compiler')

def sendEmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('adgupta183@gmail.com', 'yourGoogleappPassswdforbypassing2-stepverification')
    msg=f"subject : {sub} \n\n{body}"
    server.sendmail('adgupta183@gmail.com', to_user , msg)
    print("Your message has been delivered successfully !")

def lastoptn():
    pg.moveTo(101,1057,0.1)
    pg.click()
    pg.write(input_user)
    pg.press('enter')

def search():
    driver=webdriver.Chrome(service=s)
    driver.maximize_window()
    pg.moveTo(312,65,0.1)
    pg.click()
    word=input_user[7:]
    pg.write(word)
    pg.press('enter')

while(True):
    print("\nHow can I help you today \n")
    input_user=input().lower()

    if 'github' in input_user:
        github()

    elif 'email' in input_user:
        print("Enter the recipient address ?")
        to_user=input()
        print("Enter the subject be : ")
        sub=input()
        print("Enter the body : ")
        body=input()
        sendEmail()

    elif 'wp' in input_user or 'whatsapp' in input_user:
        whatsapp()

    elif 'yt' in input_user or 'youtube' in input_user:
        youtube()

    elif 'java' in input_user or 'java compiler' in input_user:
        javaonlinec()

    elif 'search' in input_user:
        search()
    
    elif 'quit' in input_user or 'exit' in input_user:
        print("Thank you Sir, Have a good day!")
        break

    else: 
        lastoptn()
