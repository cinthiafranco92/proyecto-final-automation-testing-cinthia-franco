
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_obtener_todos_los_posts():
    response = requests.get(f"{BASE_URL}/posts")

    assert response.status_code == 200

    datos = response.json()

    assert isinstance(datos, list)
    assert len(datos) > 0


def test_obtener_post_por_id():
    response = requests.get(f"{BASE_URL}/posts/1")

    assert response.status_code == 200

    datos = response.json()

    assert datos["id"] == 1
    assert "title" in datos
    assert "body" in datos
    assert "userId" in datos


def test_crear_post():
    payload = {
        "title": "Proyecto QA Automation",
        "body": "Prueba automatizada con Python y Requests",
        "userId": 1
    }

    response = requests.post(
        f"{BASE_URL}/posts",
        json=payload
    )

    assert response.status_code == 201

    datos = response.json()

    assert datos["title"] == payload["title"]
    assert datos["body"] == payload["body"]
    assert datos["userId"] == payload["userId"]
    assert "id" in datos


def test_actualizar_post():
    payload = {
        "id": 1,
        "title": "Post actualizado",
        "body": "Contenido actualizado",
        "userId": 1
    }

    response = requests.put(
        f"{BASE_URL}/posts/1",
        json=payload
    )

    assert response.status_code == 200

    datos = response.json()

    assert datos["id"] == 1
    assert datos["title"] == payload["title"]
    assert datos["body"] == payload["body"]


def test_eliminar_post():
    response = requests.delete(f"{BASE_URL}/posts/1")

    assert response.status_code == 200
    assert response.json() == {}
