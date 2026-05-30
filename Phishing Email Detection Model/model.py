import pandas as pd
import re

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

def extract_features(text):
    urls = len(re.findall(r'http[s]?://', text))
    return text + f" urls_{urls}"

def train_model():

    df = pd.read_csv("emails.csv")

    df["text"] = df["text"].apply(extract_features)

    X = df["text"]
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.3,
        random_state=42
    )

    vectorizer = TfidfVectorizer()

    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    model = MultinomialNB()

    model.fit(X_train_vec, y_train)

    predictions = model.predict(X_test_vec)

    accuracy = round(
        accuracy_score(y_test, predictions) * 100,
        2
    )

    matrix = confusion_matrix(
        y_test,
        predictions
    ).tolist()

    return model, vectorizer, accuracy, matrix


def predict_email(text, model, vectorizer):

    text = extract_features(text)

    vector = vectorizer.transform([text])

    result = model.predict(vector)[0]

    return "Phishing" if result == 1 else "Safe"