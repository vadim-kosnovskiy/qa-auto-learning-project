from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


opts = Options()
opts.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/121.0.0.0 Safari/537.36"
)
opts.add_argument("--disable-blink-features=AutomationControlled")
opts.add_argument("--start-maximized")
opts.add_experimental_option("excludeSwitches", ["enable-automation"])
opts.add_experimental_option('useAutomationExtension', False)
opts.add_experimental_option("detach", True)


class BasePage:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(options=opts, service=Service(ChromeDriverManager().install()))

    def close(self) -> None:
        self.driver.close()
