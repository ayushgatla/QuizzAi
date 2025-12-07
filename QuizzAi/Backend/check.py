import requests

API_KEY = "sk-df27a61ec9f94071b7c73995476ff5a4" # <= put your key here

if API_KEY.strip() == "" or "YOUR_" in API_KEY:
    raise ValueError("Bro put your actual DeepSeek API key in the variable.")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

url = "https://api.deepseek.com/v1/balance"

try:
    resp = requests.get(url, headers=headers)
    print("Status Code:", resp.status_code)
    print("Balance Info:", resp.json())
except Exception as e:
    print("Error checking balance:", e)
