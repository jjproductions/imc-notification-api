from fastapi import APIRouter, HTTPException, Depends, Header
from pydantic import BaseModel
from typing import List, Dict
from .utils import send_email, send_sms, verify_api_key, verify_card_id_email

router = APIRouter()

class EmailInfo(BaseModel):
    subject: str
    body: str

class NotificationRequest(BaseModel):
    cardId: int
    email: str
    phoneNumber: str
    emailInfo: EmailInfo

class NotificationResponse(BaseModel):
    cardId: int
    email: str
    status: str

@router.post("/send-notifications", response_model=List[NotificationResponse])
async def send_notifications(
    notifications: List[NotificationRequest],
    api_key: str = Header(...)
):
    if not verify_api_key(api_key):
        raise HTTPException(status_code=403, detail="Invalid API key")

    responses = []
    
    for notification in notifications:
        if verify_card_id_email(notification.cardId, notification.email):
            email_status = send_email(notification.emailInfo.subject, notification.emailInfo.body, notification.email)
            # sms_status = send_sms(notification.phoneNumber, notification.emailInfo.body)
            if email_status:
                responses.append(NotificationResponse(cardId=notification.cardId, email=notification.email, status="Success"))
            else:
                responses.append(NotificationResponse(cardId=notification.cardId, email=notification.email, status="Failed to send email"))
        else:
            responses.append(NotificationResponse(cardId=notification.cardId, email=notification.email, status="Card ID and email do not match"))

    return responses