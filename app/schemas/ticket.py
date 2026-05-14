from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from uuid import UUID

class TicketCreate(BaseModel):
    sender_email: str
    subject: str
    body: str

class TicketResponse(BaseModel):
    id: UUID
    sender_email: str
    subject: str
    body: str
    category: Optional[str]
    urgency: Optional[str]
    confidence: Optional[float]
    status: str
    created_at: datetime

    class Config:
        from_attributes = True