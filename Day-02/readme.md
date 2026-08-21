for name in prompts:
    print("=" * 90)
    print(f"TASK: {name}")
    print("=" * 90)
    for res in results:
        if res["task"] != name:
            continue
        print(f"\n### {res['type'].upper()} MODEL: {res['model']} "
              f"(⏱ {res['elapsed_sec']}s, total tokens {res['total_tokens']}, "
              f"reasoning tokens {res['reasoning_tokens']})\n")
        print(res["answer"])
    print()
 
 
