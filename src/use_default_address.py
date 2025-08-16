import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from get_collection_info import get_collection_info_for_address


load_dotenv()

POSTCODE = os.getenv("DEFAULT_POSTCODE")
ADDRESS = os.getenv("DEFAULT_ADDRESS")


def get_collection_info_using_default_address(driver, url):
    driver.get(url)
    postcode_input = driver.find_element(
        By.ID, "ContentPlaceHolder1_tbPostCode_controltext")
    postcode_input.send_keys(POSTCODE)
    postcode_input.submit()
    driver.find_element(By.ID, "ContentPlaceHolder1_btnLLPG").click()
    return get_collection_info_for_address(driver, ADDRESS)
