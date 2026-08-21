prompts = {
    "logic_puzzle": (
        "Five friends (Ana, Ben, Cara, Dan, Ella) sit in a row of 5 seats "
        "numbered 1 to 5 left to right. Clues: "
        "(1) Ana sits immediately left of Ben. "
        "(2) Cara does not sit at either end. "
        "(3) Dan sits somewhere to the right of Ella. "
        "(4) Ella is not in seat 1. "
        "(5) Ben is not in seat 5. "
        "Work out the exact seating order from seat 1 to seat 5, and briefly "
        "justify each step."
    ),
    "math_problem": (
        "A tank is filled by Pipe A in 6 hours and by Pipe B in 4 hours. "
        "Pipe C, working alone, can drain a full tank in 8 hours. "
        "If all three pipes are opened together starting with an empty tank, "
        "how long will it take to fill the tank? Show your work and give an "
        "exact fraction, then a decimal rounded to 2 places."
    ),
    "planning_task": (
        "You must schedule 4 tasks (T1: 3 hrs, T2: 2 hrs, T3: 4 hrs, T4: 1 hr) "
        "across 2 workers over an 8-hour day so that: total time per worker "
        "does not exceed 8 hours, T3 must start before T1 can start, and "
        "T2 and T4 must be done by the same worker. Provide a valid "
        "assignment and timeline, and explain why it satisfies every "
        "constraint."
    ),
}
 
for k, v in prompts.items():
    print(f"--- {k} ---\n{v}\n")
