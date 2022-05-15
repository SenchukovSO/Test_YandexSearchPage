from selenium.webdriver.common.by import By
from base.seleniumbase import SeleniumBase


class Yandexpage_images(SeleniumBase):
    """
    The class contains functions for the Yandex image search test
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__img_icon = "a[data-id='images']"
        self.__sel_photo = "Link"
        self.__first_photo = "serp-item__link"
        self.__photo_open = "MMImage-Origin"
        self.__button_back = "CircleButton-Icon"

    def find_img_icon(self):
        """
        The function searches for the 'Yandex Images' element
        """
        return self.is_visible("css", self.__img_icon, "Img")

    def selection_photos(self):
        """
        The function searches for an image element
        from the first selection on the page Https://yandex.ru/images
        """
        return self.is_visible("class_name", self.__sel_photo, "Selection_Photos")

    def first_photo(self):
        """
        The function searches for the first image in a selection of images
        """
        return self.is_visible("class_name", self.__first_photo, "First Photo")

    def button_forward(self):
        """
        The function is looking for a button to switch images in the
        selection forward
        """
        return self.driver.find_element(by=By.CLASS_NAME, value="MMImage-Origin")

    def button_back(self):
        """
        The function is looking for a button to switch images
        in the selection back
        """
        return self.is_visible("class_name", self.__button_back, "Back")

    def photo_open(self):
        """
        The function actually duplicates the first_photo function,
        but it is necessary to check the fact of opening the first photo
        in the collection
        """
        return self.driver.find_element(by=By.CLASS_NAME, value="MMImage-Origin").get_attribute("src")

    def result_search(self):
        """
        The function finds the information
        entered in the search field on the page
        """
        return self.driver.find_element_by_xpath("//meta[@name='description']").get_attribute("content")

    def window_b(self):
        """
        The function indexes the first page that opens
        """
        return self.driver.window_handles[0]

    def window_af(self):
        """
        The function indexes opening pages other than the first one
        """
        return self.driver.window_handles[1]

    def window_switch(self, window_after):
        """
        The function switches the selenium focus to a new page
        """
        return self.driver.switch_to.window(window_after)

    def find_attr(self, function, attr):
        """
        The function takes another function and finds the attribute
         of the element of this function
        """
        return function.get_attribute(attr)

    def click_element(self, function):
        """
        A function takes another function and clicks on an element of that function
        """
        return function.click()






