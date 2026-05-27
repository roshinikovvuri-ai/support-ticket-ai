import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.linear_model import LogisticRegression

# Load BERT model
bert_model = SentenceTransformer('all-MiniLM-L6-v2')

# Create classifier
classifier = LogisticRegression(max_iter=1000)

# Train model
def train_model():

    global classifier

    # Load dataset
    df = pd.read_csv("data/tickets.csv")


    # Remove missing values
    df = df.dropna()

    # Features and labels
    X = df["clean_text"].tolist()
    y = df["Ticket Type"].tolist()

    # Convert text into BERT embeddings
    X_embeddings = bert_model.encode(X)

    # Train classifier
    classifier.fit(X_embeddings, y)

# Predict category
def predict_category(text):

    # Convert input into embedding
    text_embedding = bert_model.encode([text])

    # Predict category
    prediction = classifier.predict(text_embedding)

    return prediction[0]