import streamlit as st
import anthropic

client = anthropic.Anthropic()

def find_best_chunk(question, chunks):
    question_words = question.lower().split()
    best_chunk = chunks[0]
    best_score = 0
    for chunk in chunks:
        score = 0
        for word in question_words:
            word = word.strip("?.,!:;")
            if len(word) > 3:
                if word in chunk.lower():
                    score = score + 1
        if score > best_score:
            best_score = score
            best_chunk = chunk
    if best_score == 0:
        return None   #no chunk earned a point
    return best_chunk

def ask_claude(prompt):
    reply = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=300,
        messages=[{"role": "user", "content": prompt}],
    )
    return reply.content[0].text

st.title("Chat With Your Documents")

uploaded = st.file_uploader("Upload a text file", type="txt")
question = st.text_input("Ask a question about the document: ")

if uploaded:
    if question:
        text = uploaded.read().decode("utf-8")
        chunks = text.split("\n\n")
        best = find_best_chunk(question, chunks)

        if best is None:
            st.write("Sorry, the document does not cover that question.")
        else:
            prompt = f"""Here is a part of a document:

{best}

using ONLY the text above, answer this question: {question}"""

            st.write("Retrieved chunk:", best)
            st.write("-----")
            st.write("Claude's answer:", ask_claude(prompt))

