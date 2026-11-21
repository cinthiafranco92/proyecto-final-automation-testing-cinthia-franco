# Proyecto Final - QA Automation Testing

## 1. Descripción del proyecto

Este proyecto consiste en la automatización de pruebas de software utilizando Python, Pytest y Selenium WebDriver para pruebas de interfaz de usuario (UI), y Requests para pruebas de API.

El objetivo es verificar el correcto funcionamiento de una aplicación web mediante pruebas automatizadas, validando escenarios positivos y negativos.

## 2. Tecnologías utilizadas

- Python 3.11
- Pytest
- Selenium WebDriver
- Requests
- Pytest-HTML
- Page Object Model (POM)
- JSON
- Git y GitHub

## 3. Pruebas de interfaz de usuario (UI)

Se realizaron pruebas automatizadas sobre el sitio SauceDemo.

Los escenarios incluyen:

- Verificación de la página de inicio de sesión.
- Validación del inventario.
- Verificación de productos visibles.
- Obtención del primer producto.
- Validación de elementos de la interfaz.
- Agregado de productos al carrito.
- Verificación del contador del carrito.
- Navegación hacia el carrito.
- Verificación del producto agregado.
- Pruebas parametrizadas de inicio de sesión utilizando datos externos en JSON.

## 4. Pruebas de API

Se realizaron pruebas automatizadas utilizando la API ReqRes y la librería Requests.

Se implementaron los siguientes escenarios:

- **GET:** obtener usuarios y validar la respuesta.
- **POST:** crear un usuario y verificar los datos recibidos.
- **DELETE:** eliminar un usuario y validar el código de respuesta.
- **GET negativo:** consultar un usuario inexistente y comprobar la respuesta 404.

Se validan los códigos de estado HTTP, el contenido y la estructura de las respuestas JSON.

## 5. Funcionalidades implementadas

- Patrón Page Object Model (POM).
- Fixtures de Pytest.
- Parametrización de pruebas.
- Lectura de datos externos desde archivos JSON.
- Capturas de pantalla cuando una prueba de interfaz falla.
- Registro de eventos mediante logging.
- Generación de reportes HTML con Pytest-HTML.
- Organización del proyecto mediante Git.

## 6. Estructura del proyecto

```text
proyecto-final-automation-testing-cinthia-franco/
│
├── data/
│   └── usuarios.json
│
├── logs/
│   └── automation.log
│
├── pages/
│   ├── login_page.py
│   └── products_page.py
│
├── reports/
│   ├── screens/
│   ├── reporte.html
│   └── reporte_api.html
│
├── tests/
│   └── test_saucedemo.py
│
├── tests_api/
│   └── test_api_usuarios.py
│
├── utils/
│   ├── leer_datos.py
│   ├── logger.py
│   └── helpers.py
│
├── conftest.py
├── pytest.ini
├── .gitignore
└── README.md
```

## 7. Instalación

Para instalar las dependencias necesarias, ejecutar:

```bash
pip install pytest selenium requests pytest-html
```

## 8. Ejecución de las pruebas

### Pruebas de interfaz (UI)

```bash
pytest tests -v
```

### Pruebas de API

```bash
pytest tests_api -v
```

### Ejecución de todas las pruebas

```bash
pytest tests tests_api -v
```

## 9. Generación de reportes

Para generar el reporte HTML de las pruebas de API:

```bash
pytest tests_api/test_api_usuarios.py -v --html=reports/reporte_api.html --self-contained-html
```

Los reportes HTML y las capturas de pantalla se almacenan en la carpeta `reports/`.

## 10. Sitios utilizados

- SauceDemo: https://www.saucedemo.com/
- ReqRes: https://reqres.in/

---

**Proyecto Final de QA Automation Testing**

Desarrollado con Python, Selenium WebDriver, Pytest y Requests.
