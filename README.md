# Chat With Your Documents (RAG)

A small Retrieval-Augmented Generation app in Python: ask a question about a document, and Claude answers using only what the document says.

## What it does
The user is asked to ask a question about the document when the app asks. The app finds the right part of the document and then AI answers the user's question from the document. If the answer is not found in the document, the AI lets the user know that the answer is not in the document.

## How it works
1. The app divides the document into chunks.
2. The app compares the words from the user's question to the chunks and finds the chunk with the most words from the user's question.
3. The chunk with the most words matched gets sent to Claude. Claude answers the question based on the text in the chunk. If the question is not found in the chunk a message is sent to the user that the document does not cover that question. 

## How to run it
- pip install anthropic
- set ANTHROPIC_API_KEY as an environment variable (your own key)
- Run python rag_app.py

## Example
Question - Which planet is the largest?
Retrieved chunk - Jupiter is the largest planet. It is so big that more than 1300 Earths could fit inside it.
Claude's answer - Jupiter is the largest planet.

When question is not found in the document:
Question - What is the tallest mountain?
Retrieved chunk - None.
Answer - Sorry, the document does not cover that question.

## Honest limitations
- Keyword matching sees letters, not meaning, so similar words don't get matched - if the user enters the word "biggest" and the text contains the words "largest", the app won't find the word "largest" in the document.
- The user can't upload his own document (planned for next version)
- If two chunks have a tie in the number of keywords matched, the app will choose the first chunk from the two and send it to the AI. 

## Roadmap
- Streamlit web UI with file upload
- V2: embeddings-based retrieval (fixes the synonym problem)

## What I learned building this
- Integrating Anthropic Claude via API.
- How a RAG app divides text into chunks and does a search to match the keywords from the user's question to the right chunk.
- Building a RAG app that finds the part of the text in a document that contains the user's question, then AI returns the answer. 
