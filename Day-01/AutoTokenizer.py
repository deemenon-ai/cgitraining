
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("gpt2")
 
words = ["unbelievable", "the", "internationalization", "Transformer", "CGI", "tokenization"]
 
for w in words:
    ids = tokenizer.encode(w)
    pieces = [tokenizer.decode([i]) for i in ids]
    print(f"{w:24s} -> {pieces}  ({len(ids)} token{'s' if len(ids)!=1 else ''})")