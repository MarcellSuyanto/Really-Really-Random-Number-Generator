from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import datetime


def get_stocks():
    options = Options()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )
    stocks_codes = ['AMZN','TSLA','AAPL','MSFT','GOOGL','NVDA']
    stocks = {}
    total_prices = 0
    for stock_code in stocks_codes:
        url = f'https://finance.yahoo.com/quote/{stock_code}'
        driver.get(url)
        regular_market_price = driver.find_element(
            By.CSS_SELECTOR,
            f'[data-symbol="{stock_code}"][data-field="regularMarketPrice"]'
        ).text
        regular_market_price = float(regular_market_price)
        stocks[stock_code] = regular_market_price
        total_prices += regular_market_price
    driver.quit()
    # close the browser and free up the resources
    return total_prices


def get_espn():
    driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
    )
    curr_date = datetime.datetime.now()
    yesterday = curr_date - datetime.timedelta(days=1)
    yesterday = yesterday.strftime("%Y/%m/%d").replace('/','')
    url = f"https://www.espn.com/soccer/scoreboard/_/date/{yesterday}"
    driver.get(url)
    scores = driver.find_elements(
        By.CSS_SELECTOR,
        '[class="ScoreCell__Score h4 clr-gray-01 fw-heavy tar ScoreCell_Score--scoreboard pl2"]'
    )
    scores = [i.text for i in scores if i.text]
    scores = list(map(int, scores))
    driver.quit()
    return sum(scores)

