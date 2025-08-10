from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def instantiate_chrome_driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    return driver
