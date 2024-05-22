# tests/test_service.py

import pytest
from unittest.mock import MagicMock, patch
from uuid import uuid4
from datetime import datetime, timedelta

from app.models.models import User, Admin, Pass_, AccessZone, AccessLog, PassRequest
from app.services.services import UserService, AdminService, PassService, AccessZoneService, AccessLogService, PassRequestService

@pytest.fixture
def mock_user_repo():
    return MagicMock()

@pytest.fixture
def mock_admin_repo():
    return MagicMock()

@pytest.fixture
def mock_pass_repo():
    return MagicMock()

@pytest.fixture
def mock_access_zone_repo():
    return MagicMock()

@pytest.fixture
def mock_access_log_repo():
    return MagicMock()

@pytest.fixture
def mock_pass_request_repo():
    return MagicMock()

@pytest.fixture
def user_service(mock_user_repo):
    with patch('app.services.services.UserRepository', return_value=mock_user_repo):
        yield UserService()

@pytest.fixture
def admin_service(mock_admin_repo):
    with patch('app.services.services.AdminRepository', return_value=mock_admin_repo):
        yield AdminService()

@pytest.fixture
def pass_service(mock_pass_repo):
    with patch('app.services.services.PassRepository', return_value=mock_pass_repo):
        yield PassService()

@pytest.fixture
def access_zone_service(mock_access_zone_repo):
    with patch('app.services.services.AccessZoneRepository', return_value=mock_access_zone_repo):
        yield AccessZoneService()

@pytest.fixture
def access_log_service(mock_access_log_repo):
    with patch('app.services.services.AccessLogRepository', return_value=mock_access_log_repo):
        yield AccessLogService()

@pytest.fixture
def pass_request_service(mock_pass_request_repo, mock_pass_repo):
    with patch('app.services.services.PassRequestRepository', return_value=mock_pass_request_repo):
        with patch('app.services.services.PassRepository', return_value=mock_pass_repo):
            yield PassRequestService()

# Tests for UserService

def test_get_user(user_service, mock_user_repo):
    user_id = uuid4()
    mock_user = User(user_id=user_id, first_name="John", last_name="Doe", birth_date=datetime(1990, 1, 1))
    mock_user_repo.get_user.return_value = mock_user

    user = user_service.get_user(user_id)

    assert user.user_id == user_id
    mock_user_repo.get_user.assert_called_once_with(user_id)

def test_create_user(user_service, mock_user_repo):
    user_id = uuid4()
    user = User(user_id=user_id, first_name="John", last_name="Doe", birth_date=datetime(1990, 1, 1))
    mock_user_repo.create_user.return_value = user

    created_user = user_service.create_user(user)

    assert created_user.user_id == user_id
    mock_user_repo.create_user.assert_called_once_with(user)

def test_delete_user(user_service, mock_user_repo):
    user_id = uuid4()
    mock_user_repo.delete_user.return_value = True

    result = user_service.delete_user(user_id)

    assert result
    mock_user_repo.delete_user.assert_called_once_with(user_id)

# Tests for AdminService

def test_get_admin(admin_service, mock_admin_repo):
    admin_id = uuid4()
    mock_admin = Admin(admin_id=admin_id, user_id=uuid4(), position="Manager", role="Admin")
    mock_admin_repo.get_admin.return_value = mock_admin

    admin = admin_service.get_admin(admin_id)

    assert admin.admin_id == admin_id
    mock_admin_repo.get_admin.assert_called_once_with(admin_id)

def test_create_admin(admin_service, mock_admin_repo):
    admin_id = uuid4()
    admin = Admin(admin_id=admin_id, user_id=uuid4(), position="Manager", role="Admin")
    mock_admin_repo.create_admin.return_value = admin

    created_admin = admin_service.create_admin(admin)

    assert created_admin.admin_id == admin_id
    mock_admin_repo.create_admin.assert_called_once_with(admin)

def test_delete_admin(admin_service, mock_admin_repo):
    admin_id = uuid4()
    mock_admin_repo.delete_admin.return_value = True

    result = admin_service.delete_admin(admin_id)

    assert result
    mock_admin_repo.delete_admin.assert_called_once_with(admin_id)

def test_reject_pass_request(pass_request_service, mock_pass_request_repo):
    request_id = uuid4()
    admin_id = uuid4()
    pass_request = PassRequest(request_id=request_id, user_id=uuid4(), request_date=datetime.now(), request_status="Pending", approved=False)
    mock_pass_request_repo.reject_pass_request.return_value = pass_request

    result = pass_request_service.reject_pass_request(request_id, admin_id)

    assert result is not None
    mock_pass_request_repo.reject_pass_request.assert_called_once_with(request_id, admin_id)
