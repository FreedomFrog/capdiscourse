from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


analyzer = SentimentIntensityAnalyzer()

def process_content(text):
    return (TextBlob(text).sentiment, analyzer.polarity_scores(text))

