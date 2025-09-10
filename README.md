# Universal AGI with ADNA

**Mission:** Build a decentralized AI civilization where agents evolve independently, collaborate across local and global societies, and record their evolution on-chain via ADNA (Artificial DNA) and Proof of Evolution (PoE).

---

## 🔹 What is ADNA?
- 🧬 **ADNA**: Cryptographically verifiable “genetic memory” of models.
- 🗳️ **PoE**: Proof of Evolution — models that demonstrably improve can propose blocks.
- 🏘️ **AI Societies**: Local, offline-capable AI communities that sync and collaborate globally.
- 🌍 **Substrate Independent**: Runs on *any* compute (CPU, GPU, FPGA, edge boards, cloud, etc).  
  > Edge platforms like NVIDIA Jetson are examples, not requirements.

---

## 🔹 Whitepaper
See the full whitepaper: [Universal AGI with ADNA Combined.pdf](./Universal%20AGI%20with%20ADNA%20Combined.pdf)

---

## 🔹 Developer Quickstart
For a developer-focused guide, see [README.dev.md](./README.dev.md).

Basic usage:

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r node/requirements.txt

# Run local devnet
python node/devnet.py

# Run a mock agent
python node/agent.py --model tiny-llm --task benchmark/mnist.json --offline
