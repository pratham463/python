import requests
url = "https://sentim-api.onrender.com/api/v1/"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}
test_sentences = {
    "Positive": "I love coding and learning new things!",
    "Negative": "I hate coding and learning new things!",
    "Neutral": "I dont hate or like coding and learning new things!"
}
print("SENTIMENT ANALYSIS TESTING\n")

for expected, text in test_sentences.items():
    data = {"text": text}

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()
        sentiment = result["result"]["type"]
        polarity = result["result"]["polarity"]
        print(f"Input Text     : {text}")
        print(f"Expected Type  : {expected}")
        print(f"Predicted Type : {sentiment}")
        print(f"Polarity Score : {polarity}")
        print("-" * 50)

    except Exception as e:
        print("Error occurred:", e)