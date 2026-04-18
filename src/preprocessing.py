def clean_data(df):
    df = df.drop_duplicates()

    df["Preferred_Tool"] = df["Preferred_Tool"].str.title().str.strip()
    df["Gender"] = df["Gender"].str.title().str.strip()

    return df
from sentiment import get_sentiment

def add_sentiment(df):
    df["Sentiment"] = df["Feedback"].apply(get_sentiment)
    return df