
TOKEN = "8502116769:AAFQlDAm2kF4k2lRJJG6B95uxxGPTynRndw"
CHAT_ID = "5152806937"
PRODUCT_URL = "https://www.myntra.com/gold-coin/kalyan+jewellers/kalyan-jewellers-24k-999-purity-lord-ganesh-gold-coin-2-gms/31416938/buy"
import os
import requests
import time

# Use environment variables for security
TOKEN = os.getenv("TG_TOKEN")
CHAT_ID = os.getenv("TG_CHAT_ID")
PRODUCT_URL = "https://www.myntra.com/gold-coin/kalyan+jewellers/kalyan-jewellers-24k-999-purity-lord-ganesh-gold-coin-2-gms/31416938/buy"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
}

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, json=payload)

def check_for_blinkdeal():
    try:
        response = requests.get(PRODUCT_URL, headers=HEADERS, timeout=20)
        if "BLINKDEAL" in response.text.upper():
            send_telegram(f"🚨 BLINKDEAL DETECTED!\nLink: {PRODUCT_URL}")
            print("Deal found!")
        else:
            print("No deal yet.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # The script runs ONCE and exits. GitHub Actions will handle the repetition.
    check_for_blinkdeal()