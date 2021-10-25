from selenium.webdriver.common.by import By


class PageListLoc:
    ITEMS_LIST = (By.XPATH, "//li[@class='media ng-scope ui-sortable-handle']")
    CREATE_BTN = (By.XPATH, "//button[normalize-space()='Create Item']")
    UPDATE_BTN = (By.XPATH, "//button[normalize-space()='Update Item']")
    TEXTAREA = (By.XPATH, "//textarea")
    INPUT_IMAGE = (By.ID, "inputImage")
    LIST_COUNT = (By.CSS_SELECTOR, "h1[class='ng-binding']")


