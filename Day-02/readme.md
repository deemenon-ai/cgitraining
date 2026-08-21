import time
 
def call_foundational(prompt, model=FOUNDATIONAL_MODEL, temperature=0.2, max_tokens=800):
    start = time.time()
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        max_tokens=max_tokens,
    )
    elapsed = time.time() - start
    return {
        "model": model,
        "type": "foundational",
        "answer": resp.choices[0].message.content,
        "elapsed_sec": round(elapsed, 2),
        "prompt_tokens": resp.usage.prompt_tokens,
        "completion_tokens": resp.usage.completion_tokens,
        "reasoning_tokens": 0,
        "total_tokens": resp.usage.total_tokens,
    }
 
def call_reasoning(prompt, model=REASONING_MODEL, reasoning_effort="medium", max_completion_tokens=2000):
    start = time.time()
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        reasoning_effort=reasoning_effort,
        max_completion_tokens=max_completion_tokens,
    )
    elapsed = time.time() - start
    usage = resp.usage
    reasoning_tokens = 0
    details = getattr(usage, "completion_tokens_details", None)
    if details is not None:
        reasoning_tokens = getattr(details, "reasoning_tokens", 0) or 0
    return {
        "model": model,
        "type": "reasoning",
        "answer": resp.choices[0].message.content,
        "elapsed_sec": round(elapsed, 2),
        "prompt_tokens": usage.prompt_tokens,
        "completion_tokens": usage.completion_tokens,
        "reasoning_tokens": reasoning_tokens,
        "total_tokens": usage.total_tokens,
    }
 
for k, v in prompts.items():
    print(f"--- {k} ---\n{v}\n")
