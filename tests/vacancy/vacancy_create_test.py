from datetime import datetime, date

import pytest

from vacancies.models import Skill


@pytest.mark.django_db
def test_create_vacancy(client, hr_token):
    expected_response = {
        "id": 1,
        "created": date.today().strftime("%Y-%m-%d"),
        "skills": [],
        "slug": "123",
        "name": "123",
        "text": "123",
        "status": "draft",
        # "is_archived": False,
        "min_experience": 1,
        "likes": 0,
        "update_at": None,
        "user": 1
    }

    data = {
        "slug": "123",
        "text": "123"
    }

    # Skill.objects.create(name="test")
    # data = {
    #     "skills": ["1"],
    #     "slug": "123",
    #     "name": "123",
    #     "text": "123",
    #     "status": "draft",
    #     "is_archived": False,
    #     "min_experience": 1,
    #     "user": 1
    # }
    response = client.post(
        "/vacancy/create/", data,
        content_type="application/json",
        HTTP_AUTHORIZATION="Token " + hr_token)

    # assert response.status_code == 201
    # assert response.data == expected_response

#
# @pytest.mark.django_db
# @pytest.mark.parametrize("status", ["open", "closed"])
# def test_vacancy_wrong_status(client, hr_token, status):
#     response = client.post("/vacancy/create/", data={
#         "skills": ["1"],
#         "slug": "123",
#         "name": "123",
#         "text": "123",
#         "status": status,
#         "is_archived": False,
#         "min_experience": 1
#     }, content_type="application/json", HTTP_AUTHORIZATION="Token " + hr_token)
#
#     assert response.status_code == 400
#     assert response.json() == {'status': ['Incorrect status']}