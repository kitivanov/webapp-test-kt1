import time
import pytest
from selenium import webdriver


ANTIBOT_MARKERS = (
    "вы не робот",
)


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def is_antibot_page(browser) -> bool:
    """Определяет, показывает ли сайт антибот-страницу («Вы не робот?»)."""
    text = (browser.page_source or "").lower()
    return any(m in text for m in ANTIBOT_MARKERS)


def test_open_ya(browser):
    """Тест открытия страницы"""
    browser.get("https://ya.ru")
    time.sleep(2)
    if is_antibot_page(browser):
        return
    assert "яндекс" in str(browser.title).lower()
