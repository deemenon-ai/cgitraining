from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
 
embedder = SentenceTransformer("all-MiniLM-L6-v2")
 
texts = [d["text"] for d in documents]
embeddings = embedder.encode(texts, normalize_embeddings=True)
 
dim = embeddings.shape[1]
index = faiss.IndexFlatIP(dim)  # inner product on normalized vectors = cosine similarity
index.add(np.array(embeddings, dtype="float32"))
 
print(f"Indexed {index.ntotal} chunks, dimension {dim}.")







def vector_search(query, k=3):
    q_emb = embedder.encode([query], normalize_embeddings=True)
    scores, idxs = index.search(np.array(q_emb, dtype="float32"), k)
    return [(documents[i], float(scores[0][rank])) for rank, i in enumerate(idxs[0])]
 
def naive_rag_retrieve(query, k=3):
    results = vector_search(query, k=k)
    return [doc for doc, score in results]
 
# Try it
sample_query = "How much does the company pay for a rental car after a collision?"
for doc, score in vector_search(sample_query):
    print(f"[{score:.3f}] {doc['id']}: {doc['text'][:90]}...")




 
