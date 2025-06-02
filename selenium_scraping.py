from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException

def get_stocks():
    # initialize a web driver instance to control a Chrome window
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.set_window_size(1920, 1080)

    # We ask Chrome to run in headleass mode to avoid excess resources usage
    options = Options()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )
    
    stocks_codes = ['AMZN','TSLA','AAPL','MSFT','GOOGL','NVDA']
    stocks = {}
    for stock_code in stocks_codes:
        url = f'https://finance.yahoo.com/quote/{stock_code}'
        driver.get(url)
        regular_market_price = driver.find_element(
            By.CSS_SELECTOR,
            f'[data-symbol="{stock_code}"][data-field="regularMarketPrice"]'
        ).text
        stocks[stock_code] = regular_market_price       

    # close the browser and free up the resources
    driver.quit()

    return stocks


