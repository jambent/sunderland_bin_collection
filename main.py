from get_user_details import get_user_details


def main():
    postcode, email_address = get_user_details()
    print(f"Postcode: {postcode}")
    print(f"Email Address: {email_address}")


if __name__ == "__main__":
    main()
