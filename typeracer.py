from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from random import randint

#Set minimum WPM required

min_wpm = 60

#Open Chrome

driver = webdriver.Chrome(executable_path="chromedriver.exe")

# Enter the URL
# Start Race
# Press the enter key when the race has started, when the program is in the waiting state

while(1):
    text = ''
    k = input("waiting")
   
    a = driver.find_elements_by_xpath("//span[@unselectable='on']")

    for i in a:
        text = text + i.get_attribute('innerHTML')
    print(text)

    text.replace("\\","")
    if text[-1] != '.' or text[-1] != '!' or text[-1] != '?':
        text = text + ' '
    time.sleep(1)



    print("Typing text")
    for letter in text:
            delay = randint(1,100)
            try:
                driver.find_element_by_xpath("//input[@autocorrect='off']").send_keys(letter)
            except:
                break
            time.sleep((delay/100)*(60/(5*min_wpm)))

