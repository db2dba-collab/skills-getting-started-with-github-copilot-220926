from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_duplicate_signup_for_same_activity_is_blocked():
    activity_name = "Chess Club"
    email = "new-duplicate-test@mergington.edu"

    first_response = client.post(
        f"/activities/{activity_name}/signup?email={email}"
    )
    assert first_response.status_code == 200

    second_response = client.post(
        f"/activities/{activity_name}/signup?email={email}"
    )

    assert second_response.status_code == 400
    assert "already" in second_response.json()["detail"].lower()
