import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.mozilla.org/firefox"
title = "Internet dla ludzi"


@pytest.fixture
def webFix():
    driver = webdriver.Firefox()
    driver.get(url)
    try:
        element = wait(driver, 10).until(EC.title_contains(title))
    except Exception as ex:
        print(ex)
    yield driver

    # always quit driver
    driver.quit()


def test_web_link(webFix):
    webFix.find_element(By.LINK_TEXT, "Learn More").click()
    title = webFix.title
    assert "Firefox" in title


def test_web_links(webFix):
    links = webFix.find_elements(By.TAG_NAME, "a")
    for link in links:
        href = link.get_attribute("href")
        assert "mozilla.org" in href or "spotify.com" in href or "twitter.com" in href or "instagram.com" in href or \
               "linkedin.com" in href or "tiktok.com" in href or "youtube.com" in href


def test_account_form(webFix):
    webFix.find_element(By.LINK_TEXT, "Join Firefox").click()
    try:
        element = wait(webFix, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "ui-helper-hidden-accessible")))
    except Exception as ex:
        print(ex)
    text_input = webFix.find_element(By.TAG_NAME, "input")
    text_input.send_keys("quchikukan@gmail.com")
    webFix.find_element(By.ID, "submit-btn").click()
    prefillEmail = None
    try:
        prefillEmail = wait(webFix, 3).until(EC.presence_of_element_located((By.ID, "prefillEmail")))
    except Exception as ex:
        print(ex)

    assert "quchikukan@gmail.com" in prefillEmail.text
