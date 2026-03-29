from sqlalchemy import Column, BigInteger, String, Boolean, DateTime, ForeignKey, Text, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import JSONB
from app.core.database import Base


class Scan(Base):
    __tablename__ = "scans"

    id = Column(BigInteger, primary_key=True, index=True)
    user_id = Column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    image_path = Column(String, nullable=True)
    image_data = Column(Text, nullable=True)
    image_mime_type = Column(String(100), nullable=True)
    plant_name = Column(String(150), nullable=False)
    scientific_name = Column(String(200), nullable=True)
    disease_detected = Column(Boolean, nullable=False, default=False)
    disease_name = Column(String(150), nullable=True)
    confidence = Column(Numeric(5, 2), nullable=False)
    confidence_label = Column(String(50), nullable=True)
    severity = Column(String(50), nullable=True)
    description = Column(Text, nullable=True)
    treatment_json = Column(JSONB, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    user = relationship("User", back_populates="scans")