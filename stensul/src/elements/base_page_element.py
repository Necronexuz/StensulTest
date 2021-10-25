"""Base page element"""
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePageElement:

    def __init__(self, loc: tuple, wait: WebDriverWait = None, root: WebElement = None):
        self._wait = wait
        self._loc = loc
        self._root = root

    def wait_until_loaded(self) -> WebElement:
        """Wait until page is loaded"""
        if self._root and isinstance(self._root, WebElement):
            return self._root.find_element(*self._loc)
        elif self._wait and isinstance(self._wait, WebDriverWait):
            return self._wait.until(EC.element_to_be_clickable(self._loc))
        else:
            raise ValueError(f'Page element must have either an instance of wait or a root web element.')

    def wait_until_present(self) -> WebElement:
        """Wait until page is loaded"""
        if self._root and isinstance(self._root, WebElement):
            return self._root.find_element(*self._loc)
        elif self._wait and isinstance(self._wait, WebDriverWait):
            return self._wait.until(EC.presence_of_element_located(self._loc))
        else:
            raise ValueError(f'Page element must have either an instance of wait or a root web element.')

    def wait_until_text_present(self, text) -> WebElement:
        if self._root and isinstance(self._root, WebElement):
            return self._root.find_element(*self._loc)
        elif self._wait and isinstance(self._wait, WebDriverWait):
            return self._wait.until(EC.text_to_be_present_in_element(self._loc, text))
        else:
            raise ValueError(f'Page element must have either an instance of wait or a root web element.')

    def is_enabled(self) -> bool:
        element = self.wait_until_present()
        return element.is_enabled()

    def click(self):
        """Write text to input."""
        element = self.wait_until_present()
        element.click()

    def write(self, value):
        """Write text to input."""
        element = self.wait_until_loaded()
        element.clear()
        element.send_keys(value)

    def get_value(self) -> str:
        """Get value attribute."""
        element = self.wait_until_loaded()
        return element.get_attribute('value')

    def get_text(self) -> str:
        """Get value attribute.
        :rtype: TExt
        """
        element = self.wait_until_loaded()
        return element.text
