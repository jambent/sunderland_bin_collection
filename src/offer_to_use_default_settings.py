def offer_to_use_default_settings():
    response = input(
        "Would you like to use your stored address details? (y/n): ")
    while response.lower() not in ["y", "n"]:
        response = input("Please enter 'y' or 'n': ")
    return response
    if response.lower() == "y":
        print("Using default settings:")
    else:
        print("Please provide your custom settings.")
