from schema import AccountLedger

def evaluate_ledger_deterministic(ledger: AccountLedger, scheme_key: dict) -> dict:
    """
    Tier 2 Deterministic Rule Engine for Kerala DHSE Valuation
    No LLM inference happens here. This is strictly rule-based math.
    """
    evaluation_result = {
        "marks_awarded": 0.0,
        "deductions": [],
        "status": "EVALUATED",
        "human_audit_required": ledger.needs_human_review
    }

    # 1. Route to Human if Perception Layer Failed
    if ledger.extraction_confidence < 0.85 or ledger.needs_human_review:
        evaluation_result["status"] = "ROUTED_TO_HUMAN"
        evaluation_result["marks_awarded"] = 0.0
        return evaluation_result

    # 2. Evaluate Exact Ledger Entries (Step Marks)
    # DHSE Scheme: 0.5 marks per correct entry pair
    correct_entries = 0
    for entry in ledger.debit_entries:
        if any(key_entry['particulars'] == entry.particulars and key_entry['amount'] == entry.amount 
               for key_entry in scheme_key.get("debit_side", [])):
            correct_entries += 1
            
    # Award partial marks for entries
    evaluation_result["marks_awarded"] += (correct_entries * 0.5)

    # 3. Evaluate Balancing Figure (Zero Variance Rule)
    # DHSE Scheme: 1 mark for correct balancing and totaling
    if ledger.balancing_figure == scheme_key.get("expected_balance"):
        evaluation_result["marks_awarded"] += 1.0
    else:
        evaluation_result["deductions"].append(
            f"Incorrect balancing figure. Expected {scheme_key.get('expected_balance')}, got {ledger.balancing_figure}"
        )

    return evaluation_result
