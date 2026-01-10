import requests
from requests.auth import HTTPBasicAuth
from PIL import Image
import os
from colorama import init, Fore, Style

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
          4.100 words
          5.exit
=====================================================
""")

