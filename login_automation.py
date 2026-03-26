from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)

driver.get("https://the-internet.herokuapp.com/login")

# VALID LOGIN TEST
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

success_text = wait.until(EC.presence_of_element_located((By.ID, "flash"))).text
print("Valid Login Test:", "PASS" if "You logged into a secure area!" in success_text else "FAIL")

driver.get("https://the-internet.herokuapp.com/login")

# INVALID LOGIN TEST
driver.find_element(By.ID, "username").send_keys("wronguser")
driver.find_element(By.ID, "password").send_keys("wrongpass")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

error_text = wait.until(EC.presence_of_element_located((By.ID, "flash"))).text
print("Invalid Login Test:", "PASS" if "Your username is invalid!" in error_text else "FAIL")

driver.quit()
