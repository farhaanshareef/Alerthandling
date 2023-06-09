import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


s= Service("//Users//mac//Downloads//chromedriver_mac_arm64")

# create webdriver object
driver = webdriver.Chrome(service=s)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()

WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "name"))).send_keys("Farhan")
driver.find_element(By.ID, "alertbtn").click()

obj = driver.switch_to.alert

msg = obj.text
print("Alert shows following message: " + msg)
expected_text= "Hello Farhan, share this practice page and share your knowledge"
assert msg==expected_text, f"Alert message is different Expected {expected_text} got {msg}"

time.sleep(2)

obj.accept()

time.sleep(2)

username = driver.find_element(By.ID, "name").send_keys("Farhan")
driver.find_element(By.ID, "confirmbtn").click()

obj = driver.switch_to.alert

msg = obj.text
print("Alert shows following message: " + msg)
expected_text= "Hello Farhan, Are you sure you want to confirm?"
assert msg==expected_text, f"Alert message is different Expected {expected_text} got {msg}"

time.sleep(2)

obj.dismiss()

print("Test case completed successfully")


