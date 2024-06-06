from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Yashwanth")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("kumar")


email_address = driver.find_element(By.NAME, value="email")
email_address.send_keys("yashwanth@gmail.com")

sign_up = driver.find_element(By.CSS_SELECTOR, value="form button")
sign_up.click()



