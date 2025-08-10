from offer_to_use_default_settings import offer_to_use_default_settings
from instantiate_chrome_driver import instantiate_chrome_driver
from use_default_address import get_collection_dates_using_default_address
from get_postcode import get_postcode
from get_addresses_at_postcode import get_addresses


def main():
    response_to_default_settings_offer = offer_to_use_default_settings()
    driver = instantiate_chrome_driver()
    try:
        if response_to_default_settings_offer.lower() == "y":
            print("Using default settings:")
            info_for_user = get_collection_dates_using_default_address(driver)
            print(info_for_user)
        else:
            postcode = get_postcode()
            # For further development:
            addresses = get_addresses(driver, postcode)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
