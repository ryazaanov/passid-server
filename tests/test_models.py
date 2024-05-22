# tests/test_models.py

import pytest
from pydantic import ValidationError
from app.models.models import User, Admin, AccessZone, Pass_, AccessLog, PassRequest
from uuid import uuid4
from datetime import datetime

def test_user_model():
    user_id = uuid4()
    birth_date = datetime(1990, 1, 1)
    user = User(
        user_id=user_id,
        first_name="John",
        last_name="Doe",
        birth_date=birth_date
    )

    assert user.user_id == user_id
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.middle_name is None
    assert user.birth_date == birth_date
    assert user.admins == []
    assert user.passes == []
    assert user.access_logs == []
    assert user.pass_requests == []

def test_admin_model():
    admin_id = uuid4()
    user_id = uuid4()
    admin = Admin(
        admin_id=admin_id,
        user_id=user_id,
        position="Manager",
        role="Admin"
    )

    assert admin.admin_id == admin_id
    assert admin.user_id == user_id
    assert admin.position == "Manager"
    assert admin.role == "Admin"

def test_access_zone_model():
    zone_id = uuid4()
    access_zone = AccessZone(
        zone_id=zone_id,
        zone_name="Main Entrance",
        description="The main entrance to the building"
    )

    assert access_zone.zone_id == zone_id
    assert access_zone.zone_name == "Main Entrance"
    assert access_zone.description == "The main entrance to the building"

def test_pass_model():
    pass_id = uuid4()
    user_id = uuid4()
    zone_id = uuid4()
    issue_date = datetime.now()
    expiry_date = datetime(2025, 1, 1)
    pass_ = Pass_(
        pass_id=pass_id,
        user_id=user_id,
        zone_id=zone_id,
        pass_type="Temporary",
        issue_date=issue_date,
        expiry_date=expiry_date,
        access_level=1
    )

    assert pass_.pass_id == pass_id
    assert pass_.user_id == user_id
    assert pass_.zone_id == zone_id
    assert pass_.pass_type == "Temporary"
    assert pass_.issue_date == issue_date
    assert pass_.expiry_date == expiry_date
    assert pass_.access_level == 1

def test_access_log_model():
    log_id = uuid4()
    user_id = uuid4()
    pass_id = uuid4()
    access_datetime = datetime.now()
    access_log = AccessLog(
        log_id=log_id,
        user_id=user_id,
        pass_id=pass_id,
        access_datetime=access_datetime,
        access_type="Entry"
    )

    assert access_log.log_id == log_id
    assert access_log.user_id == user_id
    assert access_log.pass_id == pass_id
    assert access_log.access_datetime == access_datetime
    assert access_log.access_type == "Entry"

def test_pass_request_model():
    request_id = uuid4()
    user_id = uuid4()
    request_date = datetime.now()
    pass_request = PassRequest(
        request_id=request_id,
        user_id=user_id,
        request_date=request_date,
        request_status="Pending",
        approved=False
    )

    assert pass_request.request_id == request_id
    assert pass_request.user_id == user_id
    assert pass_request.request_date == request_date
    assert pass_request.request_status == "Pending"
    assert not pass_request.approved
    assert pass_request.admin_id is None

def test_user_model_invalid_data():
    with pytest.raises(ValidationError):
        User(
            first_name="John",
            last_name="Doe",
            birth_date="invalid-date"
        )
