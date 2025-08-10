import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


load_dotenv()

URL = ("https://webapps.sunderland.gov.uk/"
       "WEBAPPS/WSS/Sunderland_Portal/Forms/"
       "bindaychecker.aspx?ccp=true")

POSTCODE = os.getenv("DEFAULT_POSTCODE")
ADDRESS = os.getenv("DEFAULT_ADDRESS")


def get_collection_dates_using_default_address(driver):
    driver.get(URL)
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
    return "\n\n".join(["\n".join([household_waste_bin_message.text,
                                   household_waste_date.text,
                                   household_waste_bin_order.text]),
                        "\n".join([recycle_bin_message.text,
                                   recycle_date.text,
                                   recycle_bin_order.text])])
