


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











































































































 
