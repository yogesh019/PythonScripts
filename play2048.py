import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser=webdriver.Chrome()
browser.get("https://gabrielecirulli.github.io/2048/")
flag=True
print("Enter key strokes on the terminal(Left:A,Up:W,Right:D,Down:S,Quit:Q):")
body_el=browser.find_element_by_tag_name("body")
el=browser.find_element_by_class_name("game-message")

while el.is_displayed()==False:
    os.system("clear")
    x=input()
    if x=='A' or x=='a':
        body_el.send_keys(Keys.LEFT)
    if x=='W'or x=='w':
        body_el.send_keys(Keys.UP)
    if x=='D'or x=='d':
        body_el.send_keys(Keys.RIGHT)

    if x=='S'or x=='s':
        body_el.send_keys(Keys.DOWN)
    
    if x=='Q'or x=='q':
        browser.close()
        break
        


