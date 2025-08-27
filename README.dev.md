# Universal AGI with ADNA — Developer README

This is the **developer-facing** README that complements the whitepaper in the repo.
It ships a reference node, an ADNA schema, PoE scoring, and a minimal on-chain registry.

## Quickstart
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r node/requirements.txt

# Demonstrate PoE lottery on a local "devnet"
python node/devnet.py

# Run a mock agent: produces an ADNA commitment + fitness
python node/agent.py --model tiny-llm --task benchmark/mnist.json --offline
```

## Repo Structure (added by PR-1)
- `adna/` — ADNA schema & helper
- `poe/` — Proof of Evolution scoring
- `governance/` — reputation + quadratic voting prototype
- `node/` — reference Python node (devnet + agent stubs)
- `contracts/ethereum/` — `ADNARegistry.sol` (commit registry)
- `specs/` — protocol docs (see `formal-proposal.md`)
- `edge/` — notes for Jetson/edge

## Notes
- This repo uses a proprietary `LICENCE`. All contributions and usage must comply with it.
- Consider marking specific folders as permissively licensed later if you want broader adoption (open-core model).
