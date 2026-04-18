from textblob import TextBlob

def get_sentiment(text):
    if not isinstance(text, str):
        return "Neutral"

    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"