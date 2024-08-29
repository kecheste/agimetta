from hyperon import *
from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis")

def sentiment_analyzer_agent(metta, *args):
    if not args:
        return [ValueAtom("No arguments provided", "Error")]

    article_description = str(args[0])
    sentiment = sentiment_analyzer(article_description)

    sentimenta_label = sentiment[0]['label']
    sentiment_score = sentiment[0]['score']

    sentiment_text = f"Sentiment: {sentimenta_label}, Score: {sentiment_score}"

    atoms = metta.parse_all(sentiment_text)

    return [ValueAtom(atom) for atom in atoms]