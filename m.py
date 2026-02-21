import cohere
import config
import time
co = cohere.Client(config.COHERE_API_KEY)
def get_ai_response(prompt,temp=0.3):
    """generating ai response"""
    try:
        res=co.chat(
            model="c4ai-aya-expanse-8b",
            message=prompt,
            temperature=temp,
            max_tokens=300
        )
        return res.text.strip()
    except Exception as e:
    
        return f"error{e}"
def feedback_activity():
    print("feed back learning")
    prompt = input("enter:")
    ans = get_ai_response(prompt)
    print("\nAI Response:\n", ans)
    rating = input("\nRate (1-5): ")
    feedback = input("Give feedback: ")
    improved = ans + "\n[Improved using feedback: " + feedback + "]"
    print("\nImproved Response:\n", improved)
def role_activity():
    print("\n=== ROLE-BASED PROMPTS ===")
    category = input("Enter category: ")
    topic = input("Enter topic: ")
    teacher = f"You are a teacher. Explain {topic} simply."
    expert = f"You are an expert in {category}. Explain {topic} in detail."
    print("\n--- Teacher View ---")
    print(get_ai_response(teacher))
    time.sleep(1)
    print("\n--- Expert View ---")
    print(get_ai_response(expert))
def temperature_activity():
    print("\n=== TEMPERATURE EXPERIMENT ===")
    prompt = input("Enter creative prompt: ")
    for t in [0.1, 0.5, 0.9]:
        print(f"\n--- Temperature {t} ---")
        print(get_ai_response(prompt, temp=t))
        time.sleep(1)
def main():
    while True:
        print("\n=== AI PROMPT ENGINEERING PROJECT ===")
        print("1. Feedback Learning")
        print("2. Role-Based Prompts")
        print("3. temperature test")
        print("4. exit")
        choice = input("chose{1-4}")
        if choice=="1":
            feedback_activity()
        elif choice=="2":
            role_activity()
        elif choice=="3":
            temperature_activity()
        elif choice=="4":
            print("exit")
            break
        else:
            print("try again")
if __name__ == "__main__":
    main()