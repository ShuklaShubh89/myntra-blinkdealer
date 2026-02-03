import os
import requests
import time
import random

# CONFIGURATION
TOKEN = os.getenv("TG_TOKEN")
CHAT_ID = os.getenv("TG_CHAT_ID")
PRODUCT_URL = "https://www.myntra.com/gold-coin/kalyan+jewellers/kalyan-jewellers-24k-999-purity-lord-ganesh-gold-coin-2-gms/31416938/buy"

# Total time this script will stay "awake" per run (in seconds)
# 600 seconds = 10 minutes of continuous monitoring
MONITOR_DURATION = 600 
CHECK_INTERVAL = 30  # Check every 30 seconds

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
}

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, json=payload, timeout=10)
    except Exception as e:
        print(f"Telegram failed: {e}")

def check_for_blinkdeal():
    try:
        response = requests.get(PRODUCT_URL, headers=HEADERS, timeout=15)
        if "BLINKDEAL" in response.text.upper():
            return True
        return False
    except Exception as e:
        print(f"Request error: {e}")
        return False

if __name__ == "__main__":
    start_time = time.time()
    print(f"Starting 10-minute burst monitor at {time.strftime('%H:%M:%S')}")
    
    while (time.time() - start_time) < MONITOR_DURATION:
        if check_for_blinkdeal():
            print("🎯 BLINKDEAL DETECTED!")
            send_telegram(f"🚨 QUICK! BLINKDEAL LIVE!\nLink: {PRODUCT_URL}")
            # If found, wait 5 mins to avoid spamming 10 notifications
            time.sleep(300) 
        else:
            print(f"[{time.strftime('%H:%M:%S')}] No deal yet...")
            time.sleep(CHECK_INTERVAL)
            
    print("Monitor duration finished. Action will restart on next cron schedule.")