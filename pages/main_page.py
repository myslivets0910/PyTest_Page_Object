# https://stepik.org/lesson/238819/step/3?unit=211271

from selenium.webdriver.common.by import By
from pages.base_page import BasePage # импорт базового класса BasePage

class MainPage(BasePage):  #создайте класс  MainPage.
    # Его нужно сделать наследником класса BasePage. Класс-предок в Python указывается в скобках
    def go_to_login_page(self):
        #  В аргументы больше не надо передавать экземпляр браузера,
        #  мы его передаем и сохраняем на этапе создания Page Object.
        #  Вместо него нужно указать аргумент self , чтобы иметь доступ к атрибутам и методам класса
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        # Так как браузер у нас хранится как аргумент класса BasePage,
        # обращаться к нему нужно соответствующим образом с помощью self
        login_link.click()