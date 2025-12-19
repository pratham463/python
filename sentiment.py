import random

def classify_text(text):

    api_response = {
        "positive": round(random.uniform(0.6, 0.9), 2),
        "negative": round(random.uniform(0.1, 0.4), 2)
    }
    sentiment = max(api_response, key=api_response.get)
    return sentiment, api_response
if __name__ == "__main__":
    text = "I love learning artificial intelligence"
    sentiment, scores = classify_text(text)
    print("Sentiment:", sentiment)
    print("Scores:", scores)