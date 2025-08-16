from selenium.webdriver.common.by import By


def get_addresses(driver, url, postcode):
    driver.get(url)
    postcode_input = driver.find_element(
        By.ID, "ContentPlaceHolder1_tbPostCode_controltext")
    postcode_input.send_keys(postcode)
    postcode_input.submit()
    driver.find_element(By.ID, "ContentPlaceHolder1_btnLLPG").click()
    select_element = driver.find_element(By.ID,
                                         "ContentPlaceHolder1_ddlAddresses")
    address_elements = select_element.find_elements(By.TAG_NAME, "option")
    address_values = [address.text for index, address
                      in enumerate(address_elements) if index > 0]
    return address_values
    # return driver.page_source
