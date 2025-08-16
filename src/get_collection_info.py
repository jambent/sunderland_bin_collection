from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def get_collection_info_for_address(driver, address):

    select_element = driver.find_element(
        By.ID, "ContentPlaceHolder1_ddlAddresses")
    select = Select(select_element)
    select.select_by_visible_text(address)
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
