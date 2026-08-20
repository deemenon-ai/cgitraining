def reset_password(employee_id: str) -> dict:
    """Reset an employee's password (mock implementation)."""
    if employee_id not in _PASSWORDS:
        return {"error": f"No password record found for {employee_id}"}

    old = _PASSWORDS[employee_id]
    NEW_PASSWORD = f"tmp{random.randint(100000, 999999)}"
    _PASSWORDS[employee_id] = NEW_PASSWORD
    return {"employee_id": employee_id, "old_password": old, "new_password": NEW_PASSWORD}

print("Before password for E1002:", _PASSWORDS.get("E1002"))
print("Running DeskPilot test:")
