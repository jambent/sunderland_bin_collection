from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


URL = ("https://webapps.sunderland.gov.uk/"
       "WEBAPPS/WSS/Sunderland_Portal/Forms/"
       "bindaychecker.aspx?ccp=true")


def get_addresses(driver, postcode):
    driver.get(URL)
    postcode_input = driver.find_element(
        By.ID, "ContentPlaceHolder1_tbPostCode_controltext")
    postcode_input.send_keys(postcode)
    postcode_input.submit()
    driver.find_element(By.ID, "ContentPlaceHolder1_btnLLPG").click()
    select_element = driver.find_element(
        "id", "ContentPlaceHolder1_ddlAddresses")
