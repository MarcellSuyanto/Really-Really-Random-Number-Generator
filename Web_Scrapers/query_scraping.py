import requests

def get_leetcode():

    # The Leetcode site blocks HTML requests with Cloudfare
    # Beautifulsoup cannot extract the web elements
    # We use GraphQL Query to extract the data
    API_URL = "https://leetcode.com/graphql"
    query = """
    {
    activeDailyCodingChallengeQuestion {
        question {
        questionFrontendId
        title
        }
    }
    }
    """
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
    }
    response = requests.post(API_URL, json={"query": query}, headers=headers)
    daily_id = response.json()['data']['activeDailyCodingChallengeQuestion']['question']['questionFrontendId']
    return int(daily_id)