import cohere
import config
co = cohere.Client(config.COHERE_API_KEY)
def generate_response(prompt):
    try:
        response = co.chat(
            model="c4ai-aya-expanse-8b",
            message = prompt,
            temperature=0.7,
            max_tokens=2000
        )
        return response.text.strip()
    except Exception as e:
        return f" Error: {e}"
def prompt_engineering_project():
    print("=" * 60)
    print("REAL PROMPT ENGINEERING PROJECT (Cohere API)")
    print("Ask any question — get REAL AI response")
    print("=" * 60)
    user_prompt = input("enter your prompt")
    print("ai response"
          )
    print(generate_response(user_prompt))
if __name__ == "__main__":
    prompt_engineering_project()