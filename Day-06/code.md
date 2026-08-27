
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

# 1. Install dependencies (Colab-friendly)
!pip install -q openai sentence-transformers faiss-cpu rank_bm25


 # 2. Set up your OpenAI API key
import os
import getpass
 
try:
    from google.colab import userdata
    api_key = "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"
except Exception:
    api_key = None
 
if not api_key:
    api_key = getpass.getpass("Enter your OpenAI API key: ")
 
os.environ["OPENAI_API_KEY"] = api_key
print("API key configured.")











































































































 
