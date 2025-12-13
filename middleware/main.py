from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from models import CardDetection, ScanEvent
from backend_client import BackendClient

# ---------- App ----------

app = FastAPI(title="CV Middleware", version="0.1")

# backend = BackendClient(base_url="http://localhost:8080")


# ---------- API DTOs ----------

class CardDetectionDTO(BaseModel):
    rank: str
    suit: str
    confidence: float


class ScanEventDTO(BaseModel):
    source: str
    success: bool
    message: str
    detection: Optional[CardDetectionDTO] = None


# ---------- Routes ----------

@app.post("/scan")
def receive_scan(event: ScanEventDTO):
    """
    Receives a card detection event and forwards it to the backend.
    """

    # No detection → nothing to do
    if not event.detection:
        return {
            "success": False,
            "message": "no card detected",
            "detection": event.detection.dict() if event.detection else None
        }

    # DTO → domain model
    detection = CardDetection(
        rank=event.detection.rank,
        suit=event.detection.suit,
        confidence=event.detection.confidence
    )

    # --- TESTING: bypass backend ---
    # Just return a fake backend response to avoid blocking
    return {
        "success": True,
        "message": "card received (backend bypassed)",
        "backend_response": {"status": "ok", "id": 123},  # dummy data
        "detection": detection.to_json()
    }

    """
    # Send to backend
    backend_response = backend.send_card(detection)

    # Backend unreachable or error
    if backend_response is None:
        return {
            "success": False,
            "message": "backend unavailable",
            "detection": detection.to_json()
        }

    # Success
    return {
        "success": True,
        "message": "card forwarded",
        "backend_response": backend_response,
        "detection": detection.to_json()
    }
    """