import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

vectorizer = TfidfVectorizer()
model = LogisticRegression()

def train_model():
    df = pd.read_csv("data/tickets.csv")

    X = df["Ticket Description"]

    y = df["Ticket Type"]


    X_vec = vectorizer.fit_transform(X)
    model.fit(X_vec, y)

def predict_category(text):
    text_vec = vectorizer.transform([text])
    return model.predict(text_vec)[0]