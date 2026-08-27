documents = [
    {
        "id": "POL-AUTO-001",
        "text": "Auto Policy, Section 4.2 (Collision Coverage): The Company will pay for direct "
                "and accidental physical loss to your covered auto caused by collision, subject to "
                "a $500 deductible per occurrence. Coverage applies regardless of fault.",
        "source": "Auto Policy Booklet", "effective_date": "2024-01-01",
    },
    {
        "id": "POL-AUTO-002",
        "text": "Auto Policy, Section 4.5 (Rental Reimbursement): If your covered auto is out of "
                "service due to a covered collision or comprehensive loss, the Company will "
                "reimburse rental costs up to $40/day for a maximum of 30 days.",
        "source": "Auto Policy Booklet", "effective_date": "2024-01-01",
    },
    {
        "id": "POL-HOME-010",
        "text": "Homeowners Policy, Section 3.1 (Dwelling Coverage): The Company will pay to repair "
                "or replace damage to the dwelling structure caused by a covered peril, up to the "
                "policy limit shown on the declarations page.",
        "source": "Homeowners Policy Booklet", "effective_date": "2024-03-15",
    },
    {
        "id": "POL-HOME-014",
        "text": "Homeowners Policy, Section 3.6 (Water Damage Exclusion): Damage caused by flood, "
                "surface water, or sewer backup is excluded from standard coverage. Separate flood "
                "insurance must be purchased to cover these perils.",
        "source": "Homeowners Policy Booklet", "effective_date": "2024-03-15",
    },
    {
        "id": "POL-CLAIMS-003",
        "text": "Claims Handling Guideline 3: All collision claims over $10,000 must be routed to "
                "a Senior Claims Adjuster for review before settlement is authorized. Claims under "
                "$10,000 may be settled by a standard adjuster.",
        "source": "Claims Handling Guidelines", "effective_date": "2024-06-01",
    },
    {
        "id": "POL-CLAIMS-007",
        "text": "Claims Handling Guideline 7: Any claim involving a suspected total loss (repair cost "
                "exceeds 75% of actual cash value) must be escalated to the Total Loss unit within "
                "2 business days of the initial estimate.",
        "source": "Claims Handling Guidelines", "effective_date": "2024-06-01",
    },
]
 
print(f"Loaded {len(documents)} chunks from {len(set(d['source'] for d in documents))} source documents.")
 































































































 
