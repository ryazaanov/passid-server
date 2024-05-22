from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.database import get_db
from app.models.models import User, Admin, Pass_, AccessZone, AccessLog, PassRequest
from app.services.services import UserService, AdminService, PassService, AccessZoneService, AccessLogService, PassRequestService

app = FastAPI()

# Конечные точки для пользователя
@app.get("/users/{user_id}")
def get_user(user_id: UUID, service: UserService = Depends(UserService)):
    user = service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user

@app.post("/users/")
def create_user(user: User, service: UserService = Depends(UserService)):
    return service.create_user(user)

@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: UUID, service: UserService = Depends(UserService)):
    if not service.delete_user(user_id):
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return

@app.put("/users/{user_id}")
def update_user(user_id: UUID, user: User, service: UserService = Depends(UserService)):
    updated_user = service.update_user(user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return updated_user

# Конечные точки для администратора
@app.get("/admins/{admin_id}")
def get_admin(admin_id: UUID, service: AdminService = Depends(AdminService)):
    admin = service.get_admin(admin_id)
    if not admin:
        raise HTTPException(status_code=404, detail="Администратор не найден")
    return admin

@app.post("/admins/")
def create_admin(admin: Admin, service: AdminService = Depends(AdminService)):
    return service.create_admin(admin)

@app.delete("/admins/{admin_id}", status_code=204)
def delete_admin(admin_id: UUID, service: AdminService = Depends(AdminService)):
    if not service.delete_admin(admin_id):
        raise HTTPException(status_code=404, detail="Администратор не найден")
    return

@app.put("/admins/{admin_id}")
def update_admin(admin_id: UUID, admin: Admin, service: AdminService = Depends(AdminService)):
    updated_admin = service.update_admin(admin_id, admin)
    if not updated_admin:
        raise HTTPException(status_code=404, detail="Администратор не найден")
    return updated_admin

# Конечные точки для пропусков
@app.get("/passes/{pass_id}")
def get_pass(pass_id: UUID, service: PassService = Depends(PassService)):
    pass_ = service.get_pass(pass_id)
    if not pass_:
        raise HTTPException(status_code=404, detail="Пропуск не найден")
    return pass_

@app.post("/passes/")
def create_pass(pass_: Pass_, service: PassService = Depends(PassService)):
    return service.create_pass(pass_)

@app.delete("/passes/{pass_id}", status_code=204)
def delete_pass(pass_id: UUID, service: PassService = Depends(PassService)):
    if not service.delete_pass(pass_id):
        raise HTTPException(status_code=404, detail="Пропуск не найден")
    return

@app.put("/passes/{pass_id}")
def update_pass(pass_id: UUID, pass_: Pass_, service: PassService = Depends(PassService)):
    updated_pass = service.update_pass(pass_id, pass_)
    if not updated_pass:
        raise HTTPException(status_code=404, detail="Пропуск не найден")
    return updated_pass

# Конечные точки для зон доступа
@app.get("/access_zones/{zone_id}")
def get_access_zone(zone_id: UUID, service: AccessZoneService = Depends(AccessZoneService)):
    access_zone = service.get_access_zone(zone_id)
    if not access_zone:
        raise HTTPException(status_code=404, detail="Зона доступа не найдена")
    return access_zone

@app.post("/access_zones/")
def create_access_zone(access_zone: AccessZone, service: AccessZoneService = Depends(AccessZoneService)):
    return service.create_access_zone(access_zone)

@app.delete("/access_zones/{zone_id}", status_code=204)
def delete_access_zone(zone_id: UUID, service: AccessZoneService = Depends(AccessZoneService)):
    if not service.delete_access_zone(zone_id):
        raise HTTPException(status_code=404, detail="Зона доступа не найдена")
    return

@app.put("/access_zones/{zone_id}")
def update_access_zone(zone_id: UUID, access_zone: AccessZone, service: AccessZoneService = Depends(AccessZoneService)):
    updated_access_zone = service.update_access_zone(zone_id, access_zone)
    if not updated_access_zone:
        raise HTTPException(status_code=404, detail="Зона доступа не найдена")
    return updated_access_zone

# Конечные точки для журнала доступа
@app.get("/access_logs/{log_id}")
def get_access_log(log_id: UUID, service: AccessLogService = Depends(AccessLogService)):
    access_log = service.get_access_log(log_id)
    if not access_log:
        raise HTTPException(status_code=404, detail="Журнал доступа не найден")
    return access_log

@app.post("/access_logs/")
def create_access_log(access_log: AccessLog, service: AccessLogService = Depends(AccessLogService)):
    return service.create_access_log(access_log)

# Конечные точки для запросов на пропуск
@app.post("/pass_requests/")
def create_pass_request(pass_request: PassRequest, service: PassRequestService = Depends(PassRequestService)):
    return service.create_pass_request(pass_request)

@app.get("/pass_requests/{request_id}")
def get_pass_request(request_id: UUID, service: PassRequestService = Depends(PassRequestService)):
    pass_request = service.get_pass_request(request_id)
    if not pass_request:
        raise HTTPException(status_code=404, detail="Запрос на пропуск не найден")
    return pass_request

@app.put("/pass_requests/{request_id}/approve")
def approve_pass_request(request_id: UUID, admin_id: UUID, zone_id: UUID, pass_type: str, access_level: int,  service: PassRequestService = Depends(PassRequestService)):
    approved_pass_request = service.approve_pass_request(request_id, admin_id, zone_id, pass_type, access_level)
    if not approved_pass_request:
        raise HTTPException(status_code=404, detail="Запрос на пропуск не найден или не одобрен")
    return approved_pass_request

@app.put("/pass_requests/{request_id}/reject")
def reject_pass_request(request_id: UUID, admin_id: UUID, service: PassRequestService = Depends(PassRequestService)):
    rejected_pass_request = service.reject_pass_request(request_id, admin_id)
    if not rejected_pass_request:
        raise HTTPException(status_code=404, detail="Запрос на пропуск не найден или не отклонен")
    return rejected_pass_request
