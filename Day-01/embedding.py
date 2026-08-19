
from transformers import AutoModel
import numpy as np
import matplotlib.pyplot as plt
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("gpt2")

model = AutoModel.from_pretrained("gpt2")
embedding_table = model.get_input_embeddings().weight.detach().numpy()  # shape: (vocab_size, hidden_dim)
 
def word_vector(word):
    # Use the first token of the word's encoding as a stand-in single-token vector
    token_id = tokenizer.encode(" " + word)[0]
    return embedding_table[token_id]
 
sample_words = ["king", "queen", "man", "woman", "dog", "cat", "Python", "JavaScript"]
vectors = np.array([word_vector(w) for w in sample_words])
 
def cosine_sim(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
 
n = len(sample_words)
sim_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        sim_matrix[i, j] = cosine_sim(vectors[i], vectors[j])
 
plt.figure(figsize=(6, 5))
plt.imshow(sim_matrix, cmap="viridis")
plt.xticks(range(n), sample_words, rotation=45, ha="right")
plt.yticks(range(n), sample_words)
plt.colorbar(label="Cosine similarity")
plt.title("Embedding similarity (GPT-2 input embeddings)")
plt.tight_layout()
plt.show()