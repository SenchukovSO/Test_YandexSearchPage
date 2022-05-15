from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


class SeleniumBase:
    """
    The class describes the main functions for searching for elements on Yandex pages
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15, 0.5)

    def __get_selenium_by(self, find_by: str) -> dict:
        """
        The function declares more convenient ways to record locators
        """
        find_by = find_by.lower()
        locating = {
            "css": By.CSS_SELECTOR,
            "xpath": By.XPATH,
            "class_name": By.CLASS_NAME,
            "id": By.ID,
            "link_text": By.LINK_TEXT
        }

        return locating[find_by]

    def is_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        """
        The function returns the webelement
        """
        return self.wait.until(
            ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name)

    def are_visible(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        """
        The function returns web elements as a list
        """
        return self.wait.until(
            ec.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)), locator_name)