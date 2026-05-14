from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.ticket import Ticket
from app.schemas.ticket import TicketCreate, TicketResponse
from typing import List
from uuid import UUID

router = APIRouter(prefix="/tickets", tags=["tickets"])

@router.post("/", response_model=TicketResponse)
def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    db_ticket = Ticket(
        sender_email=ticket.sender_email,
        subject=ticket.subject,
        body=ticket.body,
        status="pending"
    )
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

@router.get("/", response_model=List[TicketResponse])
def get_tickets(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    return db.query(Ticket).offset(skip).limit(limit).all()

@router.get("/{ticket_id}", response_model=TicketResponse)
def get_ticket(ticket_id: UUID, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket