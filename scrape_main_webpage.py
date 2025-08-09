from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv


load_dotenv()

URL = ("https://webapps.sunderland.gov.uk/"
       "WEBAPPS/WSS/Sunderland_Portal/Forms/"
       "bindaychecker.aspx?ccp=true")

POSTCODE = os.getenv("POSTCODE")
def interact_with_webpage(url):
    options = Options()
    #options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    driver.get(url)
    time.sleep(0.5)
    postcode_input = driver.find_element(By.ID, "ContentPlaceHolder1_tbPostCode_controltext")
    postcode_input.send_keys(POSTCODE)
    postcode_input.submit()
    time.sleep(1)
    content = driver.page_source
    driver.quit()
    return content

if __name__ == "__main__":
    response = interact_with_webpage(URL)
    print(response if response else "Failed to retrieve the webpage.")