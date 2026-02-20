import cohere
from config import COHERE_API_KEY
if not COHERE_API_KEY:
    print("error")
    exit()
co = cohere.Client(COHERE_API_KEY)
def generate_response(prompt,temperature=0.5):
        response = co.chat(
            model="c4ai-aya-expanse-8b",
            message=prompt,
            temperature=temperature,
            max_tokens=300
        )
        return response.text.strip()
def run_activity():
    print("welcome chose a theme")
    category=input(
         "enter here kindly you cat"
    ).strip()
    item=input(
         f"your{category} is this"
    ).strip()
    if not category or not item:
        print("❌ Please fill in both fields.")
        return
    zero_shot = f"Is {item} a {category}? Answer Yes or No."
    print("\n--- ZERO-SHOT LEARNING ---")
    print("Response:", generate_response(zero_shot, temperature=0.3))
    one_shot = f"""
Example:
Category: fruit
Item: apple
Answer: Yes, apple is a fruit.
Now try:
Category: {category}
Item: {item}
Answer:
"""
    print("\n--- ONE-SHOT LEARNING ---")
    print("Response:", generate_response(one_shot, temperature=0.3))
    few_shot = f"""
Example 1:
Category: fruit
Item: apple
Answer: Yes, apple is a fruit.

Example 2:
Category: animal
Item: dog
Answer: Yes, dog is an animal.
Now try:
Category: {category}
Item: {item}
Answer:
"""
    print("\n--- FEW-SHOT LEARNING ---")
    print("Response:", generate_response(few_shot, temperature=0.3))
    creative_prompt = f"""
Write a one-sentence story about the given word.
Example:
Word: moon
Story: The moon shined brightly in the night sky.
Word: {item}
Story:
"""
    print("\n--- CREATIVE TASK ---")
    print("Response:", generate_response(creative_prompt, temperature=0.7)) 
    print("\n--- REFLECTION QUESTIONS ---")
    print("1. How did zero-shot, one-shot, and few-shot differ?")
    print("2. Which one was most accurate?")
    print("3. How did examples help the AI?")
if __name__ == "__main__":
    run_activity()