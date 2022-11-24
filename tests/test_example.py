from selenium import webdriver
import pytest


def test_1(browser):
    browser.get("https://ya.ru")
    assert "Яндекс" in browser.title
