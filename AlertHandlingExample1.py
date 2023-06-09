import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s= Service("//Users//mac//Downloads//chromedriver_mac_arm64")

# create webdriver object
driver = webdriver.Chrome(service=s)

current_url = driver.get("http://demo.guru99.com/test/delete_customer.php")
driver.maximize_window()

# Wait up to 10 seconds for the element with name "cusid" to be visible,
# then enter the customer ID "53920"
customer_id = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "cusid"))).send_keys("53920")

# Find the submit button by name and submit the form
driver.find_element(By.NAME, "submit").submit()

# Switch the driver's focus to the alert dialog
obj = driver.switch_to.alert

# Get the text of the alert message
msg = obj.text
print("Alert shows the following message: " + msg)

# Accept the alert by clicking the OK button
obj.accept()

# Pause execution for 2 seconds (not necessary, just an example)
time.sleep(2)

# Wait up to 10 seconds for the element with name "cusid" to be visible again,
# then enter the customer ID "53920" (as an example)
customer_id = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "cusid"))).send_keys("53920")

# Find the submit button by name and submit the form again
driver.find_element(By.NAME, "submit").submit()

# Switch the driver's focus to the alert dialog again
obj = driver.switch_to.alert

# Get the text of the second alert message
msg = obj.text
print("Alert shows the following message: " + msg)

# Dismiss the alert by clicking the Cancel button
obj.dismiss()
