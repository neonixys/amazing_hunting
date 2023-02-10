from datetime import date

import pytest


@pytest.mark.django_db
def test_retrieve_vacancy(client, vacancy, hr_token):
    expected_response = {
        "created": date.today().strftime("%Y-%m-%d"),
        "id": vacancy.pk,
        "skills": [],
        "slug": "test",
        "status": "draft",
        "text": "test text",
        "min_experience": None,
        "likes": 0,
        "update_at": None,
        "user": vacancy.user_id
    }

    response = client.get(f"/vacancy/{vacancy.pk}/",
                          HTTP_AUTHORIZATION="Token " + hr_token)

    assert response.status_code == 200
    assert response.data == expected_response
