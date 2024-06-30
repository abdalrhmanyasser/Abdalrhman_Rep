import time
import pyautogui
import os
def clickOnImage(imgName, _region):
    CLICKED = False
    while not CLICKED:
        try:
            p = pyautogui.locateCenterOnScreen(imgName, region=_region)
            pyautogui.click(p.x, p.y, duration=0.3)
            pyautogui.moveTo(0, 0, duration=0.1)
            time.sleep(0.3)
            pyautogui.keyDown('ctrl')
            pyautogui.press('tab', interval=0.1)
            pyautogui.keyUp('ctrl')
            pyautogui.sleep(2)
            CLICKED=True
        except:
            pass
link = R"https://datanodes.to/m58ia0el0517/RDR2_--_fitgirl-repacks.site_--_.part*.rar"
links = []
for i in range(137):
    links.append(link.split("*")[0] + str(i) + ".rar")
for i in range(6):
    for j in range(23):
        # os.system("start " + links[(i+1)*(j+1)-1])
        pass
    for j in range(23):
        clickOnImage(R'C:\Users\abdal\Documents\Visual Code\Abdalrhman_Rep\Python\Scraping\CONDOWN.png', (1252, 795, 600, 200))
        