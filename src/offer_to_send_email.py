def offer_to_send_email():
    response = input(
        "\nWould you like this to be emailed to you? (y/n): ")
    while response.lower() not in ["y", "n"]:
        response = input("Please enter 'y' or 'n': ")
    return response
