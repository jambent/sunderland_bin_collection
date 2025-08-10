from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
from dotenv import load_dotenv


load_dotenv()

URL = ("https://webapps.sunderland.gov.uk/"
       "WEBAPPS/WSS/Sunderland_Portal/Forms/"
       "bindaychecker.aspx?ccp=true")

POSTCODE = os.getenv("POSTCODE")
ADDRESS = os.getenv("ADDRESS")


def interact_with_webpage(url, postcode=POSTCODE, address=ADDRESS):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    driver.get(url)
    postcode_input = driver.find_element(
        By.ID, "ContentPlaceHolder1_tbPostCode_controltext")
    postcode_input.send_keys(POSTCODE)
    postcode_input.submit()
    driver.find_element(By.ID, "ContentPlaceHolder1_btnLLPG").click()
    select_element = driver.find_element(
        "id", "ContentPlaceHolder1_ddlAddresses")
    select = Select(select_element)
    select.select_by_visible_text(ADDRESS)
    household_waste_bin_message = driver.find_element(
        By.ID, "ContentPlaceHolder1_LabelHouseNext")
    household_waste_date = driver.find_element(
        By.ID, "ContentPlaceHolder1_LabelHouse")
    household_waste_bin_order = driver.find_element(
        By.ID, "ContentPlaceHolder1_LabelHouseTime")
    recycle_bin_message = driver.find_element(
        By.ID, "ContentPlaceHolder1_LabelBlueNext")
    recycle_date = driver.find_element(
        By.ID, "ContentPlaceHolder1_LabelRecycle")
    recycle_bin_order = driver.find_element(
        By.ID, "ContentPlaceHolder1_LabelHouseRec")
    print("\n")
    print(household_waste_bin_message.text)
    print(household_waste_date.text)
    print(household_waste_bin_order.text)
    print("\n")
    print(recycle_bin_message.text)
    print(recycle_date.text)
    print(recycle_bin_order.text)
    print("\n")
    # content = driver.page_source  # if html interrogation required
    driver.quit()


if __name__ == "__main__":
    response = interact_with_webpage(URL)
    # print(response if response else "Failed to retrieve the webpage.")
