from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import var_storage

# ChromeWebDriver setup and open link
PATH = "../chromedriver"
service = Service(PATH)
options = Options()

driver = webdriver.Chrome(service=service, options=options)
driver.get(var_storage.ebay_watches_url)
wait = WebDriverWait(driver, 10)


# open in new tab and verify title and price
def itemFilterVer(model_type, item_path, item_price_path, keyword=""):
    model_filter = wait.until(EC.visibility_of_element_located((By.XPATH, model_type)))
    model_filter.click()
    current_filter_window = driver.current_window_handle
    item = driver.find_element(By.XPATH, item_path)
    item_price = driver.find_element(By.XPATH, item_price_path)
    item.click()
    item_title_text = item.text
    item_price_text = item_price.text
    if "to" in item_price_text:
        item_price_text = item_price_text[1:6]
    for handle in driver.window_handles:
        if handle != current_filter_window:
            driver.switch_to.window(handle)
            break
    new_tab_title = driver.find_element(By.XPATH, var_storage.newTab_title)
    new_tab_price = driver.find_element(By.XPATH, var_storage.newTab_price)
    if item_title_text == new_tab_title.text and item_price_text in new_tab_price.text:
        print(f"Item is {keyword}")
    else:
        print(f"Item is NOT {keyword}")
    driver.close()
    driver.switch_to.window(current_filter_window)
    model_filter = wait.until(EC.visibility_of_element_located((By.XPATH, model_type)))
    model_filter.click()


# check 2 first Rolex items
itemFilterVer(var_storage.rolex_checkbox, var_storage.rolex_item_1, var_storage.rolex_item_1_price, "Rolex")
itemFilterVer(var_storage.rolex_checkbox, var_storage.rolex_item_2, var_storage.rolex_item_2_price, "Rolex")

# check 2 first Casio items
itemFilterVer(var_storage.casio_checkbox, var_storage.casio_item_1, var_storage.casio_item_1_price, "Casio")
itemFilterVer(var_storage.casio_checkbox, var_storage.casio_item_2, var_storage.casio_item_2_price, "Casio")

driver.quit()
