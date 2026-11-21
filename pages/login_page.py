from selenium.webdriver.common.by import By
from utils.logger import obtener_logger


class LoginPage:


    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver
        self.logger = obtener_logger("LoginPage")

    def abrir_pagina(self):
        self.driver.get("https://www.saucedemo.com/")
        self.logger.info("Se abrió la página de SauceDemo")

    def ingresar_usuario(self, usuario):
        self.driver.find_element(
            *self.USERNAME
        ).send_keys(usuario)
        self.logger.info("Se ingresó el nombre de usuario")

    def ingresar_password(self, password):
        self.driver.find_element(
            *self.PASSWORD
        ).send_keys(password)

    def hacer_login(self):
        self.driver.find_element(
            *self.LOGIN_BUTTON
        ).click()
        self.logger.info("Se presionó el botón de inicio de sesión")


        