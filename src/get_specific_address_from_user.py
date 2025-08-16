def get_specific_address(addresses):
    print("These are the addresses at this postcode:")
    for index, address in enumerate(addresses, start=1):
        if len(str(index)) == 1:
            print(f"\033[94m({index})\033[0m   {address}")
        else:
            print(f"\033[94m({index})\033[0m  {address}")
    address_number = input(
        "Please enter the number corresponding to your address, "
        "and then press Enter\n")
    number_to_address_mapping = {
        str(index): address for index,
        address in enumerate(
            addresses,
            start=1)}
    while address_number not in number_to_address_mapping:
        address_number = input(
            "Invalid input. Please enter a valid number "
            "corresponding to your address:\n")
    return number_to_address_mapping.get(address_number)
