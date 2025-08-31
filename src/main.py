import os
from offer_to_use_default_settings import offer_to_use_default_settings
from instantiate_chrome_driver import instantiate_chrome_driver
from use_default_address import get_collection_info_using_default_address
from get_postcode import get_postcode
from get_addresses_at_postcode import get_addresses
from get_specific_address_from_user import get_specific_address
from get_collection_info import get_collection_info_for_address
from offer_to_send_email import offer_to_send_email
from send_email import send_email


URL = ("https://webapps.sunderland.gov.uk/"
       "WEBAPPS/WSS/Sunderland_Portal/Forms/"
       "bindaychecker.aspx?ccp=true")
ADDRESS = os.getenv("DEFAULT_ADDRESS")


def main():
    response_to_default_settings_offer = offer_to_use_default_settings()
    driver = instantiate_chrome_driver()
    try:
        if response_to_default_settings_offer.lower() == "y":
            print("Using default settings:")
            info_for_user = get_collection_info_using_default_address(
                driver, URL)
            print(info_for_user)
            response_to_email_offer = offer_to_send_email()
            if response_to_email_offer.lower() == "y":
                send_email(ADDRESS, info_for_user)
        else:
            postcode = get_postcode()
            addresses = get_addresses(driver, URL, postcode)
            selected_address = get_specific_address(addresses)
            info_for_user = get_collection_info_for_address(
                driver, selected_address)
            print(info_for_user)
            response_to_email_offer = offer_to_send_email()
            if response_to_email_offer.lower() == "y":
                send_email(selected_address, info_for_user)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
