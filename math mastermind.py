import io
import re
import streamlit as st
import cohere
import config

co = cohere.Client(config.COHERE_API_KEY)
MATH_SYSTEM="""you are a maths mastermind and i will help you sole your questions and doubts"""
def generate(prompt,temperature = 0.3,tokens=1000):
    try:
        r=co.chat(
            model="c4ai-aya-expanse-8b",
            message =prompt,
            temperature=temperature,
            max_tokens=tokens
        )
        return r.text.strip()
    except Exception as e:
        return f"erorr:{e}"
def looks_incomplete(text):
    return not text.strip().endswith((".", "!", "?"))
def generate_complete(prompt, temperature, tokens):
    ans = generate(prompt, temperature, tokens)
    if looks_incomplete(ans):
        cont = generate(
            f"Continue from where you stopped. Do not repeat.\n\n{ans}",
            temperature,
            tokens
        )
        ans = ans + "\n" + cont
    return ans
def export_txt(history):
    txt=""
    for i,h in enumerate(history,1):
        txt +=f"Q{i}:{h['question']}\n A{i}:{h['awnser']}\n\n"
    return io.BytesIO(txt.encode("utf-8"))
def run_math_mastermind():
    st.titel("mathmastermind")
    st.session_state.setdefault("history_mm",[])
    temp=st.slider("Precision Level",0.0,1.0,0.1)
    tokens=st.slider("max tokens",200,2000,1200)
    col1, col2 = st.columns([1, 2])

    if col1.button("Clear"):
        st.session_state.history_mm = []
        st.rerun()

    if st.session_state.history_mm:
        col2.download_button(
            "Export",
            export_txt(st.session_state.history_mm),
            "Math_Solutions.txt",
            "text/plain"
        )
    problem = st.text_area("Enter math problem:")
    level = st.selectbox("Difficulty", ["Basic", "Intermediate", "Advanced"])

    if st.button("Solve"):
        if not problem.strip():
            st.warning
        else:
            with st.spinner("Solving..."):
                prompt = f"""MATH_SYSTEM

Difficulty: {level}
Problem: {problem}
"""
            ans = generate_complete(prompt, temp, tokens)
        st.session_state.history_mm.insert(
            0, {"question": problem.strip(), "answer": ans}
        )

        st.rerun()

    if not st.session_state.history_mm:
        return

    st.markdown("### Solution History")

    for i, h in enumerate(st.session_state.history_mm, 1):
        st.markdown(f"**Q{i}: {h['question']}**")
        st.markdown(h["answer"])
        st.markdown("---")

