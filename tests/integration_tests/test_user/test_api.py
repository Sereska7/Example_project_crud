import pytest
from httpx import AsyncClient


@pytest.mark.parametrize("email,password,status_code", [
    ("kot@pes.com", "kotopes", 200),
])
async def test_register_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post("/v1/register", json={
        "email": email,
        "password": password,
    })

    assert response.status_code == status_code


