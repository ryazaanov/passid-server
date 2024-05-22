from sqlalchemy.orm import Session
from uuid import UUID
from datetime import datetime, timedelta
from app.repositories.repository import UserRepository, AdminRepository, PassRepository, AccessZoneRepository, AccessLogRepository, PassRequestRepository
from app.models.models import User, Admin, Pass_, AccessZone, AccessLog, PassRequest

class UserService:
    def __init__(self):
        self.user_repo = UserRepository()

    def get_user(self, user_id: UUID):
        return self.user_repo.get_user(user_id)

    def create_user(self, user: User):
        return self.user_repo.create_user(user)

    def delete_user(self, user_id: UUID):
        return self.user_repo.delete_user(user_id)

    def update_user(self, user_id: UUID, user: User):
        return self.user_repo.update_user(user_id, user)

class AdminService:
    def __init__(self):
        self.admin_repo = AdminRepository()

    def get_admin(self, admin_id: UUID):
        return self.admin_repo.get_admin(admin_id)

    def create_admin(self, admin: Admin):
        return self.admin_repo.create_admin(admin)

    def delete_admin(self, admin_id: UUID):
        return self.admin_repo.delete_admin(admin_id)

    def update_admin(self, admin_id: UUID, admin: Admin):
        return self.admin_repo.update_admin(admin_id, admin)

class PassService:
    def __init__(self):
        self.pass_repo = PassRepository()

    def get_pass(self, pass_id: UUID):
        return self.pass_repo.get_pass(pass_id)

    def create_pass(self, pass_: Pass_):
        return self.pass_repo.create_pass(pass_)

    def delete_pass(self, pass_id: UUID):
        return self.pass_repo.delete_pass(pass_id)

    def update_pass(self, pass_id: UUID, pass_: Pass_):
        return self.pass_repo.update_pass(pass_id, pass_)

class AccessZoneService:
    def __init__(self):
        self.access_zone_repo = AccessZoneRepository()

    def get_access_zone(self, zone_id: UUID):
        return self.access_zone_repo.get_access_zone(zone_id)

    def create_access_zone(self, access_zone: AccessZone):
        return self.access_zone_repo.create_access_zone(access_zone)

    def delete_access_zone(self, zone_id: UUID):
        return self.access_zone_repo.delete_access_zone(zone_id)

    def update_access_zone(self, zone_id: UUID, access_zone: AccessZone):
        return self.access_zone_repo.update_access_zone(zone_id, access_zone)

class AccessLogService:
    def __init__(self):
        self.access_log_repo = AccessLogRepository()

    def get_access_log(self, log_id: UUID):
        return self.access_log_repo.get_access_log(log_id)

    def create_access_log(self, access_log: AccessLog):
        return self.access_log_repo.create_access_log(access_log)

class PassRequestService:
    def __init__(self):
        self.pass_request_repo = PassRequestRepository()
        self.pass_repo = PassRepository()

    def create_pass_request(self, pass_request: PassRequest):
        return self.pass_request_repo.create_pass_request(pass_request)

    def get_pass_request(self, request_id: UUID):
        return self.pass_request_repo.get_pass_request(request_id)

    def approve_pass_request(self, request_id: UUID, admin_id: UUID, zone_id: UUID, pass_type: str, access_level: int):
        pass_request = self.pass_request_repo.approve_pass_request(request_id, admin_id)
        if pass_request and pass_request.approved:
            pass_obj = Pass_(
                user_id=pass_request.user_id,
                zone_id=zone_id,
                pass_type=pass_type,
                issue_date=datetime.now(),
                expiry_date=datetime.now() + timedelta(days=30),
                access_level=access_level
            )
            return self.pass_repo.create_pass(pass_obj)
        return None

    def reject_pass_request(self, request_id: UUID, admin_id: UUID):
        return self.pass_request_repo.reject_pass_request(request_id, admin_id)
