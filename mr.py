import requests
from PIL import Image
from io import BytesIO


def generate_ai_image(prompt, size):
    url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}"
    response = requests.get(url)
    img = Image.open(BytesIO(response.content)).convert("RGB")
    return img.resize(size)

def pseudo_inpaint(prompt, image_path, mask_path):
    base_img = Image.open(image_path).convert("RGB")
    mask_img = Image.open(mask_path).convert("L")

    ai_img = generate_ai_image(prompt, base_img.size)


    result = Image.composite(ai_img, base_img, mask_img)
    return result


def main():
    print("Inpainting & Restoration Challenge ")
    print("White mask area will be replaced using AI\n")

    while True:
        prompt = input("Enter description (or 'exit'): ")
        if prompt.lower() == "exit":
            print("Goodbye!")
            break

        image_path = input("Enter base image path: ")
        mask_path = input("Enter mask image path: ")

        try:
            print("\nProcessing inpainting...")
            result = pseudo_inpaint(prompt, image_path, mask_path)
            result.show()

            save = input("Save image? (yes/no): ").lower()
            if save == "yes":
                name = input("File name (without extension): ").strip()
                result.save(f"{name}.png")
                print(f"Image saved as {name}.png\n")

            print("-" * 60)

        except Exception as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()
