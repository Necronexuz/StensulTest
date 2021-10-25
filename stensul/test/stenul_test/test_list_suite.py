from stensul.src.elements.list_item import ListItem
from stensul.src.pages.list_app_page import ListApp
from stensul.test.common.test_base import TestBase

_CREATORS = "Creators: Matt Duffer, Ross Duffer"
_GOOD_IMG_PATH = '/Users/ivanjimenezlanda/PycharmProjects/StensulTest/img/Artorias-token.png'
_GOOD_IMG_PATH_NEW = '/Users/ivanjimenezlanda/PycharmProjects/StensulTest/img/IVJL.JPG'
_ACCEPTABLE_TXT = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean " \
                  "massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec " \
                  "quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. " \
                  "Donec."
_EDIT_TEXT = "Sir Artorias the Abysswalker was one of the Four Knights of Lord Gwyn"


class TestList(TestBase):

    # T00 - Iterable Test Case
    def test_item_list_length(self):
        list_app_page = ListApp(self.driver)
        list_app_page.open()
        list_app_page.list_items.reload()
        assert len(list_app_page.list_items) == 13, "List items should be 13 at initial state"

    # T01 - Create Item
    def test_create_item(self):
        list_app_page = ListApp(self.driver)
        list_app_page.open()
        list_app_page.create_item(_GOOD_IMG_PATH, _ACCEPTABLE_TXT)
        list_app_page.list_items.reload()
        assert list_app_page.get_counter() == 14, "List of items don't match"

    # T02 - Edit Item without image cause BUG
    def test_edit_item(self):
        list_app_page = ListApp(self.driver)
        list_app_page.open()
        item_to_edit: ListItem
        item_to_edit = list_app_page.get_item(-1)  # Get the last element
        item_to_edit.edit_item_btn()
        list_app_page.edit_item(_GOOD_IMG_PATH_NEW, _EDIT_TEXT)
        assert item_to_edit.get_description() == _EDIT_TEXT, "Edit text don't match"

    # T03 - Delete Item
    def test_delete_item(self):
        list_app_page = ListApp(self.driver)
        list_app_page.open()
        list_app_page.delete_item(-1, True)  # Get the last element

    # T04 - Search Item by description
    def test_search_item(self):
        list_app_page = ListApp(self.driver)
        list_app_page.open()
        found_item: ListItem
        for item in list_app_page.list_items:
            item: ListItem
            if item.get_description() == _CREATORS:
                found_item = item  # print(f'\n {"*" * 29} Item description found. {"*" * 29}')
                break
        assert found_item.get_description() == _CREATORS, "Description is not Matching"

    # T05 - Search Item by description
    def test_max_length(self):
        list_app_page = ListApp(self.driver)
        list_app_page.open()
        # print(f'\nis the button enabled: {list_app_page.create_is_enabled()}')
        # Initial State
        assert list_app_page.create_is_enabled() is False, "Button is enabled"
        list_app_page.write_textarea(_ACCEPTABLE_TXT)  # Text <= 300 characters
        # print(f'\nis the button enabled: {list_app_page.create_is_enabled()}')
        assert list_app_page.create_is_enabled() is True, "Button is not enabled"
        list_app_page.write_textarea(_ACCEPTABLE_TXT + "1")  # Text > 300 characters
        # print(f'\nis the button enabled: {list_app_page.create_is_enabled()}')
        assert list_app_page.create_is_enabled() is False, "Button is enabled"
