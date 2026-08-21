results = []
 
for name, prompt in prompts.items():
    print(f"Running '{name}' on {FOUNDATIONAL_MODEL} (foundational)...")
    f_res = call_foundational(prompt)
    f_res["task"] = name
    results.append(f_res)
 
    print(f"Running '{name}' on {REASONING_MODEL} (reasoning)...")
    r_res = call_reasoning(prompt)
    r_res["task"] = name
    results.append(r_res)
 
print("\nDone.")
    print(f"--- {k} ---\n{v}\n")
