from hyperon import *
import requests

api_key = 'ad4490eb5b0d4911aac9580b11ecfd82'

def news_agent(metta, *args):
    if not args:
        return [ValueAtom("No arguments provided", "Error")]

    query = str(args[0])
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}'
    response = requests.get(url)
    
    if response.status_code != 200:
        return [ValueAtom("Failed to fetch news articles", "Error")]

    data = response.json()

    if data['status'] == 'error':
        return [ValueAtom(data['message'], "Error")]

    articles = data.get('articles', [])
    if not articles:
        return [ValueAtom("No articles found", "Error")]

    # I fetched the first article's description just for the sake of simplicity
    article_description = articles[0].get('description', 'No description available')
    
    atoms = metta.parse_all(article_description)
    return [ValueAtom(atom) for atom in atoms]