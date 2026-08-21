import pandas as pd
 
df = pd.DataFrame(results)[
    ["task", "type", "model", "elapsed_sec", "prompt_tokens",
     "completion_tokens", "reasoning_tokens", "total_tokens"]
]
df
 
