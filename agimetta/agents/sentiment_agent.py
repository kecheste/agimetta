from hyperon import *
from textblob import TextBlob

def sentiment_analysis_agent(metta, *args):
    if not args:
        return [ValueAtom("No arguments provided", "Error")]

    text = str(args[0])
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        sentiment_text = "Positive sentiment"
    elif sentiment < 0:
        sentiment_text = "Negative sentiment"
    else:
        sentiment_text = "Neutral sentiment"

    atoms = metta.parse_all(sentiment_text)
    
    return [ValueAtom(atom) for atom in atoms]
