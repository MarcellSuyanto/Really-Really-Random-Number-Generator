from bsoup_scraping import get_bbc, get_wiki

from query_scraping import get_leetcode

from selenium_scraping import get_stocks


stocks = get_stocks()

numbers = [get_wiki(), get_bbc(), get_leetcode()]
print(numbers)




