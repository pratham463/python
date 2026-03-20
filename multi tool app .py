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
        return f"error: {e}"
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
def run_ai_teaching_assistant():
     st.title("Ai teaching assistant")
     st.session_state.setdefault("histor_ata",[])
     temp=st.slider("goofiness level:",0.0,1.0,0.3)
     tokens=st.slider("length:",200,2000,10000)
     memory=st.checkbox("enable conversation memory",value=True)
     col1,col2=st.colums([1,2])
     if col1.button("clear"):
          st.session_state.history_ata =[
               
          ]
          st.rerun()
     if st.session_state.history_ata:
          col2.download_button(
               "export",
               export_txt(st.session_state.history_ata),
               "TEeaching_Asistnat_Cat.txt",
               "text/plsin"
          )
     q=st.text_input("enter your question")
     if st.button("Ask"):
          if not q.strip():
               st.warning("enter a question?")
          else:
        with st.spinner("Thinking..."):
            prompt = q

            # NEW: Conversation Memory
            if memory and st.session_state.history_ata:
                previous = "\n".join(
                    [f"Q: {h['question']}\nA: {h['answer']}"
                     for h in st.session_state.history_ata[:3]]
                )