"""Transparent, illustrative transaction-risk baseline (not an ML model)."""
from dataclasses import dataclass
from math import isfinite


@dataclass(frozen=True)
class Transaction:
    amount: float
    transactions_last_hour: int
    country_mismatch: bool = False


def score_transaction(transaction: Transaction) -> dict:
    """Return a deterministic score and auditable reason codes."""
    if not isfinite(transaction.amount) or transaction.amount < 0:
        raise ValueError("amount must be finite and nonnegative")
    if isinstance(transaction.transactions_last_hour, bool) or not isinstance(transaction.transactions_last_hour, int) or transaction.transactions_last_hour < 0:
        raise ValueError("transactions_last_hour must be a nonnegative integer")
    if not isinstance(transaction.country_mismatch, bool):
        raise ValueError("country_mismatch must be boolean")
    reasons = []
    if transaction.amount >= 5000:
        reasons.append(("HIGH_AMOUNT", 40))
    if transaction.transactions_last_hour >= 8:
        reasons.append(("HIGH_VELOCITY", 35))
    if transaction.country_mismatch:
        reasons.append(("COUNTRY_MISMATCH", 25))
    score = min(100, sum(points for _, points in reasons))
    band = "high" if score >= 70 else "medium" if score >= 35 else "low"
    return {"risk_score": score, "risk_band": band, "reasons": [name for name, _ in reasons], "model_type": "illustrative_rules_v1"}


if __name__ == "__main__":
    print(score_transaction(Transaction(amount=6500, transactions_last_hour=10, country_mismatch=True)))
