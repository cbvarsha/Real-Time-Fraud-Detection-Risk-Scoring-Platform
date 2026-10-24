# Transaction Risk Scoring — Reference Implementation

An **independent portfolio project** demonstrating a transparent, rule-based transaction risk scoring baseline. This is **not** a trained machine-learning model, real-time production service, or validated fraud detection system.

## Current scope

- Deterministic scoring based on transaction amount, velocity, and geographic mismatch
- Risk bands and human-readable decision reasons
- Pure-Python implementation with standard-library tests
- Synthetic examples only; no customer or production data

## Run

```bash
python -m src.app
python -m unittest discover -s tests -v
```

## Engineering roadmap

1. Add a versioned event schema, idempotent ingestion, and persistent event storage.
2. Introduce a feature store and temporal train/validation/test splits.
3. Train and calibrate a fraud classifier on appropriately licensed data; measure PR-AUC, recall at fixed false-positive rate, latency, and drift.
4. Add API authentication, structured logs, tracing, rate limiting, CI, and threat modeling.
5. Document fairness, privacy, human review, and model governance.

## Limitations

The risk thresholds are illustrative. The outputs must not be used for financial or fraud-prevention decisions.

## License

No license has been granted; see repository ownership terms.
