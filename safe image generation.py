import streamlit as st
from io import BytesIO
from PIL import Image
import requests
import urllib.parse
import re
BLOCK_WORDS = [
    "suicide", "self harm", "self-harm", "kill", "murder",
    "bomb", "explosive", "terror", "attack",
    "gun", "weapon", "knife", "shoot",
    "blood", "gore", "dismember", "decapitate",
    "hate", "nazi", "racism"
]
BLOCK_PATTERNS = [
    r"\b(kill|murder|suicide|self[-\s]?harm)\b",
    r"\b(gun|weapon|knife|bomb|explosive)\b",
    r"\b(blood|gore|decapitate)\w*\b",
    r"\b(terror|attack)\b",
    r"\b(nazi|racism)\w*\b"
]
def is_safe(prompt:str):
    p = prompt.lower()
    for word in BLOCK_WORDS:
        if word in p:
            return False,f"sorry cant use this word during generation   {word}"
    for pat in BLOCK_PATTERNS:
        if re.search(pat, prompt, flags=re.I):
            return False, "Blocked unsafe pattern"
    return True, ""
def gen_image(prompt: str):
    ok, reason = is_safe(prompt)
    if not ok:
        return None, f" Prompt contains unsafe content. {reason}"
    try:
        encoded_prompt = urllib.parse.quote(prompt)
        url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"
        response =requests.get(url)
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
            return img, None
        else:
            return None, " Failed to generate image."
    except Exception as e:
        return None, str(e)
def main():
    st.set_page_config(page_title="Safe AI Image Generator", layout="centered")
    st.title("Safe AI Image Generator (Classroom Version)")
    st.info("Unsafe topics like violence, self-harm, and weapons are blocked.")
    with st.form("image_form"):
        raw = st.text_area(
            "Image Description",
            height=120,
            placeholder="Example: A cute robot reading a book in a library"
        )
        submit = st.form_submit_button("Generate Image")
    if submit:
        if not raw.strip():
            st.warning(" Please enter an image description.")
            return
        with st.spinner("Generating image..."):
            img, err = gen_image(raw.strip())
        if err:
            st.error(err)
            return
        st.image(img, caption="Generated Image", use_container_width=True)
        st.session_state.generated_image = img
        if img:
            buf = BytesIO()
            img.save(buf,format="PNG")
            st.download_button(
                "download image",
                buf.getvalue,
                "ai_generated_image.png",
                "image/png"
            )
if __name__ =="__main__":
    main()