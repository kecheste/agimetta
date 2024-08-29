from hyperon import *
from textblob import TextBlob

# This agent uses TextBlob to perform sentiment analysis on the first argument
def sentiment_analysis_agent(metta, *args):
    # if no arguments are provided, return an error message
    if not args:
        return [ValueAtom("No arguments provided", "Error")]

    # perform sentiment analysis on the text provided
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
