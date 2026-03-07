import io
import streamlit as st
import cohere
import config
co = cohere.Client(config.COHERE_API_KEY)
def generate_response(prompt, temperature=0.3, max_tokens=300):
    try:
        res = co.chat(
            model="c4ai-aya-expanse-8b",
            message=prompt,
            temperature=temperature,
            max_tokens=max_tokens
        )
        return res.text.strip()
    except Exception as e:
        return f"{e}"
CSS="""
    <style>
.history-wrap {
    max-height: 420px;
    overflow-y: auto;
    padding-right: 6px;
}
.qa-card {
    border: 1px solid #e6e6e6;
    background: #f9f9ff;
    border-radius: 10px;
    padding: 14 px 16 px;
    margin: 10px 0;
    box - shadow: 0 1 px 2px rgba(0,0,0,0.04);
}
}

.q{
    font-weight: 700;
    color: #0a6ebd;
    margin-bottom: 8px;
}
.a{
    white-space: pre-wrap;
    color: #333;
    line-height: 1.5;
}
</style>
"""
def export_bytes(history):
    text = "".join([
        f"Q{i}: {h['question']}\nA{i}: {h['answer']}\n\n"
        for i, h in enumerate(history, 1)
    ])
    return io.BytesIO(text.encode("utf-8"))
def setup_ui():
    st.set_page_config(page_title="Ai teaching assistant", layout="centered")
    st.title(" Ai teaching assistant (Cohere)")
    st.write("Ask any question and get ai-powered answers.")
    st.session_state.setdefault("history", [])
col_clear, col_export = st.columns([1, 2])

with col_clear:
    if st.button(" Clear Chat"):
        st.session_state.history = []
        st.rerun()
with col_export:
    if st.session_state.history:
        st.download_button(
            label="Export Chat",
            data=export_bytes(st.session_state.history),
            file_name="AI_Chat_History.txt",
            mime="text/plain",
        )
    user_input = st.text_input("Enter your question:")
    if st.button("Ask"):
        q =user_input.strip()
        if q:
            with st.spinner("Generating Response......"):
                a = generate_response(q,temperature=0.3)
                st.session_state.history.insert(0, {
                            "question": q,
                            "answer": a
                })

                st.rerun()

        else:
            st.warning("⚠ Please enter a question.")
            st.markdown("### Conversation History")
            st.markdown(CSS, unsafe_allow_html=True)

            cards = []

            for i, h in enumerate(st.session_state.history, 1):
                cards.append(
                    f"""
                    <div class="qa-card">
                            <div class="q">Q{i}: {h["question"]}</div>
                            <div class="a">{h["answer"]}</div>
                    </div>
                    """
                    )
            st.markdown(
                '<div class="history-wrap">'+"".join(cards)+"</div>",
                unsafe_allow_html=True
                 )
def main():
    setup_ui()
if __name__ == "__main__":
    main()