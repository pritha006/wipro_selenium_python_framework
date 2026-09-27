from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# -------------------------------------------------
# ASSIGNMENT 3
# CSS SELECTOR CHALLENGE
# -------------------------------------------------

# Launch Chrome Browser
driver = webdriver.Chrome()

# Maximize Browser Window
driver.maximize_window()

# Open Website
driver.get("https://testautomationpractice.blogspot.com/")

time.sleep(3)

print("=" * 60)
print("Assignment 3 - CSS Selector Challenge")
print("=" * 60)
print("Page Title :", driver.title)
print("=" * 60)

# -------------------------------------------------
# 1. CSS Selector using ID
# -------------------------------------------------

print("\n1. CSS Selector using ID\n")

name_field = driver.find_element(By.CSS_SELECTOR, "#name")
name_field.send_keys("User")

print("Successfully located Name field using CSS ID Selector (#name)")

time.sleep(2)

# -------------------------------------------------
# 2. CSS Selector using Class
# -------------------------------------------------

print("\n2. CSS Selector using Class\n")

email_field = driver.find_element(By.CSS_SELECTOR, ".form-control")
email_field.clear()
email_field.send_keys("sample@test.com")

print("Successfully located an element using CSS Class Selector (.form-control)")

time.sleep(2)

# -------------------------------------------------
# 3. CSS Selector using Attribute
# -------------------------------------------------

print("\n3. CSS Selector using Attribute\n")

male_radio = driver.find_element(By.CSS_SELECTOR, "input[id='male']")
male_radio.click()

print("Successfully located Male radio button using Attribute Selector")

time.sleep(2)

# -------------------------------------------------
# 4. CSS Wildcard Selector - Starts With (^=)
# -------------------------------------------------

print("\n4. CSS Wildcard - Starts With (^=)\n")

start_elements = driver.find_elements(By.CSS_SELECTOR, "input[id^='input']")

print("Elements whose ID starts with 'input':", len(start_elements))

for index, element in enumerate(start_elements, start=1):
    print(f"{index}. {element.get_attribute('id')}")

time.sleep(2)

# -------------------------------------------------
# 5. CSS Wildcard Selector - Ends With ($=)
# -------------------------------------------------

print("\n5. CSS Wildcard - Ends With ($=)\n")

end_elements = driver.find_elements(By.CSS_SELECTOR, "input[id$='date']")

print("Elements whose ID ends with 'date':", len(end_elements))

for index, element in enumerate(end_elements, start=1):
    print(f"{index}. {element.get_attribute('id')}")

time.sleep(2)

# -------------------------------------------------
# 6. CSS Wildcard Selector - Contains (*=)
# -------------------------------------------------

print("\n6. CSS Wildcard - Contains (*=)\n")

contain_elements = driver.find_elements(By.CSS_SELECTOR, "input[id*='date']")

print("Elements whose ID contains 'date':", len(contain_elements))

for index, element in enumerate(contain_elements, start=1):
    print(f"{index}. {element.get_attribute('id')}")

time.sleep(2)

# -------------------------------------------------
# CLOSE BROWSER
# -------------------------------------------------

driver.quit()

print("\n" + "=" * 60)
print("Assignment 3 completed successfully.")
print("=" * 60)