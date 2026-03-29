from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class DashboardItem(BaseModel):
    label: str
    count: int


class DashboardResponse(BaseModel):
    total_scans: int
    diseased_scans: int
    healthy_scans: int
    avg_confidence: float
    last_scan_at: Optional[datetime] = None
    top_plants: List[DashboardItem]
    top_diseases: List[DashboardItem]