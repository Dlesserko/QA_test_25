from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # FULL_NAME = (By.CSS_SELECTOR,"input[id='userName']")
    EMAIL = (By.ID, "email")
    FULL_PASSWORD = (By.CSS_SELECTOR, "#pass")
    # CURRENT_ADDRESS = (By.CSS_SELECTOR,"input[id='currentAddress']")
    # PERMAMENT_ADDRESS = (By.CSS_SELECTOR,"input[id='permamentAddress']")
    # SUBMIT_IF_HAVE = (By.PARTIAL_LINK_TEXT, '//a[contains(text(), "У меня уже есть аккаунт")]')
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")


    # CREATED_FULL_NAME = (By.CSS_SELECTOR,'#output # name')
    # CREATED_EMAIL = (By.CSS_SELECTOR,"'#output # Email'")
    # CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR,"input[id='currentAddress']")
    # CREATED_PERMAMENT_ADDRESS =(By.CSS_SELECTOR,"output #permamentAdderess")
class MyPetsPageLocators:
    MY_PETS = (By.LINK_TEXT, "Мои питомцы")





