from rank_bm25 import BM25Okapi
 
tokenized_corpus = [d["text"].lower().split() for d in documents]
bm25 = BM25Okapi(tokenized_corpus)
 
def hybrid_search(query, k=3, vector_weight=0.6):
    # Vector scores over the full corpus
    q_emb = embedder.encode([query], normalize_embeddings=True)
    vec_scores = (np.array(embeddings, dtype='float32') @ q_emb[0])
 
    # BM25 keyword scores over the full corpus
    bm25_scores = np.array(bm25.get_scores(query.lower().split()))
    if bm25_scores.max() > 0:
        bm25_scores = bm25_scores / bm25_scores.max()  # normalize to 0-1
 
    fused = vector_weight * vec_scores + (1 - vector_weight) * bm25_scores
    top_idx = np.argsort(-fused)[:k]
    return [(documents[i], float(fused[i])) for i in top_idx]
 
# Compare: an exact-number query where keyword matching should help
exact_query = "What is the threshold for escalating a claim to a Senior Claims Adjuster?"
print("-- Vector-only --")
for doc, score in vector_search(exact_query):
    print(f"[{score:.3f}] {doc['id']}")
print("\n-- Hybrid (vector + BM25) --")
for doc, score in hybrid_search(exact_query):
    print(f"[{score:.3f}] {doc['id']}")
 
