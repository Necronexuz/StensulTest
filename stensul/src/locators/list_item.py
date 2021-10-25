from selenium.webdriver.common.by import By


class ListItemLoc:
    TEXT_DESC = (By.CLASS_NAME, 'media-body')
    #TODO - Note: use Xpath .// so I can iterate on the current node when using it.
    EDIT_BTN = (By.XPATH, ".//button[contains(@class,'btn btn-default')][normalize-space()='Edit']")
    DELETE_BTN = (By.XPATH, ".//button[contains(@class,'btn btn-default')][normalize-space()='Delete']")
    CONFIRM_BTN = (By.XPATH, "//button[normalize-space()='Yes, delete it!']")
    CANCEL_BTN = (By.XPATH, "//button[normalize-space()='Cancel']")

