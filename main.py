from Web_Scrapers.bsoup_scraping import *

from Web_Scrapers.query_scraping import *

from Web_Scrapers.selenium_scraping import *




functions = {
    'Wikipedia': get_wiki(),
    'BBC News': get_bbc(),
    'NASA Astronomy Site': get_astro(),
    'Daily Leetcode Problem Number': get_leetcode(),
    'Yahoo Finance Stocks Market Price': get_stocks(),
    'ESPN Soccer Scores': get_espn()
}

value_list = [value for value in functions.values()]
print(value_list)

avg = sum(value_list)/len(value_list)
print(avg)



"""
1. Set up Readme File properly
    Project description

    Installation instructions

    Usage examples

    Contribution guidelines

    Screenshots/GIFs (if applicable)
2. License
3. requirements.txt
4. Description
5. https://www.youtube.com/watch?v=eNDuqcrLTLs
"""


