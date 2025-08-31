# Sunderland Bin Collection
Sunderland Council does not have an API for public use in order to obtain details regarding bin collection dates.  This program uses Selenium to programatically interact with the relevant webpage on their website (https://webapps.sunderland.gov.uk/WEBAPPS/WSS/Sunderland_Portal/Forms/bindaychecker.aspx?ccp=true).  It returns the next household waste and recycling dates for either a default address or an address selected by the user after a postcode is input.  An email can optionally be sent to the user with the same information.

## Setup
To install the program's dependencies into your virtual environment:
```
$ pip install -r requirements.txt
```
or if using uv:
```
$ uv pip install -r requirements.txt
```

The program relies on the user having
i) a gmail account with 2-step verification (required for ii), below)
ii) an associated gmail app password

A .env file should be created locally containing the following information:
```
DEFAULT_POSTCODE="SRX XXX"
DEFAULT_ADDRESS="XXXXXXXXXXXXXXXXXXXXX"  (Has to match website format, exactly)
SMTP_SERVER="smtp.gmail.com"
RECIPIENT_EMAIL_ADDRESS="XXXXXXXXXXXXXXXX"
SENDER_GMAIL_ADDRESS = "XXXXX@gmail.com"
PORT = "465"
GMAIL_APP_PASSWORD = "XXXXXXXXXXXXXXXX"
```

## Usage
To run:
```
$ python ./src/main.py
```
or if using uv:
```
$ uv run ./src/main.py
```


