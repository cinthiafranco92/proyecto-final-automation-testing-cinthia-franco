# 🚀 Proyecto Final - QA Automation Testing

**Automatización de pruebas de interfaz de usuario (UI) y API utilizando Python, Selenium WebDriver, Pytest y Requests.**

## 👩‍💻 Descripción del proyecto

Este proyecto consiste en el desarrollo de un framework de automatización de pruebas de software utilizando Python.

Se implementaron pruebas automatizadas de interfaz de usuario (UI) sobre la aplicación SauceDemo mediante Selenium WebDriver y Pytest, y pruebas de API utilizando Requests y JSONPlaceholder.

El objetivo principal es validar el correcto funcionamiento de una aplicación web mediante escenarios positivos y negativos, aplicando buenas prácticas de automatización, organización del código y reutilización de componentes.

## 🛠️ Tecnologías y herramientas

| Tecnología | Utilización |
|---|---|
| Python 3.11 | Lenguaje de programación |
| Pytest | Framework de testing |
| Selenium WebDriver | Automatización de interfaz web |
| Requests | Automatización de pruebas API |
| Pytest-HTML | Generación de reportes HTML |
| Page Object Model (POM) | Patrón de diseño |
| JSON | Almacenamiento de datos de prueba |
| Logging | Registro de eventos |
| Git y GitHub | Control de versiones |

## 🧪 1. Pruebas de interfaz de usuario (UI)

Se realizaron pruebas automatizadas sobre [SauceDemo](https://www.saucedemo.com/).

### Escenarios implementados

- Verificación de la página de inicio de sesión.
- Validación del inventario.
- Verificación de productos visibles.
- Obtención del primer producto.
- Validación de elementos de la interfaz.
- Agregado de productos al carrito.
- Verificación del contador del carrito.
- Navegación hacia el carrito.
- Verificación del producto agregado.
- Pruebas parametrizadas de inicio de sesión con diferentes usuarios.

### Técnicas aplicadas

- Selenium WebDriver.
- Localizadores mediante By.
- Esperas explícitas con WebDriverWait.
- Page Object Model (POM).
- Fixtures de Pytest.
- Parametrización de pruebas.
- Lectura de datos externos desde JSON.

## 🌐 2. Pruebas de API

Se implementaron pruebas automatizadas utilizando la librería Requests y la API pública [JSONPlaceholder](https://jsonplaceholder.typicode.com/).

**Endpoint base:**

`https://jsonplaceholder.typicode.com`

### Escenarios implementados

| Método HTTP | Endpoint | Validación |
|---|---|---|
| GET | /posts | Obtener todos los posts |
| GET | /posts/1 | Consultar un post por ID |
| POST | /posts | Crear un post |
| PUT | /posts/1 | Actualizar un post |
| DELETE | /posts/1 | Eliminar un post |

### Validaciones realizadas

- Códigos de estado HTTP.
- Estructura y contenido de respuestas JSON.
- Validación de campos obligatorios.
- Comparación de datos enviados y recibidos.
- Verificación de respuestas exitosas.

**Nota:** JSONPlaceholder es una API de prueba que simula operaciones de escritura. Las operaciones POST, PUT y DELETE no modifican permanentemente los datos almacenados.

## ⚙️ 3. Funcionalidades implementadas

- Patrón de diseño Page Object Model (POM).
- Fixtures para administrar el WebDriver.
- Parametrización de casos de prueba.
- Lectura de datos externos desde archivos JSON.
- Capturas de pantalla ante fallos en pruebas UI.
- Registro de eventos mediante Logging.
- Generación de reportes HTML.
- Separación de pruebas UI y API.
- Organización del proyecto mediante Git y GitHub.

## 📁 4. Estructura del proyecto

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
│   ├── reporte_api.html
│   └── reporte.html
│
├── tests/
│   └── test_saucedemo.py
│
├── tests_api/
│   └── test_api_usuarios.py
│
├── utils/
│   ├── helpers.py
│   ├── leer_datos.py
│   └── logger.py
│
├── .gitignore
├── conftest.py
├── pytest.ini
└── README.md
```

## 💻 5. Instalación y configuración

### Requisitos previos

- Python 3.11.
- Google Chrome.
- Visual Studio Code (recomendado).
- Git.

### Instalar dependencias

Desde la terminal, ejecutar:

```bash
python -m pip install pytest selenium requests pytest-html
```

## ▶️ 6. Ejecución de las pruebas

### Ejecutar pruebas de interfaz (UI)

```bash
pytest tests -v
```

### Ejecutar pruebas de API

```bash
pytest tests_api -v
```

### Ejecutar todas las pruebas

```bash
pytest tests tests_api -v
```

## 📊 7. Reportes de ejecución

El proyecto utiliza Pytest-HTML para generar reportes visuales de los resultados.

### Reporte de pruebas UI

```bash
pytest tests -v --html=reports/reporte.html --self-contained-html
```

### Reporte de pruebas API

```bash
pytest tests_api -v --html=reports/reporte_api.html --self-contained-html
```

### Reporte general

```bash
pytest tests tests_api -v --html=reports/reporte.html --self-contained-html
```

Los reportes se generan en la carpeta `reports/`.

Las capturas de pantalla de pruebas fallidas se almacenan en `reports/screens/`.

## ✅ 8. Resultados de las pruebas

En la última ejecución completa del proyecto se obtuvieron los siguientes resultados:

| Tipo de prueba | Resultado |
|---|---:|
| UI y login | 12 PASSED |
| API | 5 PASSED |
| **Total** | **17 PASSED** |
| Fallidas | 0 |

**Resultado: 17 pruebas aprobadas de 17 ejecutadas.**

## 🔗 9. Aplicaciones utilizadas

- [SauceDemo](https://www.saucedemo.com/) - Aplicación web utilizada para las pruebas de interfaz.
- [JSONPlaceholder](https://jsonplaceholder.typicode.com/) - API REST utilizada para las pruebas automatizadas.

## 🎯 10. Objetivo profesional

Este proyecto forma parte de mi formación en QA Automation Testing y demuestra la aplicación práctica de conocimientos de Python, automatización de pruebas UI y API, diseño POM, parametrización, manejo de datos y generación de reportes.

---

**Proyecto Final - QA Automation Testing**

Desarrollado con Python | Selenium WebDriver | Pytest | Requests | JSONPlaceholder

**GitHub:** [proyecto-final-automation-testing-cinthia-franco](https://github.com/cinthiafranco92/proyecto-final-automation-testing-cinthia-franco)

