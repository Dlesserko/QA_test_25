import time

import pytest

from pages.elements_page import TextBoxPage, MyPetsPage


class TestElements:
    class TestTextBox:

        def test_text_box(self , driver):
            text_box_page = TextBoxPage(driver, 'https://petfriends.skillfactory.ru/login')
            text_box_page.open()
            # text_box_page.SUBMIT_IF_HAVE.click()
            text_box_page.fill_all_fields()
            # text_box_page.go_to_my_pets()
            # print(text_box_page.cheсk_filled_form())
            output_email , output_password = text_box_page.check_filled_form()
            print(output_email)
            print(output_password)

class TestMyPets:
        def test_my_pets(selfs,driver):
            my_pets_page = MyPetsPage(driver, 'https://petfriends.skillfactory.ru/my_pets')
            my_pets_page.open()
            my_pets_page.open_full_list()
            my_pets_page.click_random_checkbox()

# def test(driver):
#     page = BasePage(driver,'https://petfriends.skillfactory.ru/login')
#     page.open()
#     time.sleep(3)