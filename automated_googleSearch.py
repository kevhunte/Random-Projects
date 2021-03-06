#usr/bin/python
import sys, os, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
"""
    This project will be used to automate google searches, based on a search provided at the command line.
"""
def slowScroll(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4);")
    time.sleep(0.5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
    time.sleep(0.5)
    driver.execute_script("window.scrollTo(0, 3*document.body.scrollHeight/4);")
    time.sleep(0.5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

browser = webdriver.Chrome()
browser.get('https://google.com')

search_bar = browser.find_element_by_name('q')

if len(sys.argv) > 1:
    search_param = sys.argv[1]
    if('+' in search_param):
        words = search_param.split('+')
        search_param = ''
        for w in words:
            search_param += w+' '           #reformat string without + symbols
else:
    search_param = 'random search'

search_bar.send_keys(search_param)
search_bar.send_keys(Keys.RETURN)
#controls for inside of webpage
time.sleep(0.5)                             #give time to properly load
webpages = browser.find_elements_by_partial_link_text('https://')     #list of webpages
index = 0
num_iters = range(len(webpages))

for webpage in num_iters:
    #print("webpage num: "+str(webpage))    #debugging
    if(webpage >= len(webpages)):           #be careful, webpages length dynamically changes
        browser.quit()
        break
    webpages[webpage].click()
    time.sleep(1)                           #blocking function. Wait to load
#browser.execute_script("window.scrollTo(0, document.body.scrollHeight/2);") #make scroll speed slower
    slowScroll(browser)
    time.sleep(2)
    browser.back()
    time.sleep(1)                           #wait for page to load
    webpages = browser.find_elements_by_partial_link_text('https://')   #regen elements, fixes problems

print("loop finished")
time.sleep(3)           #show for three seconds before closing
browser.quit()
print('closed with no issues')
