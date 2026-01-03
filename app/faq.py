import pandas as pd
from pathlib import Path 
import chromadb
from chromadb.utils import embedding_functions
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

faqs_path = Path(__file__).parent / "resources/faq_data.csv"
chromadb_client = chromadb.Client()
collection_name = "faqs"

ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

def ingest_faq_data(path):
    if collection_name not in chromadb_client.list_collections():
        collection = chromadb_client.get_or_create_collection(name=collection_name,
        embedding_function=ef
        )
        
        df = pd.read_csv(path)
        question = df['question'].tolist()
        answers = df['answer'].tolist()
        ids = [f"id_{i}" for i in range(len(question))]
        metadata = [{"answer": ans} for ans in answers]

        collection.add(ids=ids,
        documents=question,
        metadatas=metadata
        )
    else:
        print(f"Collection {collection_name} already exists. Skipping ingestion.")

def get_relevent_qa(query):
    collection = chromadb_client.get_collection(name=collection_name)
    return collection.query(query_texts=[query], n_results=2)


def faq_chain(query: str):
    results = get_relevent_qa(query)
    context = " ".join([item['answer'] for item in results['metadatas'][0]])
    answer = generate_answer(query, context)
    return answer
    

def generate_answer(query : str, context : str):
    prompt = f'''Given the following context and question, generate answer based on this context only.
    If the answer is not found in the context, kindly state "I don't know". Don't try to make up an answer.
    
    CONTEXT: {context}
    
    QUESTION: {query}
    '''
    client = Groq()
    chat_completion = client.chat.completions.create(
        model=os.getenv("GROQ_MODEL_NAME"),
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return chat_completion.choices[0].message.content.strip()

if __name__ == "__main__":
    ingest_faq_data(faqs_path)
    query= "Do you take cash as a payment method?"
    results = faq_chain(query)
    print("Q:", query)
    print("A:", results)
