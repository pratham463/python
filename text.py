import requests
from requests.auth import HTTPBasicAuth
from PIL import Image
import os
from colorama import init, Fore, Style
from config import HF_API_KEY
init(autoreset=True)
API_KEY = ""
API_SECRET = ""
IMAGGA_URL = "https://api.imagga.com/v2/tags"


def truncate_text(text, word_limit):
    words = text.split()
    return " ".join(words[:word_limit])


def get_image_tags(image_path, limit=10):
    with open(image_path, "rb") as img:
        response = requests.post(
            IMAGGA_URL,
            auth=HTTPBasicAuth(API_KEY, API_SECRET),
            files={"image": img}
        )

    data = response.json()
    tags=data.get("result", {}).get("tags", [])
    return [tag["tag"]["en"] for tag in tags[:limit]]
def generate_caption (tags):
    sentence = (
        f"This image shows {tags[0]}. "
        f"It includes elements such as {', '.join(tags[1:6])}. "
        f"The scene appears visually clear and well composed."
    )
    return truncate_text(sentence, 30)
def generate_summary(tags):
    sentence = (
                f"The image primarily features {tags[0]}. "
        f"Other visible elements include {', '.join(tags[1:7])}. "
        f"The objects are clearly distinguishable and form a meaningful scene. "
        f"The image provides a simple yet informative visual representation."
    )
def print_menu():
    print(f"""{Style.BRIGHT}{Fore.GREEN}
==============IMAGE TO TEXT CONVERSION================
          1.5 words
          2.30 words
          3.50 words
          5.exit
=====================================================
""")
def main():
    Image_path = input(f"{Fore.CYAN} enter the path of the image"
                       )
    if not os.path.exists(Image_path):
        print(f"file does not exists  ")
        return
    try:
        image = Image.open(Image_path)
    except Exception as e:
        print(f"{Fore.RED}Failed to open image: {e}")
        return

    basic_caption = generate_caption(image)
    print(
        f"\n{Fore.YELLOW}Basic Caption:{Style.BRIGHT} {basic_caption}"
    )
    while True:
        print_menu()
        choice = input(
            f"{Fore.CYAN}Enter your choice (1-4): {Style.RESET_ALL}"
        )
        if choice == "1":
            caption = truncate_text(basic_caption, 5)
            print(
                f"{Fore.GREEN}Caption (5 words): {Style.BRIGHT}{caption}"
            )
        if choice == "2":
            caption = truncate_text(basic_caption, 30)
            print(
                f"{Fore.GREEN}Caption (30 words): {Style.BRIGHT}{caption}"
            )
        elif choice == "3":
            print(
                f"{Fore.YELLOW}Basic Caption:{Style.BRIGHT} {basic_caption}"
            )
        elif choice == "4":
            print(f"{Fore.MAGENTA}Thank you! Exiting program.")
            break

        else:
            print(f"{Fore.RED}Invalid choice. Try again.")
if __name__ == "__main__":
    main()