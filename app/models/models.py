from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from uuid import UUID

class User(BaseModel):
    user_id: Optional[UUID] = None
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    birth_date: datetime
    admins: List["Admin"] = []
    passes: List["Pass_"] = []
    access_logs: List["AccessLog"] = []
    pass_requests: List["PassRequest"] = []

    class Config:
        orm_mode = True
        from_attributes = True

class Admin(BaseModel):
    admin_id: Optional[UUID] = None
    user_id: UUID
    position: str
    role: str

    class Config:
        orm_mode = True
        from_attributes = True

class AccessZone(BaseModel):
    zone_id: Optional[UUID] = None
    zone_name: str
    description: Optional[str] = None

    class Config:
        orm_mode = True
        from_attributes = True

class Pass_(BaseModel):
    pass_id: Optional[UUID] = None
    user_id: UUID
    zone_id: UUID
    pass_type: str
    issue_date: datetime
    expiry_date: datetime
    access_level: int

    class Config:
        orm_mode = True
        from_attributes = True

class AccessLog(BaseModel):
    log_id: Optional[UUID] = None
    user_id: UUID
    pass_id: UUID
    access_datetime: datetime
    access_type: str

    class Config:
        orm_mode = True
        from_attributes = True

class PassRequest(BaseModel):
    request_id: Optional[UUID] = None
    user_id: UUID
    request_date: datetime
    request_status: str
    approved: bool = False
    admin_id: Optional[UUID] = None

    class Config:
        orm_mode = True
        from_attributes = True
