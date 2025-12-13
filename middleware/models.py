from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class CardDetection:
    rank: str            # "A", "2", ..., "10", "J", "Q", "K"
    suit: str            # "Hearts", "Spades", "Diamonds", "Clubs"
    confidence: float    # 0.0 - 1.0

    def to_json(self) -> dict:
        return asdict(self)


@dataclass
class ScanEvent:
    detection: Optional[CardDetection]
    source: str          # "android"
    success: bool
    message: str

    def to_json(self) -> dict:
        return {
            "success": self.success,
            "message": self.message,
            "source": self.source,
            "detection": (
                self.detection.to_json() if self.detection else None
            )
        }
