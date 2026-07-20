import anthropic

client = anthropic.Anthropic()

def split_document(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    chunks = text.split("\n\n")
    return chunks

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

question = input("Ask a question about the document: ")

chunks = split_document("space_facts.txt")
best = find_best_chunk(question, chunks)

if best is None:
    print("Sorry, the document does not cover that question.")
else:
    prompt = f"""Here is a part of a document:

{best}

using ONLY the text above, answer this question: {question}"""

    print("Retrieved chunk:", best)
    print("-----")
    print("Claude's answer:", ask_claude(prompt))



