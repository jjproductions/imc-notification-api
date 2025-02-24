from pydantic import BaseModel, EmailStr

class EmailInfo(BaseModel):
    subject: str
    body: str

class NotificationRequest(BaseModel):
    cardId: int
    email: EmailStr
    phoneNumber: str
    emailInfo: EmailInfo