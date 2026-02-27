import cohere
import config
import time
co=cohere.Client(config.COHERE_API_KEY)
def generate_response(prompt,temperature=0.5,max_tokens=400):
        """generate ai response"""
        try:
            response = co.chat(
                model="c4ai-aya-expanse-8b",
                message=prompt,
                temperature=temperature,
                max_tokens=300
        )
            return response.text.strip()
        except Exception as e:
              return f"erorr{e}"
def bias_mitigation_activity():
    print("activit.....")
    prompt = input("enter a prompt").strip()
    if not prompt:
          print("error")
          return
    initial = generate_response(prompt)
    print("initial response",initial)
    neutral=input("rewrite in neutral form").strip()
    if neutral:
       improved = generate_response(neutral)
       print("\nNeutral AI Response:\n", improved)
    else:
       print("No neutral prompt entered.")
def token_limit_activity():
    print("\n=== TOKEN LIMIT ACTIVITY ===")
    long_prompt = input("Enter a long prompt: ").strip()
    if long_prompt:
        long_result = generate_response(long_prompt, max_tokens=800)
        preview = long_result[:500] + "..." if len(long_result) > 500 else long_result
        print("\nLong Prompt Response (Preview):\n", preview)
    else:
        print("Skipped long prompt.")
    short_prompt = input("enter condensed form").strip()
    if short_prompt:
        short_result=generate_response(short_prompt,max_tokens = 250)
        print("\nCondensed Prompt Response:\n", short_result)
    else:
        print("Skipped condensed prompt.")
def main():
    while True:
        print("\n=== AI PROMPT ENGINEERING PROJECT (Cohere) ===")
        print("1. Bias Mitigation")
        print("2. Token Limit Test")
        print("3. Exit")
        choice = input("Choose (1-3): ").strip()
        if choice == "1":
            bias_mitigation_activity()
        elif choice == "2":
            token_limit_activity()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    main()

