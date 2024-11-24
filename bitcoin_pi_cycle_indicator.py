import requests
import pandas as pd
from datetime import datetime, timedelta
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# API endpoint for Bitcoin price data
PRICE_URL = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"

def get_bitcoin_data(days=365):
    params = {
        "vs_currency": "usd",
        "days": days,
        "interval": "daily"
    }
    try:
        response = requests.get(PRICE_URL, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        if "prices" not in data:
            raise KeyError("'prices' key not found in API response")
        df = pd.DataFrame(data["prices"], columns=["timestamp", "price"])
        df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
        df = df.set_index("date")
        return df[["price"]]
    except requests.RequestException as e:
        print(f"Error fetching data from API: {e}")
        print(f"Response content: {response.text}")
        raise
    except (KeyError, ValueError) as e:
        print(f"Error processing API response: {e}")
        print(f"Response content: {response.text}")
        raise

def calculate_pi_cycle_indicator(df):
    df["111ma"] = df["price"].rolling(window=111).mean()
    df["350ma_x2"] = df["price"].rolling(window=350).mean() * 2
    return df

def check_pi_cycle_top(df):
    last_row = df.iloc[-1]
    return last_row["111ma"] > last_row["350ma_x2"]

def send_email(subject, body, to_email):
    # Replace these with your email configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "YOUR_GMAIL_ADDRESS@gmail.com"  # Replace with your Gmail address
    smtp_password = "YOUR_APP_PASSWORD"  # Replace with your App Password
    from_email = smtp_username

    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        print(f"Attempting to send email to {to_email}")
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            print("Connected to SMTP server")
            server.starttls()
            print("Started TLS")
            print(f"Attempting to login with username: {smtp_username}")
            server.login(smtp_username, smtp_password)
            print("Logged in successfully")
            server.send_message(msg)
            print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")
        raise

# Update the recipient email address here
recipient_email = "YOUR_RECIPIENT_EMAIL@example.com"  # Replace with the email where you want to receive alerts

def main():
    first_run = True
    while True:
        try:
            print(f"Fetching Bitcoin data at {datetime.now()}")
            df = get_bitcoin_data()
            print("Data fetched successfully. Calculating Pi Cycle Indicator.")
            df = calculate_pi_cycle_indicator(df)
            is_top = check_pi_cycle_top(df)

            if first_run:
                subject = "Bitcoin Pi Cycle Top Indicator Script Started"
                body = f"""
The Bitcoin Pi Cycle Top Indicator script has started running at {datetime.now()}.

This script will continuously monitor the Bitcoin price and check for a Pi Cycle Top indicator.

If a Pi Cycle Top is detected, you will receive an email alert similar to this:

Subject: Bitcoin Pi Cycle Top Indicator Alert
Body: A potential Bitcoin market top has been detected by the Pi Cycle Top Indicator at {datetime.now()}.
Current Bitcoin price: $XX,XXX.XX
111-day Moving Average: $XX,XXX.XX
350-day Moving Average (x2): $XX,XXX.XX

Please note that this is just one indicator and should not be used as the sole basis for investment decisions.

The script will continue running and check for updates every 5 minutes.
"""
                send_email(subject, body, recipient_email)
                print(f"Initial startup email sent on {datetime.now()}")
                first_run = False
            elif is_top:
                subject = "Bitcoin Pi Cycle Top Indicator Alert"
                body = f"A potential Bitcoin market top has been detected by the Pi Cycle Top Indicator at {datetime.now()}."
                send_email(subject, body, recipient_email)
                print(f"Pi Cycle Top alert sent on {datetime.now()}")
            else:
                print(f"No Pi Cycle Top detected at {datetime.now()}")

            print("Waiting for 5 minutes before next check.")
            time.sleep(300)  # Wait for 5 minutes instead of 24 hours for testing

        except Exception as e:
            print(f"An error occurred at {datetime.now()}: {e}")
            print("Waiting for 1 minute before retrying.")
            time.sleep(60)  # Wait for 1 minute before retrying if there's an error

if __name__ == "__main__":
    main()