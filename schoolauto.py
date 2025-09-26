# Import webdriver from selenium and following modules #
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
# create variables for username/s and password/s strings #
usernamestr1=""
passwordstr1=""
# Stating which browser should be opened #
browser=webdriver.Chrome()
# Stating which url to open #
browser.get((""))
# scrapeing the html to find correct elements by either id, name, xpath, css selector #
# Find username box using css selector and send the username in the variable usernamestr1 #
username=browser.find_element_by_css_selector("input[type=\"text\" i]")
username.send_keys(usernamestr1)
# Find password box ussing css selector and send the password in the variable passwordstr1 #
password=browser.find_elements_by_css_selector("input[type=\"password\" i]")
password.send_keys(passwordstr1)
# Find login button and send a click #
login=browser.find_element_by_css_selector("input[type=\"submit\" i]")
login.click()
# Open new tab test

#browser.execute_script("window.open('');")

#usernamestr2=("")
#passwordstr2=("")




#usernamestr2=browser.find_element_by_css_selector("input[type=\"email\" i]")
#usernamestr2.send_keys(usernamestr2)
#nextbutton=browser.find_element_by_css_selector("input[type=\"submit\"]")
#nextbutton.click()
#password2=WebDriverWait(browser, 15).until(
#    expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input[type=\"password\" i]")))
#password2.send_keys(passwordstr2)
#signinbutton=browser.find_element_by_css_selector("input[type=\"submit\" i]")
#signinbutton.click()
