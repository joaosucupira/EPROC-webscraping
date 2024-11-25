# Inicialização do webdriver

import time, os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager # type: ignore

DRIVER_PATH = os.path.join("drivers","chromedriver.exe")
service = Service(DRIVER_PATH)
chrome_options = Options()

def initialize_driver() :
    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        ), options=chrome_options
    )
    return driver

def close_driver(driver, wait_time = 0) :
    time.sleep(wait_time)
    driver.quit()