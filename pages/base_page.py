from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self, browser: WebDriver, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
