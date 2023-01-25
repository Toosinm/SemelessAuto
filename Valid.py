from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start the browser
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://the-internet.herokuapp.com/")

# Click on the "Form Authentication" link
driver.find_element_by_link_text("Form Authentication").click()

# Find the username and password fields and enter the credentials
username_field = driver.find_element_by_id("username")
password_field = driver.find_element_by_id("password")
username_field.send_keys("tomsmith")
password_field.send_keys("SuperSecretPassword!")

# Click on the login button
driver.find_element_by_class_name("radius").click()

# Wait for the success message to appear
success_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "flash")))

# Assert that the success message is correct
assert success_message.text == "You logged into a secure area!"

# Close the browser
driver.quit()