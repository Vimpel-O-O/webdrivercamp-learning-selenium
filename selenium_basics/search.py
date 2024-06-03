from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


PATH = "../chromedriver"
service = Service(PATH)
options = Options()

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.ebay.com/")

wait = WebDriverWait(driver, 10)
search = wait.until(expected_conditions.visibility_of_element_located(
    (By.XPATH, "//label[contains(text(), 'search')]/following-sibling::input[1]")))
search.click()

print(driver.current_url)

search.send_keys("women watch")
search_btn = driver.find_element(By.XPATH, "//input[@value='Search']")
search_btn.click()

result_vrfctn = driver.find_element(By.XPATH, "//span[contains(text(), 'women watch')]/parent::h1")
assert "women watch" in result_vrfctn.text, "Incorrect search result"

time.sleep(2)
driver.quit()

