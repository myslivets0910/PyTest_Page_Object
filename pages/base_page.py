from selenium.webdriver.common.by import By

class BasePage(object): # cоздаем новый класс BasePage, который наследует от базового класса object

    def __init__(self, browser, url): #Это метод инициализации (конструктор) класса. Он принимает два параметра — browser и url
        """Конструктор класса.
        :param browser:
        :param url:
        """
        # Это строка документации (докстринг), которая объясняет, что делают параметры browser и url
        self.browser = browser # сохраняем переданные параметры browser и url как атрибуты экземпляра класса.
        self.url = url

    def open(self):
        """метод открывает нужную страницу,
        используя метод get()
        """
        self.browser.get(self.url) # # определяем метод open, который будет открывать веб-страницу по указанному URL

        #код вызывает метод get() у объекта browser, передавая ему URL, который хранится в атрибуте self.url.
        # В результате браузер откроет указанную страницу.