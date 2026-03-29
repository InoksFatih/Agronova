from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class TreatmentResponse(BaseModel):
    curative: List[str] = Field(default_factory=list)
    preventive: List[str] = Field(default_factory=list)
    care_tips: List[str] = Field(default_factory=list)


class ScanResponse(BaseModel):
    id: int
    image_path: Optional[str] = None
    image_data: Optional[str] = None
    image_mime_type: Optional[str] = None
    plant_name: str
    scientific_name: Optional[str] = None
    disease_detected: bool
    disease_name: Optional[str] = None
    confidence: float
    confidence_label: Optional[str] = None
    severity: Optional[str] = None
    description: Optional[str] = None
    treatment_json: Optional[TreatmentResponse] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True