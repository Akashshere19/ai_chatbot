import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(
    path="data/vector_db"
)

collection = client.get_or_create_collection(
    name="docs"
)

model = SentenceTransformer("all-MiniLM-L6-v2")

def add_document(text):
    chunks = chunk_text(text)
    for chunk in chunks:

        embedding = model.encode(text).tolist()
        collection.add(
            documents=[text],
            embeddings=[embedding],
            ids=[str(hash(text))]
        )

def search(query):
    
    emb = model.encode(query).tolist()

    result = collection.query(
        query_embeddings=[emb],
        n_results=2
    )
    docs = result.get("documents")[0]

    docs = list(set(docs))  

    return docs

    # return result["docs"][0]

def chunk_text(text,chunk_size=500,overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        chunk = text[start:start + chunk_size]
        chunks.append(chunk)
        start +=chunk_size - overlap
    return chunks      

