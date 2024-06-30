import time
import pyautogui
import requests 
import re
import os
# pip install pywhatkit
import pywhatkit as kit
from easygui import *
from bs4 import BeautifulSoup 

# sample web page
sample_web_page = 'https://online.aud.edu/Campus/summer12024ug.asp'
# Specify the phone number (with country code) and the message
phone_number = "+971569661626"
message = "This is an automated message... Class ENGL103 is open"
pyautogui.PAUSE = 0.1
# call get method to request that page
x = True
courseName = input("COURSE CODE : ").upper()
Section = input("COURSE SECTION : ").upper()
while x:
    page = requests.get(sample_web_page)
    print("ONLINE" if page.status_code == 200 else "Broken")
    if page.status_code != 200:
        print("servers are offline?")
        page.close()
        exit()
    # courseName = "ENGL103"
    # Section = "C"
    # with the help of beautifulSoup and html parser create soup
    soup = BeautifulSoup(page.content, "html.parser")
    for i in soup.find_all(string=re.compile(courseName)):
        print("".join(i.split("     ")), end=" ")
        print(i.parent.parent.parent.attrs["bgcolor"] == "#ffffff")
        if i.split("     -")[1] == Section and i.parent.parent.parent.attrs["bgcolor"] == "#ffffff":
            print("THIS IS YOUR SELECTED COURSE!\nITS AVAILABLE!\nWE NEED REGISTRATION")
            checkOnline = requests.get(R"https://studentlive.aud.edu/Login.aspx?ReturnUrl=%2f%3fwa%3dwsignin1.0%26wtrealm%3dhttps%253a%252f%252fonline.aud.edu%252f%26wct%3d2024-05-02T10%253a39%253a00Z%26wctx%3drm%253d0%2526id%253dpassive%2526ru%253dsecure%252fstudent%252fstuportal.aspx%26AppType%3dPortal%26Role%3dSTUDENT&wa=wsignin1.0&wtrealm=https%3a%2f%2fonline.aud.edu%2f&wct=2024-05-02T10%3a39%3a00Z&wctx=rm%3d0%26id%3dpassive%26ru%3dsecure%2fstudent%2fstuportal.aspx&AppType=Portal&Role=STUDENT")
            if (checkOnline.status_code == 200 ):
                # Send the message instantly
                kit.sendwhatmsg_instantly(phone_number, message, 50)
                x = False
                os.system('shutdown /s /f')
    page.close()
    time.sleep(45)
                # Register
                # pyautogui.hotkey('win', '2', interval=0.1)
                # pyautogui.sleep(8)
                # pyautogui.click(400, 60)
                # pyautogui.write('online.aud.edu', 0.02)
                # pyautogui.press('enter')
                # pyautogui.click(1790, 295, duration=6)
                # pyautogui.click(1500, 390, duration=0.2)
                # pyautogui.click(1472, 695, duration=5)
                # pyautogui.click(140, 307, duration=6)
                # pyautogui.click(142, 352, duration=0.4)
            #     while True:
            #         try:
            #             x = pyautogui.locateOnScreen(R"Python\Scraping\RegNotFound.png")
            #             print("broken")
            #             pyautogui.click(157, 60, duration=1)
            #             pyautogui.sleep(20)
            #             time.sleep(20)
            #         except:
            #             break
                    
            #     pyautogui.click(1175, 552, duration=0.4)
            #     pyautogui.press("down", interval=0.2)
            #     pyautogui.press('enter', interval=0.2)
            #     pyautogui.moveTo(1000, 560, duration=0.3)
            #     time.sleep(2)
            #     pyautogui.scroll(-2000)
            #     time.sleep(2)
            #     pyautogui.click(1477, 538, duration=5)
            #     pyautogui.sleep(2)
            #     pyautogui.click(R'Python\Scraping\imageQUICKADD.png')
            #     pyautogui.click(790, 627, duration=0.4)
            #     pyautogui.write(courseName)
            #     pyautogui.click(720, 709, duration=0.1)
            #     pyautogui.write(Section)
            #     pyautogui.click(1022, 805, duration=0.1)
            #     pyautogui.click(1022, 805, duration=0.2)
            #     pyautogui.click(1122, 266, duration=2)
            #     pyautogui.click(1688, 709, duration=12)
            #     x = False
            # else:
            #     print(R"https://studentlive.aud.edu/Login is offline.", checkOnline.status_code)    