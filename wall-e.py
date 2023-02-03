import time
import datetime
import smtplib
import subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

s=Service('chromedriver.exe')
currentTime = datetime.datetime.now()
currentTime.hour
if currentTime.hour < 12:
    now="Good morning"
elif 12 <= currentTime.hour < 18:
    now="Good afternoon "
else:
    now="Good evening "
print("\n")
print(f"Hello Sir ... {now}! ")
print("I'm Wall-E ;) \nA small scale assistant created by Adarsh Gupta ")
print("\n")

def github():
    driver=webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get('https://github.com/login')
    time.sleep(1)
    user=driver.find_element_by_id('login_field')
    user.click()
    user.send_keys('adgupta183@gmail.com')
    paswd=driver.find_element_by_id('password')
    paswd.click()
    paswd.send_keys('yourpassword')
    submit=driver.find_element_by_name('commit')
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
    server.login('adgupta183@gmail.com', 'googleAppcodeforbypassing2stepauthentication')
    msg=f"subject : {sub} \n\n{body}"
    server.sendmail('adgupta183@gmail.com', to_user , msg)
    print("Your message has been delivered successfully !")

def notepad():
    subprocess.call('notepad.exe')

def calculator():
    subprocess.call('calc.exe')

def excel():
    subprocess.call('C://Program Files (x86)//Microsoft Office//root//Office16//EXCEL.exe')

def powerpoint():
    subprocess.call('C://Program Files (x86)//Microsoft Office//root//Office16//POWERPNT.exe')

def explorer():
    subprocess.call('explorer.exe')

def word():
    subprocess.call('C://Program Files (x86)//Microsoft Office//root//Office16//WINWORD.exe')

def idle():
    subprocess.call('IDLE.exe')


while(True):
    print("How can i help you today ")
    input_user=input().lower()

    if 'github' in input_user:
        github()

    elif 'whatsapp' in input_user:
        whatsapp()

    elif 'email' in input_user:
        print("Enter the recipient address : ")
        to_user=input()
        print("Enter the subject be : ")
        sub=input()
        print("Enter the body : ")
        body=input()
        sendEmail()

    elif 'notepad' in input_user:
        notepad()

    elif 'calc' in input_user:
        calculator()

    elif 'explorer' in input_user:
        explorer()

    elif 'excel' in input_user:
        excel()

    elif 'ppt' in input_user:
        powerpoint()

    elif 'word' in input_user:
        word()

    elif 'yt' in input_user:
        youtube()

    elif 'java' in input_user:
        javaonlinec()

    elif 'idle' in input_user:
        idle()
    
    elif 'quit' in input_user:
        break

    else: 
        print("Out of Limits")
