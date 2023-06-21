import pyautogui as pg
import time

time.sleep(5)
for i in range(2):
    pg.write("Explaining PyAutoGUI... message no. " + str(i+1))
    pg.press("Enter")
 

print(pg.write("This is a text written slowly",interval=0.2))
pg.press("Enter")









