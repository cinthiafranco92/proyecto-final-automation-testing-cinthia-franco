import pytest
from selenium.webdriver.common.by import By

from pages.products_page import ProductsPage

from utils.leer_datos import cargar_usuarios

from pages.login_page import LoginPage




@pytest.mark.parametrize(
    "caso",
    cargar_usuarios()
)
def test_login_parametrizado(driver, caso):

    login = LoginPage(driver)

    login.abrir_pagina()
    login.ingresar_usuario(caso["usuario"])
    login.ingresar_password(caso["clave"])
    login.hacer_login()

    if caso["resultado"] == "exito":
        assert "inventory.html" in driver.current_url

    else:
        mensaje = driver.find_element(
            By.CLASS_NAME, "error-message-container"
        ).text

        assert mensaje != ""

def test_login_page(driver):

    login = LoginPage(driver)

    login.abrir_pagina()
    login.ingresar_usuario("standard_user")
    login.ingresar_password("secret_sauce")
    login.hacer_login()

    assert "inventory.html" in driver.current_url



def test_verificar_inventario(logged_in_driver):
  
    productos = ProductsPage(logged_in_driver)

    titulo = productos.obtener_titulo()

    assert titulo == "Products"


# =================================================================================
# Actividad 2:Caso de prueba "Navegación y verificación del catálogo de productos"
# =================================================================================


def test_productos_visibles(logged_in_driver):


    productos = ProductsPage(logged_in_driver)

    lista_productos = productos.obtener_productos()

    assert len(lista_productos) > 0


def test_obtener_primer_producto(logged_in_driver):

    productos = ProductsPage(logged_in_driver)

    primer_producto = productos.obtener_primer_producto()

    assert primer_producto != ""



def test_validacion_interfaz(logged_in_driver):

    productos = ProductsPage(logged_in_driver)

    titulo = productos.obtener_titulo()
    lista_productos = productos.obtener_productos()

    assert titulo == "Products"
    assert len(lista_productos) > 0
  
# ================================================
# Actividad 3:Caso de prueba "Carrito de compras"
# ================================================

def test_add_product_to_cart(logged_in_driver):

    productos = ProductsPage(logged_in_driver)

    productos.agregar_primer_producto()

    contador = productos.obtener_contador_carrito()

    assert contador == "1"

def test_contador_carrito(logged_in_driver):

    productos = ProductsPage(logged_in_driver)

    productos.agregar_primer_producto()

    contador = productos.obtener_contador_carrito()

    assert contador == "1"


def test_navegar_carrito(logged_in_driver):

    productos = ProductsPage(logged_in_driver)

    productos.agregar_primer_producto()
    productos.abrir_carrito()

    assert "cart.html" in logged_in_driver.current_url


def test_verificar_producto_carrito(logged_in_driver):

    productos = ProductsPage(logged_in_driver)

    primer_producto = productos.obtener_primer_producto()

    productos.agregar_primer_producto()
    productos.abrir_carrito()

    producto_carrito = productos.obtener_producto_del_carrito()
    
    assert producto_carrito == primer_producto


