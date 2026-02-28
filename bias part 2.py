import cohere
import config
co=cohere.Client(config.COHERE_API_KEY)
def generate_response(prompt,temperature=0.3):
        try:
            response = co.chat(
                model="c4ai-aya-expanse-8b",
                message=prompt,
                temperature=temperature,
                max_tokens=800
        )
            return response.text.strip()
        except Exception as e:
              return f"erorr{e}"
def get_essay_details():
      ("hello i am your writting assistant")
      topic = input("Topic: ").strip()
      essay_type = input("Type: ").strip()
      length = input("Word Count: ").strip()
      audience = input("Target audience: ").strip()
      return topic, essay_type ,length ,audience 
def generate_essay(topic, essay_type ,length ,audience ):
    try:
        temp = float(input("Temperature(0.1 - 0.7)").strip())
    except:
        temp=0.3
    sections = {
    "Introduction": f"Write an introduction for a {essay_type} essay about {topic} in {length}. Audience: {audience}.",
    "Body": f"Write the body of a {essay_type} essay about {topic} for {audience}.",
    "Conclusion": f"Write a strong conclusion for a {essay_type} essay about {topic} for {audience}."
}
    for title,prompt in sections.items():
         print("Title")
         print(generate_response(prompt,temp))
def main():
     print("welcome to ai writting assistant")
     topic, essay_type ,length ,audience=get_essay_details()
     if topic and essay_type:
          generate_essay(topic, essay_type ,length ,audience)
     else:
          print("topic and essay type are required")
if __name__ == "__main__":
    main()