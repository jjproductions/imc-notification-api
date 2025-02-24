from pydantic import BaseModel, EmailStr, constr
from typing import List, Optional

class EmailInfo(BaseModel):
    subject: str
    body: str

class NotificationRequest(BaseModel):
    cardId: int
    email: EmailStr
    phoneNumber: Optional[constr]  # Assuming phone number length
    emailInfo: EmailInfo

class NotificationResponse(BaseModel):
    cardId: int
    email: str
    status: str  # "success" or "failure"
    message: Optional[str]  # Additional message in case of failure