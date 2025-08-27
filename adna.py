import hashlib, json
from dataclasses import dataclass, asdict
from typing import List, Dict, Any

def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

@dataclass
class ADNA:
    model_id: str
    parent_ids: List[str]
    version: str
    created_at: str
    traits: Dict[str, Any]
    training: Dict[str, Any]
    fitness: Dict[str, float]
    zk_proof: str = ""
    signer: str = ""

    def to_json(self) -> str:
        return json.dumps(asdict(self), separators=(',', ':'), sort_keys=True)

    def commitment(self) -> str:
        return sha256_hex(self.to_json().encode())
