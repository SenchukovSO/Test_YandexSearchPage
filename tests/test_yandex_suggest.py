import pytest
from pom.yandexpage_suggest import Yandexpage_search
import time


@pytest.mark.usefixtures("setup")
class TestYandexPage:

    def test_search(self):
        yandexpage_search = Yandexpage_search(self.driver)
        # Checking for search availability
        if not yandexpage_search.get_search():
            print("\n1) The 'search' element is missing from the page \n")
        else:
            print("\n1) The 'search' element is present on the page \n")

            # Checking for search availability
            yandexpage_search.search_sendkeys()

            # Check that the suggest table has appeared
            text = yandexpage_search.find_suggest()
            if text is None:
                print("2) Suggest is not on the page, \n")
            else:
                print("2) Suggest is on the page: \n")

                # Press ENTER to make a table with search results appear
                yandexpage_search.click_enter()
                # Collecting all the links from the search results table
                links = yandexpage_search.find_links()

                # Checking if the first five links
                # from the search result lead to the page tensor.ru
                count = 0
                for i in range(5):
                    if links[i].text == "tensor.ru":
                        count += 1
                if count >= 5:
                    print("3) The first five search results contain a link to tensor.ru")
                else:
                    print("3) The first five search results contain not only links to the site tensor.ru")





















