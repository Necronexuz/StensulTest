from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from stensul.src.elements.base_page_element import BasePageElement
from stensul.src.locators.list_item import ListItemLoc


class ListItem:
    def __init__(self, wait: WebDriverWait, root: WebElement):
        self._description = BasePageElement(ListItemLoc.TEXT_DESC, wait=wait, root=root)
        self._edit_btn = BasePageElement(ListItemLoc.EDIT_BTN, wait=wait, root=root)
        self._delete_btn = BasePageElement(ListItemLoc.DELETE_BTN, wait=wait, root=root)
        self._confirm = BasePageElement(ListItemLoc.CONFIRM_BTN, wait=wait, root=root)
        self._dismiss = BasePageElement(ListItemLoc.CANCEL_BTN, wait=wait, root=root)

    def get_description(self) -> str:
        """Get description for item."""
        # TODO - Function not returning teh right value - This need to be changed IVAN!!!!!!
        # This is a workaround
        # return self._description._root.text[12:]
        return self._description.get_text()[12:]

    def edit_item_btn(self):
        """Edit an Item"""
        self._edit_btn.click()

    def delete_item_btn(self):
        """Delete an Item"""
        self._delete_btn.click()

    def dismiss(self):
        """Dismiss an alert"""
        self._dismiss.click()

    def confirm(self):
        """Confirm an alert"""
        self._confirm.click()


