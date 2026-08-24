# --- Experiment: sweep reasoning_effort for math_problem, auto-grade, and cost logging
import re
import pandas as pd
from fractions import Fraction

math_prompt = prompts['math_problem']
expected_frac = Fraction(24, 7)
expected_decimal = round(float(expected_frac), 2)

reasoning_values = ['none', 'low', 'medium', 'high']
experiments = []

# Price per 1k tokens (USD) - update with official published rates for accurate cost logging
price_per_1k = {
    FOUNDATIONAL_MODEL: 0.0,  # set to actual price per 1000 tokens for foundational model
    REASONING_MODEL: 0.0,     # set to actual price per 1000 tokens for reasoning model
}


def extract_fraction_and_decimal(text):
    # Try to find a fraction like '24/7' or '24 / 7' or spelled '24/7'
    frac_match = re.search(r'(\b\d+\s*/\s*\d+\b)', text)
    decimal_match = re.search(r'([0-9]+\.[0-9]+)', text)
    frac_val = None
    dec_val = None
    if frac_match:
        try:
            frac_val = Fraction(frac_match.group(1).replace(' ', ''))
        except Exception:
            frac_val = None
    if decimal_match:
        try:
            dec_val = round(float(decimal_match.group(1)), 2)
        except Exception:
            dec_val = None
    return frac_val, dec_val


def grade_math_answer(text):
    frac_val, dec_val = extract_fraction_and_decimal(text)
    frac_ok = (frac_val == expected_frac)
    dec_ok = (dec_val == expected_decimal)
    # If fraction missing but decimal within small tolerance, accept
    if frac_val is None and dec_val is not None:
        dec_ok = abs(dec_val - expected_decimal) < 0.01
    score = int(frac_ok) + int(dec_ok)  # 0..2
    return {
        'fraction_found': str(frac_val) if frac_val is not None else None,
        'fraction_ok': frac_ok,
        'decimal_found': float(dec_val) if dec_val is not None else None,
        'decimal_ok': dec_ok,
        'score': score,
    }

# Run experiments
for effort in reasoning_values:
    print(f"Running reasoning model with reasoning_effort={effort}...")
    res = call_reasoning(math_prompt, reasoning_effort=effort)
    grade = grade_math_answer(res['answer'])

    # compute cost from tokens and provided price mapping
    model = res['model']
    ppk = price_per_1k.get(model, 0.0)
    cost = (res['prompt_tokens'] + res['completion_tokens']) * (ppk / 1000.0)

    experiments.append({
        'reasoning_effort': effort,
        'model': model,
        'elapsed_sec': res['elapsed_sec'],
        'prompt_tokens': res['prompt_tokens'],
        'completion_tokens': res['completion_tokens'],
        'reasoning_tokens': res.get('reasoning_tokens', 0),
        'total_tokens': res['total_tokens'],
        'cost_usd': round(cost, 6),
        'answer': res['answer'],
        **grade,
    })

# Also include foundational baseline if available
f_res = call_foundational(math_prompt)
f_grade = grade_math_answer(f_res['answer'])
ppk_f = price_per_1k.get(f_res['model'], 0.0)
cost_f = (f_res['prompt_tokens'] + f_res['completion_tokens']) * (ppk_f / 1000.0)
experiments.append({
    'reasoning_effort': 'foundational_baseline',
    'model': f_res['model'],
    'elapsed_sec': f_res['elapsed_sec'],
    'prompt_tokens': f_res['prompt_tokens'],
    'completion_tokens': f_res['completion_tokens'],
    'reasoning_tokens': 0,
    'total_tokens': f_res['total_tokens'],
    'cost_usd': round(cost_f, 6),
    'answer': f_res['answer'],
    **f_grade,
})

exp_df = pd.DataFrame(experiments)

# Summary table
summary = exp_df[['reasoning_effort','model','elapsed_sec','prompt_tokens','completion_tokens','reasoning_tokens','total_tokens','cost_usd','score']]
print('\nExperiment summary:')
display(summary)

# Simple plots: score vs effort, tokens vs effort
import matplotlib.pyplot as plt

plt.figure(figsize=(8,4))
plt.plot(exp_df['reasoning_effort'], exp_df['score'], marker='o')
plt.title('Grading score (0..2) vs reasoning_effort')
plt.xlabel('reasoning_effort')
plt.ylabel('score')
plt.grid(True)
plt.show()

plt.figure(figsize=(8,4))
plt.bar(exp_df['reasoning_effort'], exp_df['total_tokens'], color='#2C5F2D')
plt.title('Total tokens used vs reasoning_effort')
plt.xlabel('reasoning_effort')
plt.ylabel('total_tokens')
plt.show()

# Save results for later analysis
exp_df.to_csv('Day-03/reasoning_effort_math_experiments.csv', index=False)
print('Saved results to Day-03/reasoning_effort_math_experiments.csv')

# Print explanations supported by data points
print('\nObservations:')
for _, row in exp_df.iterrows():
    print(f"- effort={row['reasoning_effort']}: score={row['score']}, total_tokens={row['total_tokens']}, elapsed={row['elapsed_sec']}s, cost=${row['cost_usd']}")

print('\nAnswers collected:')
for _, row in exp_df.iterrows():
    print('\n---', row['reasoning_effort'], '---')
    print(row['answer'])

print('\nNext steps implemented in this notebook:')
print('- Automatic grader (regex + exact match) for math_problem')
print('- Token-cost logging (update price_per_1k with official rates)')
print('- A slot to extend prompts with domain-specific reasoning tasks (edit `prompts` dict)')
