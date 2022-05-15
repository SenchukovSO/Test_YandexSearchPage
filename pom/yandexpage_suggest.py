from selenium.webdriver import Keys
from base.seleniumbase import SeleniumBase


class Yandexpage_search(SeleniumBase):
    """
    The class contains functions for checking suggest
    and the presence of links tensor.ru
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__search = "text"
        self.__suggest = "mini-suggest__popup-content"
        self.__links = "//a[@class='Link Link_theme_outer Path-Item link path__item link organic__greenurl']//b"

    def get_search(self):
        """
        The function searches for a search field on the page yandex.ru
        """
        return self.is_visible("id", self.__search, "Search")

    def search_sendkeys(self):
        """
        The function using the get_search function finds the search field
        and enters the text 'Tensor' there
        """
        search_click = self.get_search()
        search_click.send_keys("Тензор")

    def find_suggest(self):
        """
        The function finds the suggest element and returns it as text
        """
        suggest = self.is_visible("class_name", self.__suggest, "Suggest").text
        return suggest

    def click_enter(self):
        """
        The function uses the get_search function to find the search field
        and press the ENTER button
        """
        enter = self.get_search()
        enter.send_keys(Keys.ENTER)

    def find_links(self):
        """
        The function searches for links from the search results
        """
        return self.are_visible("xpath", self.__links, "Links")




