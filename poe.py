from typing import Dict

def score(f: Dict[str, float], weights=None) -> float:
    w = weights or {"accuracy": 0.5, "speed": 0.2, "energy": 0.2, "cost": -0.1}
    return (
        w["accuracy"] * f.get("accuracy", 0.0) +
        w["speed"] * f.get("speed", 0.0) +
        w["energy"] * f.get("energy", 0.0) +
        w["cost"] * f.get("cost", 0.0)
    )

def dominance_penalty(dominance: float, k: float = 0.3) -> float:
    return max(0.0, 1.0 - k * dominance)

def proposer_probability(scores: Dict[str, float], dominance: Dict[str, float]) -> Dict[str, float]:
    total = sum(scores.values()) or 1.0
    probs = {}
    for m, s in scores.items():
        p = (s / total) * dominance_penalty(dominance.get(m, 0.0))
        probs[m] = p
    z = sum(probs.values()) or 1.0
    return {m: p / z for m, p in probs.items()}
