import requests
url = "https://sentim-api.onrender.com/api/v1/"
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}
data = {"text": "I love coding!"}
response = requests.post(url, headers=headers, json=data)
print(response.json())