import requests
import json

API_KEY = "AIzaSyBy9rxI02eVTQ2JV70-49a_2WyECcZT9Ho"  

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

headers = {
    "Content-Type": "application/json",
}

data = {
    "contents": [
        {
            "parts": [
                {
                    "text": "Explain how AI works in a few words"
                }
            ]
        }
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(data))
result = response.json()

print("Response:", result["candidates"][0]["content"]["parts"][0]["text"])
