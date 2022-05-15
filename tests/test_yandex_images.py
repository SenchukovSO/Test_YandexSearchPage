import pytest
from pom.yandexpage_images import Yandexpage_images


@pytest.mark.usefixtures("setup")
class Testyandeximages:

    def test_images(self):
        yandex_img = Yandexpage_images(self.driver)
        # We remember the index of the first tab, then the second one will appear, it is necessary to switch
        window_before = yandex_img.window_b()

        element_img = yandex_img.find_img_icon()
        if not element_img:
            print("\nThe link to the pictures is missing on the page\n")
        else:
            print("\nThe link to the pictures is present on the page\n")

            # Looking for a link to a selection of images
            link_img = yandex_img.find_attr(element_img, "href")
            # Go to the page with pictures
            yandex_img.click_element(element_img)
            # Compare the link of the element_img element that we clicked with the current address of Yandex images
            if not link_img.find("Https://yandex.ru/images/"):
                print("We have not switched to Https://yandex.ru/images\n")
            else:
                print("We really switched to Https://yandex.ru/images\n")

                # Changing the focus window
                window_after = yandex_img.window_af()
                yandex_img.window_switch(window_after)

                # Search for the title and links to the first selection
                selection_photos = yandex_img.selection_photos()
                name_selection_photos = selection_photos.text

                # Go to the page of the first selection
                yandex_img.click_element(selection_photos)

                # Аind the data about the search query on the page
                res_search = yandex_img.result_search()

                # Сomparison of the search query result by the name of the selection (must match)
                if res_search.find(name_selection_photos):
                    print("The first category of images has opened, in search of the correct text\n")

                    first_photo = yandex_img.first_photo()
                    # Click on the first photo
                    yandex_img.click_element(first_photo)
                    # Check if the picture we clicked on has opened
                    photo_open = yandex_img.photo_open()
                    if photo_open is not None:
                        print("The first picture opened\n")

                        # Moving on to the second picture
                        button_forward = yandex_img.button_forward()
                        button_forward.click()
                        # Going back to the previous photo (the first one)
                        button_back = yandex_img.button_back()
                        button_back.click()

                        first_image_link = yandex_img.photo_open()
                        # We compare the picture that we opened the very first one
                        # with the one that we returned to after opening the second one
                        if photo_open == first_image_link:
                            print("The picture that we opened the very first one coincides"
                                  " with the picture that we opened "
                                  "when we came back from the second picture\n")
                        else:
                            print("The picture that we opened the very first one does not match the picture"
                                  " that we opened when we came back from the second picture\n")
                    else:
                        print("Picture doesnt open\n")
                else:
                    print("Название подборки не совпадает с поисковой выдачей")