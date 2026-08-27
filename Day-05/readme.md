
# Imports
import pandas as pd
from dataclasses import dataclass
from typing import List

pd.set_option('display.max_colwidth', 100)

@dataclass
class Item:
    name: str
    user_business_value: int  # 1..10
    time_criticality: int     # 1..10
    risk_reduction_opportunity: int  # 1..10
    job_size: int             # must be > 0

def compute_wsjf(items: List[Item]) -> pd.DataFrame:
    """Compute Cost of Delay and WSJF for a list of Items.
    Raises ValueError if any job_size <= 0.
    Returns a DataFrame sorted by WSJF descending.
    """
    rows = []
    for it in items:
        if it.job_size is None or it.job_size <= 0:
            raise ValueError(f"Invalid job_size for item '{it.name}': {it.job_size!r}. job_size must be > 0.")
        cost_of_delay = int(it.user_business_value) + int(it.time_criticality) + int(it.risk_reduction_opportunity)
        wsjf = round(cost_of_delay / float(it.job_size), 2)
        rows.append({
            'name': it.name,
            'cost_of_delay': cost_of_delay,
            'job_size': it.job_size,
            'wsjf': wsjf
        })
    df = pd.DataFrame(rows)
    df = df.sort_values('wsjf', ascending=False).reset_index(drop=True)
    df.index += 1
    return df

def show_and_explain(df: pd.DataFrame):
    display(df[['name','cost_of_delay','job_size','wsjf']])
    print('\nExplanation: Cost of Delay = user_business_value + time_criticality + risk_reduction_opportunity')
    print('WSJF = Cost of Delay / Job Size (higher WSJF means higher priority).')
