from bsoup_scraping import get_bbc, get_wiki, get_astro

from query_scraping import get_leetcode

from selenium_scraping import get_stocks, get_espn




functions = {
    'Wikipedia': get_wiki(),
    'BBC News': get_bbc(),
    'NASA Astronomy Site': get_astro(),
    'Daily Leetcode Problem Number': get_leetcode(),
    'Yahoo Finance Stocks Market Price': get_stocks(),
    'ESPN Soccer Scores': get_espn()

}
stocks = get_stocks()
scores = get_espn()

numbers = [get_wiki(), get_bbc(), get_astro(), get_leetcode()]
print(numbers)
avg = sum(numbers)/len(numbers)
print(avg)




