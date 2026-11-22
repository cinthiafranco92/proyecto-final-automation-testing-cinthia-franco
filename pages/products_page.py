from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import obtener_logger



class ProductsPage:

    INVENTORY_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    FIRST_PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    ADD_TO_CART_FIRST = (By.CLASS_NAME, "btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = obtener_logger("ProductsPage")

    def obtener_titulo(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.INVENTORY_TITLE)
        ).text

    def obtener_productos(self):
        self.wait.until(
            EC.visibility_of_element_located(self.INVENTORY_LIST)
        )

        productos = self.driver.find_elements(*self.INVENTORY_ITEMS)

        self.logger.info(
        f"Se encontraron {len(productos)} productos"
    )
        
        return productos

        

    def obtener_primer_producto(self):
        return self.driver.find_elements(
            *self.FIRST_PRODUCT_NAME
        )[0].text

    def agregar_primer_producto(self):
        self.driver.find_elements(
            *self.ADD_TO_CART_FIRST
        )[0].click()

        self.logger.info("Se agregó el primer producto al carrito")

    def obtener_contador_carrito(self):
        return self.driver.find_element(*self.CART_BADGE).text

    def abrir_carrito(self):
        self.driver.find_element(*self.CART_LINK).click()

        self.logger.info("Se abrió el carrito de compras")

    def obtener_producto_del_carrito(self):
        return self.wait.until(
        lambda driver: driver.find_element(
            By.CLASS_NAME, "inventory_item_name"
        ).text
    )