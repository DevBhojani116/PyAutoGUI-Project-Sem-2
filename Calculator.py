import pyautogui as pg
import time

def button_location(img): #function to find out where I need to click
    imgLocation = pg.locateOnScreen(img) #finds out the location of the specified button
    imgCenter = pg.center(imgLocation) #finds out the centre of the button
    return (imgCenter)

#finds out the search button and clicks on it
searchButton = button_location("search.png")
pg.moveTo(searchButton.x,searchButton.y,1)
pg.leftClick() 

#writes calculator in the search option of the search bar and opens it
time.sleep(0.5)
pg.typewrite("Calculator",0.1)
pg.press("Enter")

#performs a calculation
time.sleep(1)
pg.press("2")
pg.hotkey("shiftleft","8")
pg.press("2")
pg.press("=")