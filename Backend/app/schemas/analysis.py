from pydantic import BaseModel, Field
from typing import Optional, List


class Treatment(BaseModel):
    curative: List[str] = Field(default_factory=list)
    preventive: List[str] = Field(default_factory=list)
    care_tips: List[str] = Field(default_factory=list)


class AnalysisResponse(BaseModel):
    plant_name: str
    scientific_name: Optional[str] = None
    disease_detected: bool
    disease_name: Optional[str] = None
    confidence: float
    confidence_label: str
    severity: Optional[str] = None
    description: Optional[str] = None
    treatment: Treatment


class ErrorResponse(BaseModel):
    error: str
    detail: str