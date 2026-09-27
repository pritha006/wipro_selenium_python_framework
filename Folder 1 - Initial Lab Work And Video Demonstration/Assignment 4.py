from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

time.sleep(3)

print("=" * 60)
print("Assignment 4 - Child Nodes Using CSS")
print("=" * 60)
print("Page Title :", driver.title)
print("=" * 60)


print("\n1. Child Elements inside Date Picker Box\n")

child_elements = driver.find_elements(
    By.CSS_SELECTOR,
    "div.date-picker-box > *"
)

print("Total Child Elements :", len(child_elements))
print("-" * 60)

for index, element in enumerate(child_elements, start=1):
    print(f"Child {index} : {element.tag_name}")

time.sleep(2)


print("\n2. Start Date Field\n")

start_date = driver.find_element(
    By.CSS_SELECTOR,
    "div.date-picker-box > input#start-date"
)

start_date.send_keys("01-09-2026")

print("Start Date entered successfully.")

time.sleep(2)


print("\n3. End Date Field\n")

end_date = driver.find_element(
    By.CSS_SELECTOR,
    "div.date-picker-box > input#end-date"
)

end_date.send_keys("10-09-2026")

print("End Date entered successfully.")

time.sleep(2)


print("\n4. Separator Element\n")

separator = driver.find_element(
    By.CSS_SELECTOR,
    "div.date-picker-box > span.separator"
)

print("Separator Text :", separator.text)

time.sleep(2)


print("\n5. Submit Button\n")

submit_button = driver.find_element(
    By.CSS_SELECTOR,
    "div.date-picker-box > button.submit-btn"
)

print("Button Text :", submit_button.text)

submit_button.click()

print("Submit button clicked successfully.")

time.sleep(3)

driver.quit()

print("\n" + "=" * 60)
print("Assignment 4 completed successfully.")
print("=" * 60)