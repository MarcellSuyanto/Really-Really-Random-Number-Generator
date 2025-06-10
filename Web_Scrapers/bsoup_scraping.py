import requests
from bs4 import BeautifulSoup
from .query_scraping import get_leetcode


def get_wiki():
    """
    Gets the length of the topic of the randomly generated wikipedia article
    """

    url = "https://en.wikipedia.org/wiki/Special:Random"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    topic = soup.find('body').find('h1').get_text()
    topic = topic.replace(" ", "")
    
    return len(topic)


def get_bbc(): 
    url = "https://www.bbc.com/news"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('h2')[:-1]

    # No. of headlines are usually around double-digit range
    index = (get_leetcode()//get_wiki())%len(headlines)
    return len(headlines[index].text.strip())

def get_astro():
    url = "https://apod.nasa.gov/apod/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    explanation = soup.get_text().replace("\n", "").replace(",","")
    explanation = explanation.split(' ')
    i = explanation.index("Explanation:")
    explanation = explanation[i:]

    total = 0 
    for word in explanation:
        try:
            total += int(word)
        except ValueError:
            continue
    if not total:
        return len(explanation)
    
    return total
    




