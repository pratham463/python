import requests
from PIL import Image
from io import BytesIO
def generate_image(prompt):
    url=f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}"
    response = requests.get(url)
    response.raise_for_status()
    img = Image.open(BytesIO(response.content))
    return img
img = generate_image(
    "cozy aesthetic study room with warm lights, books, plants, soft tones")
img