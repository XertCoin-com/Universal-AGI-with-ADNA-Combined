import time, random, json
from poe.poe import proposer_probability, score

chain = []

def simulate_round(models):
    scores = {m: score({"accuracy": random.random(), "speed": random.random(), "energy": random.random(), "cost": random.random()/5}) for m in models}
    dominance = {m: sum(1 for b in chain if b["proposer"] == m)/max(1,len(chain)) for m in models}
    probs = proposer_probability(scores, dominance)
    r = random.random()
    cum = 0.0
    selected = models[-1]
    for m,p in probs.items():
        cum += p
        if r <= cum:
            selected = m
            break
    block = {"height": len(chain)+1, "proposer": selected, "scores": scores}
    chain.append(block)
    return block, probs

if __name__ == "__main__":
    models = ["alpha", "beta", "gamma"]
    for _ in range(5):
        blk, probs = simulate_round(models)
        print(json.dumps({"block": blk, "probs": probs}, indent=2))
        time.sleep(0.4)
