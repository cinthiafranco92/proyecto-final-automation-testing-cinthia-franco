import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pathlib import Path
from datetime import datetime

from utils.helpers import login_exitoso


@pytest.fixture(scope="function") #Se define un fixture de Pytest con alcance a nivel de función para inicializar y cerrar el navegador antes y después de cada prueba
def driver():
    # Inicialización del navegador Chrome
    service = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=service)
    
    yield navegador  # Se devuelve el objeto del navegador para su uso en las pruebas

    navegador.quit() # Cierre del navegador al finalizar el test 


@pytest.fixture
def logged_in_driver(driver):
    login_exitoso(driver)
    return driver






@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    resultado = yield
    report = resultado.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:
            carpeta = Path(__file__).parent / "reports" / "screens"
            carpeta.mkdir(parents=True, exist_ok=True)

            fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
            nombre = f"{item.name}_{fecha}.png"
            ruta = carpeta / nombre

            driver.save_screenshot(str(ruta))

            try:
                import pytest_html

                extras = getattr(report, "extras", [])
                extras.append(pytest_html.extras.image(str(ruta)))
                report.extras = extras

            except ImportError:
                print("pytest-html no está instalado.")