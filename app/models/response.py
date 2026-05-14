from sqlalchemy import Column, String, Float, DateTime, Text, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid
from app.models.ticket import Base

class Response(Base):
    __tablename__ = "responses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    ticket_id = Column(UUID(as_uuid=True), ForeignKey("tickets.id"), nullable=False)
    draft = Column(Text, nullable=True)
    final = Column(Text, nullable=True)
    source_docs = Column(Text, nullable=True)
    approved_by = Column(String(255), nullable=True)
    tokens_used = Column(Float, default=0)
    cost_usd = Column(Float, default=0)
    cache_hit = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)