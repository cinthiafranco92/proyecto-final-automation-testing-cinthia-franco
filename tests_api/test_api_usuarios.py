
import requests


def test_obtener_usuarios():

    url = "https://reqres.in/api/users?page=2"

    respuesta = requests.get(url)

    # Validar código HTTP
    assert respuesta.status_code == 200

    # Convertir respuesta a JSON
    datos = respuesta.json()

    assert "data" in datos
    assert isinstance(datos["data"], list)
    assert len(datos["data"]) > 0

    # Validar contenido
    assert datos["page"] == 2
    assert len(datos["data"]) > 0

    print(datos)




def test_crear_usuario():

    url = "https://reqres.in/api/users"

    usuario = {
        "name": "Matias QA",
        "job": "tester"
    }

    respuesta = requests.post(url, json=usuario)

    # Validar código HTTP
    assert respuesta.status_code == 201

    # Obtener respuesta JSON
    datos = respuesta.json()

    # Validar los datos
    assert datos["name"] == "Matias QA"
    assert datos["job"] == "tester"
    assert "id" in datos
    assert "createdAt" in datos
    assert isinstance(datos["id"], str)




def test_eliminar_usuario():

    url = "https://reqres.in/api/users/2"

    respuesta = requests.delete(url)

    # Validar código HTTP
    assert respuesta.status_code == 204

    # Validar que la respuesta no tenga contenido
    assert respuesta.text == ""




def test_usuario_no_existente():
    url = "https://reqres.in/api/users/999"

    respuesta = requests.get(url)

    assert respuesta.status_code == 404