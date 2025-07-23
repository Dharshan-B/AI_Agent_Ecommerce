import requests

url = "http://localhost:8000/ask"
question = {"question": "Calculate the RoAS (Return on Ad Spend)."}

response = requests.post(url, json=question)
print("Status:", response.status_code)
print("Response JSON:\n", response.json())