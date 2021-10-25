import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from stensul.src.elements.base_page_element import BasePageElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from stensul.src.elements.list_item import ListItem
from stensul.src.elements.list_items import ListItems
from stensul.src.locators.stensul_list import PageListLoc
from stensul.src.pages.base_page import BasePage

_URL = 'http://immense-hollows-74271.herokuapp.com'


class ListApp(BasePage):

    def __init__(self, driver: WebDriver, timeout: int = 15):
        super().__init__(driver, _URL, timeout)
        self.list_items = ListItems(PageListLoc.ITEMS_LIST, self._wait)
        self.__create_btn = BasePageElement(PageListLoc.CREATE_BTN, wait=self._wait)
        self.__update_btn = BasePageElement(PageListLoc.UPDATE_BTN, wait=self._wait)
        self.__textarea = BasePageElement(PageListLoc.TEXTAREA, wait=self._wait)
        self.__input_img = BasePageElement(PageListLoc.INPUT_IMAGE, wait=self._wait)
        self.__list_count = BasePageElement(PageListLoc.LIST_COUNT, wait=self._wait)

    def get_item(self, index: int) -> ListItem:
        self.list_items.reload()
        try:
            if index < 0:
                return self.list_items[index]
            else:
                return self.list_items[index - 1]
        except IndexError:
            print(f'\n\n {"*" * 29} Value is not in range to 0 to {len(self.list_items)} . {"*" * 29}')
            return None

    def create_item(self, path_file=None, text_input=""):
        """
        Create Item on the list & Handle alerts
        :param path_file: File path of the Img to be uploaded
        :param text_input: Text to write on text area
        """
        if path_file is not None:
            self.__input_img.write(path_file)
            self.__textarea.write(text_input)
            self.__create_btn.click()
        else:
            try:  # handle the alert if present
                self.__textarea.write(text_input)
                self.__create_btn.click()
                WebDriverWait(self._driver, 5).until(EC.alert_is_present(), 'Timed out waiting ALERT')
                alert = self._driver.switch_to.alert
                alert.accept()
            except TimeoutError:
                print("No Alert")

    def edit_item(self, path_file=None, text_input=""):
        """
        Edit an Item on the list
        :param path_file: File path of the Img to be uploaded
        :param text_input: Text to write on text area
        """
        if path_file is not None and text_input != "":  # Change Img and text
            self.__input_img.write(path_file)
            self.__textarea.write(text_input)
            self.__update_btn.click()
        elif path_file is not None:  # NO Image Update
            self.__input_img.write(path_file)
            self.__update_btn.click()
        elif text_input != "":  # Only Text Change
            self.__textarea.write(text_input)
            self.__update_btn.click()

    def delete_item(self, index, confirm=True):
        """
        Delete Index item on the list
        :param index: Index of the item to be deleted
        :param confirm: Boolean True: Delete Item / False: Dismiss Alert and no Item deleted.
        """
        item: ListItem
        item = self.get_item(index)
        item.delete_item_btn()
        if not confirm:
            item.dismiss()
        else:
            item.confirm()

    def update_is_enabled(self) -> bool:
        return self.__update_btn.is_enabled()

    def create_is_enabled(self) -> bool:
        return self.__create_btn.is_enabled()

    def write_textarea(self, text):
        self.__textarea.write(text)

    def get_counter(self) -> int:
        self.__list_count.wait_until_text_present(f'List of items ({len(self.list_items)+1})')
        return int(self.__list_count.get_text()[15:17])
