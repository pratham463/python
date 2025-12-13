import requests
BASE_URL = "https://uselessfacts.jsph.pl/random.json?language=en"
def get_fact(category):   
    try:
        url = BASE_URL.format(category)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"\n {data['text']}\n")
        else:
            print(" Category not found or API error.\n")
    except:
        print(" Failed to fetch fact.\n")
categories = ["Technology", "Science", "Random", "History", "Food", "Animals"]
print("🧠 Useless Facts Explorer")
print("Select a category or type 'q' to quit.\n")
for i, c in enumerate(categories, 1):
    print(f"{i}. {c}")
while True:
    choice = input("\nEnter category number: ")
    if choice.lower() == "q":
        print("Goodbye! 👋")
        break

    if choice.isdigit() and 1 <= int(choice) <= len(categories):
        selected = categories[int(choice) - 1]
        print(f"\nFetching {selected} fact...")
        get_fact(selected)
    else:
        print("⚠️ Invalid choice. Try again.")