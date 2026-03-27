import io
import re
import streamlit as st
import cohere
import config

co = cohere.Client(config.COHERE_API_KEY)


MATH_SYSTEM = """You are a Math Mastermind.
Solve with clear step-by-step reasoning, correct notation, and a final answer.
Verify when possible and mention an alternative method briefly if relevant."""

# ---------------- Core AI Function ----------------
def generate(prompt, temperature=0.3, tokens=1000):
    try:
        r = co.chat(
            model="c4ai-aya-expanse-8b",
            message=prompt,
            temperature=temperature,
            max_tokens=tokens
        )
        return r.text.strip()
    except Exception as e:
        return f"Error: {e}"

# ---------------- Auto-Completion ----------------
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

# ---------------- Export ----------------
def export_txt(history):
    txt = ""
    for i, h in enumerate(history, 1):
        txt += f"Q{i}: {h['question']}\nA{i}: {h['answer']}\n\n"
    return io.BytesIO(txt.encode("utf-8"))

# ================== Teaching Assistant ==================
def run_ai_teaching_assistant():
    st.title("🤖 AI Teaching Assistant")

    st.session_state.setdefault("history_ata", [])

    # NEW: Controls
    temp = st.slider("Creativity Level", 0.0, 1.0, 0.3)
    tokens = st.slider("Max Tokens (Response Length)", 200, 2000, 1000)
    memory = st.checkbox("Enable Conversation Memory", value=True)

    col1, col2 = st.columns([1, 2])
    if col1.button("🧹 Clear"):
        st.session_state.history_ata = []
        st.rerun()

    if st.session_state.history_ata:
        col2.download_button(
            "📄 Export",
            export_txt(st.session_state.history_ata),
            "Teaching_Assistant_Chat.txt",
            "text/plain"
        )

    q = st.text_input("Enter your question:")

    if st.button("Ask"):
        if not q.strip():
            st.warning("⚠️ Enter a question.")
        else:
            with st.spinner("Thinking..."):
                prompt = q

                # NEW: Conversation Memory
                if memory and st.session_state.history_ata:
                    previous = "\n".join(
                        [f"Q: {h['question']}\nA: {h['answer']}"
                         for h in st.session_state.history_ata[:3]]
                    )
                    prompt = previous + "\nCurrent Question: " + q

                ans = generate_complete(prompt, temp, tokens)

            st.session_state.history_ata.insert(
                0, {"question": q.strip(), "answer": ans}
            )
            st.rerun()

    if not st.session_state.history_ata:
        return

    st.markdown("### Conversation History")

    for i, h in enumerate(st.session_state.history_ata, 1):
        st.markdown(f"**Q{i}: {h['question']}**")
        st.markdown(h["answer"])

        # NEW: Regenerate Feature
        if st.button(f"🔁 Regenerate Q{i}", key=f"regen_{i}"):
            new_ans = generate_complete(h["question"], temp, tokens)
            st.session_state.history_ata[i-1]["answer"] = new_ans
            st.rerun()

        st.markdown("---")

def run_math_mastermind():
    st.title("🧮 Math Mastermind")

    st.session_state.setdefault("history_mm", [])

    temp = st.slider("Precision Level", 0.0, 1.0, 0.1)
    tokens = st.slider("Max Tokens", 200, 2000, 1200)

    col1, col2 = st.columns([1, 2])
    if col1.button("🧹 Clear"):
        st.session_state.history_mm = []
        st.rerun()

    if st.session_state.history_mm:
        col2.download_button(
            "📄 Export",
            export_txt(st.session_state.history_mm),
            "Math_Solutions.txt",
            "text/plain"
        )

    problem = st.text_area("Enter math problem:")
    level = st.selectbox("Difficulty", ["Basic", "Intermediate", "Advanced"])

    if st.button("Solve"):
        if not problem.strip():
            st.warning("⚠️ Enter a math problem.")
        else:
            with st.spinner("Solving..."):
                prompt = f"{MATH_SYSTEM}\n\nDifficulty: {level}\nProblem: {problem}"
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

def main():
    st.sidebar.title("Select Feature")

    option = st.sidebar.radio(
        "",
        ["AI Teaching Assistant", "Math Mastermind"]
    )

    if option == "AI Teaching Assistant":
        run_ai_teaching_assistant()
    else:
        run_math_mastermind()

if __name__ == "__main__":
    main()