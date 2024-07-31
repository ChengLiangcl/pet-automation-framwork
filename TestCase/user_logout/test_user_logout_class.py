import json
import pytest
import allure
from Models.users import User


@pytest.mark.run(order=5)
class TestUserLogout:
    @allure.title(""""
                Scenario: User logout
                Given an existing user
                When the user click logout button
                Then the user should be logged out the system successfully 
                """)
    def test_user_log_out(self):
        user = User
        response = user.logout()
        assert response['status_code'] == 200

