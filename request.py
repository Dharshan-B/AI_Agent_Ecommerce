import requests

url = "http://localhost:8000/ask"
question = {"question": "Which product had the highest CPC?"}

response = requests.post(url, json=question)
print("Status:", response.status_code)
print("Response JSON:\n", response.json())
