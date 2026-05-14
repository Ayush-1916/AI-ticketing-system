from sqlalchemy import Column, String, Float, DateTime, Text, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid
import enum

Base = declarative_base()

class TicketStatus(str, enum.Enum):
    pending = "pending"
    auto_handled = "auto_handled"
    escalated = "escalated"
    resolved = "resolved"

class UrgencyLevel(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    sender_email = Column(String(255), nullable=False)
    subject = Column(String(500), nullable=False)
    body = Column(Text, nullable=False)
    category = Column(String(100), nullable=True)
    urgency = Column(String(50), nullable=True)
    confidence = Column(Float, nullable=True)
    status = Column(String(50), default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)