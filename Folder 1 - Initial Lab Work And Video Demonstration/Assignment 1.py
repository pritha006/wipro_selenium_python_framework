from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(3)

# webpage locator using ID
print("1. Demonstrating ID Locator")

name_field = driver.find_element(By.ID, "name")
name_field.send_keys("User")

print("ID locator successfully located the Name field.")
time.sleep(2)

# webpage locator using name
print("2. Demonstrating Name Locator")
gender_radio = driver.find_element(By.NAME, "gender")

gender_radio.click()
print("Name locator successfully located the Gender radio button.")
time.sleep(2)

# webpage locator using class name
print("3. Demonstrating Class Name Locator")
class_element = driver.find_element(
    By.CLASS_NAME,
    "form-control"
)
print("Class Name locator successfully located the element.")
time.sleep(2)

# webpage locator using tag name
print("4. Demonstrating Tag Name Locator")
inputs=driver.find_elements(
    By.TAG_NAME,
    "input"
)
print("Number of input elements found:",len(inputs))
time.sleep(2)

# webpage locator using link text
print("5. Demonstrating Link Text Locator")
link=driver.find_element(
    By.LINK_TEXT,
    "Apple"
)
print("Link found using Link Text:",link.text)
time.sleep(2)
print("Assignment 1 completed successfully.")

