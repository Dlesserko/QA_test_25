import time

from locators.elements_page_locator import TextBoxPageLocators
from locators.elements_page_locator import MyPetsPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        # self.element_is_visible(self.locators.SUBMIT_IF_HAVE).click()
        # self.element_is_visible(self.locators.FULL_NAME).send_kys('')
        self.element_is_visible(self.locators.EMAIL).send_keys('LarryFram.r.10.1.9.93@gmail.com')
        self.element_is_visible(self.locators.FULL_PASSWORD).send_keys('yWGTseV3Qi3dUMZ')
        # self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys()
        # self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_kys()
        self.element_is_visible(self.locators.SUBMIT).click()
        # self.element_is_visible(self.locators.SUBMIT_IF_ALREADY_HAVE).click()
        time.sleep(5)

    def cheсk_filled_form(self):
        email = self.element_is_present(self.locators.EMAIL).text.split(':')[1]
        password =  self.element_is_present(self.locators.FULL_PASSWORD).text.split(':')[1]
        return email , password


class MyPetsPage(BasePage):
    locators = MyPetsPageLocators()
    def open_my_pets(self):
        self.element_is_present(self.locators.MY_PETS).click()

    def click_random_checkbox(self):
        item_list = self.element_are_visible(self.locators.MY_PETS)
        for item in item_list:
            self.go_to_element(item)
            print(item.txt)
