import datetime as dt

from src.managers.source_manager.domain import Login
from tests.service import create_test_sourcedata_service
from src.security import verify_password


class TestLogin:
    def test_insert_and_get_login(self):
        service = create_test_sourcedata_service()
        login = Login(username="user1", password="pass123")
        service.insert_login(login=login)
        retrieved = service.get_login_by_username(username="user1")
        assert retrieved is not None
        assert retrieved.username == "user1"
        assert verify_password("pass123", retrieved.password)
