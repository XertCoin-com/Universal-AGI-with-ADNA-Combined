from dataclasses import dataclass

@dataclass
class Reputation:
    accuracy: float = 0.0
    contributions: float = 0.0
    ethics: float = 0.0

    def index(self, w=None) -> float:
        w = w or {"accuracy": 0.4, "contributions": 0.4, "ethics": 0.2}
        return w["accuracy"]*self.accuracy + w["contributions"]*self.contributions + w["ethics"]*self.ethics

def quadratic_vote(tokens: float, rep_idx: float) -> float:
    return (tokens ** 0.5) * (1.0 + rep_idx)
