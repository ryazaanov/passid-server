# combined_service/app/repository.py
from uuid import UUID
from sqlalchemy.orm import Session
from app.schemas.schema import UserSchema, AdminSchema, AccessZoneSchema, AccessLogSchema, PassRequestSchema, PassSchema
from app.models.models import User, Admin, AccessZone, AccessLog, PassRequest, Pass_
from app.database import get_db

class UserRepository:
    
    db: Session

    def __init__(self):
        self.db = next(get_db())

    def get_user(self, user_id: UUID):
        db_user = self.db.query(UserSchema).filter(UserSchema.user_id == user_id).first()
        return User.from_orm(db_user) if db_user else None

    def get_users(self):
        db_users = self.db.query(UserSchema).all()
        return [User.from_orm(user) for user in db_users]

    def create_user(self, user: User):
        db_user = UserSchema(**user.dict())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return User.from_orm(db_user)
    
    def delete_user(self, user_id: UUID):
        self.db.query(UserSchema).filter(UserSchema.user_id == user_id).delete()
        self.db.commit()
        return True
    
    def update_user(self, user_id: UUID, user: User):
        db_user = self.db.query(UserSchema).filter(UserSchema.user_id == user_id).first()
        if not db_user:
            return None
        for key, value in user.dict().items():
            setattr(db_user, key, value)
        self.db.commit()
        self.db.refresh(db_user)
        return User.from_orm(db_user)

class AdminRepository:

    db: Session

    def __init__(self):
        self.db = next(get_db())

    def get_admin(self, admin_id: UUID):
        db_admin = self.db.query(AdminSchema).filter(AdminSchema.admin_id == admin_id).first()
        return Admin.from_orm(db_admin) if db_admin else None

    def create_admin(self, admin: Admin):
        db_admin = AdminSchema(**admin.dict())
        self.db.add(db_admin)
        self.db.commit()
        self.db.refresh(db_admin)
        return Admin.from_orm(db_admin)
    
    def delete_admin(self, admin_id: UUID):
        self.db.query(AdminSchema).filter(AdminSchema.admin_id == admin_id).delete()
        self.db.commit()
        return True
    
    def update_admin(self, admin_id: UUID, admin: Admin):
        db_admin = self.db.query(AdminSchema).filter(AdminSchema.admin_id == admin_id).first()
        if not db_admin:
            return None
        for key, value in admin.dict().items():
            setattr(db_admin, key, value)
        self.db.commit()
        self.db.refresh(db_admin)
        return Admin.from_orm(db_admin)
                
class PassRepository:

    db: Session

    def __init__(self):
        self.db = next(get_db())

    def get_pass(self, pass_id: UUID):
        db_pass = self.db.query(PassSchema).filter(PassSchema.pass_id == pass_id).first()
        return Pass_.from_orm(db_pass) if db_pass else None
    
    def get_passes(self):
        db_passes = self.db.query(PassSchema).all()
        return [Pass_.from_orm(pass_) for pass_ in db_passes]

    def create_pass(self, pass_: Pass_):
        db_pass = PassSchema(**pass_.dict())
        self.db.add(db_pass)
        self.db.commit()
        self.db.refresh(db_pass)
        return Pass_.from_orm(db_pass)
    
    def delete_pass(self, pass_id: UUID):
        self.db.query(PassSchema).filter(PassSchema.pass_id == pass_id).delete()
        self.db.commit()
        return True
    
    def update_pass(self, pass_id: UUID, pass_: Pass_):
        db_pass = self.db.query(PassSchema).filter(PassSchema.pass_id == pass_id).first()
        if not db_pass:
            return None
        for key, value in pass_.dict().items():
            setattr(db_pass, key, value)
        self.db.commit()
        self.db.refresh(db_pass)
        return Pass_.from_orm(db_pass)

class AccessZoneRepository:

    db: Session

    def __init__(self):
        self.db = next(get_db())

    def get_access_zone(self, zone_id: UUID):
        db_access_zone = self.db.query(AccessZoneSchema).filter(AccessZoneSchema.zone_id == zone_id).first()
        return AccessZone.from_orm(db_access_zone) if db_access_zone else None

    def create_access_zone(self, access_zone: AccessZone):
        db_access_zone = AccessZoneSchema(**access_zone.dict())
        self.db.add(db_access_zone)
        self.db.commit()
        self.db.refresh(db_access_zone)
        return AccessZone.from_orm(db_access_zone)
    
    def delete_access_zone(self, zone_id: UUID):
        self.db.query(AccessZoneSchema).filter(AccessZoneSchema.zone_id == zone_id).delete()
        self.db.commit()
        return True
                
    def update_access_zone(self, zone_id: UUID, access_zone: AccessZone):
        db_access_zone = self.db.query(AccessZoneSchema).filter(AccessZoneSchema.zone_id == zone_id).first()
        if not db_access_zone:
            return None
        for key, value in access_zone.dict().items():
            setattr(db_access_zone, key, value)
        self.db.commit()
        self.db.refresh(db_access_zone)
        return AccessZone.from_orm(db_access_zone)

class AccessLogRepository:

    db: Session

    def __init__(self):
        self.db = next(get_db())

    def get_access_log(self, log_id: UUID):
        db_access_log = self.db.query(AccessLogSchema).filter(AccessLogSchema.log_id == log_id).first()
        return AccessLog.from_orm(db_access_log) if db_access_log else None

    def create_access_log(self, access_log: AccessLog):
        db_access_log = AccessLogSchema(**access_log.dict())
        self.db.add(db_access_log)
        self.db.commit()
        self.db.refresh(db_access_log)
        return AccessLog.from_orm(db_access_log)

class PassRequestRepository:

    db: Session

    def __init__(self):
        self.db = next(get_db())

    def get_pass_request(self, request_id: UUID):
        db_pass_request = self.db.query(PassRequestSchema).filter(PassRequestSchema.request_id == request_id).first()
        return PassRequest.from_orm(db_pass_request) if db_pass_request else None

    def create_pass_request(self, pass_request: PassRequest):
        db_pass_request = PassRequestSchema(**pass_request.dict())
        self.db.add(db_pass_request)
        self.db.commit()
        self.db.refresh(db_pass_request)
        return PassRequest.from_orm(db_pass_request)
    
    def approve_pass_request(self, request_id: UUID, admin_id: UUID):
        pass_request = self.get_pass_request(request_id)
        if pass_request:
            pass_request.request_status = "approved"
            pass_request.approved = True
            pass_request.admin_id = admin_id
            self.db.commit()
            self.db.refresh(pass_request)
        return PassRequest.from_orm(pass_request)

    def reject_pass_request(self, request_id: UUID):
        pass_request = self.get_pass_request(request_id)
        if pass_request:
            pass_request.request_status = "rejected"
            pass_request.approved = False
            self.db.commit()
            self.db.refresh(pass_request)
        return PassRequest.from_orm(pass_request)
