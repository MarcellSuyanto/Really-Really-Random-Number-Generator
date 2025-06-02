import requests
from bs4 import BeautifulSoup
from query_scraping import get_leetcode


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

def get_espn():
    week = 19
    year = 2022

    url = "https://www.espn.com/nfl/scoreboard/_/week/{week}/year/{year}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    all_data = []
    for board in soup.select('.ScoreboardScoreCell'):
        title = board.find_previous(class_='Card__Header__Title').text
        teams = [t.text for t in board.select('.ScoreCell__TeamName')]
        scores = [s.text for s in board.select('.ScoreCell__Score')] or ['-', '-']

        all_data.append((week, title, teams[0], scores[0], teams[1], scores[1]))

    print(all_data)

get_espn()

