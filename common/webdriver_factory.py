"""Implements web driver factory pattern to create new instances."""
from platform import system
from pathlib import Path
from selenium import webdriver
from common.utils import get_project_root

__DRIVER_DIR = 'drivers'

__CHROME_FILE_NAME = 'chromedriver'

__FIREFOX_FILE_NAME = 'geckodriver'

__WIN_EXTENSION = '.exe'


def get_driver(browser_name: str):
    """Get a new instance of web driver.
    :param browser_name: Browser name (chrome|firefox)
    :return: Web driver instance.
    """
    if browser_name.lower() == 'chrome':
        return __create_chrome()
    elif browser_name.lower() == 'firefox':
        return __create_firefox()
    else:
        raise ValueError(f'{browser_name} not supported')


def __create_chrome():
    chrome_path = __get_chrome_path()
    driver = webdriver.Chrome(executable_path=chrome_path)
    driver.maximize_window()
    return driver


def __create_firefox():
    firefox_path = __get_firefox_path()
    driver = webdriver.Firefox(executable_path=firefox_path)
    driver.maximize_window()
    return driver


def __get_chrome_path() -> Path:
    return __get_driver_path(__CHROME_FILE_NAME)


def __get_firefox_path() -> Path:
    return __get_driver_path(__FIREFOX_FILE_NAME)


def __get_driver_path(executable) -> Path:
    root = get_project_root()
    if system().lower() == 'windows':
        executable += __WIN_EXTENSION
    return root.joinpath(__DRIVER_DIR, executable)