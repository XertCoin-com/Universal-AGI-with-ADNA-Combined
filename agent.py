import argparse, time, json, random
from adna.adna import ADNA
from poe.poe import score
from datetime import datetime

def run(model_name: str, task: str, offline: bool):
    for step in range(3):
        time.sleep(0.4)
    fitness = {"accuracy": round(random.uniform(0.7, 0.95), 4),
               "speed": random.uniform(0.5, 1.0),
               "energy": random.uniform(0.5, 1.0),
               "cost": random.uniform(0.1, 0.5)}
    adna = ADNA(
        model_id=f"{model_name}-{int(time.time())}",
        parent_ids=[],
        version="0.1.0",
        created_at=datetime.utcnow().isoformat() + "Z",
        traits={"transformer": True, "params_m": 250},
        training={"datasets_commit": "deadbeef", "steps": 1000, "hyperparams": {"lr": 1e-4}},
        fitness={**fitness, "composite": score(fitness)},
    )
    print(json.dumps({"adna_commit": adna.commitment(), "fitness": adna.fitness}, indent=2))

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--model", required=True)
    p.add_argument("--task", required=True)
    p.add_argument("--offline", action="store_true")
    args = p.parse_args()
    run(args.model, args.task, args.offline)
