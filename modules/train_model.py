import os
import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Read training dataset
data = pd.read_csv("dataset/training_data.csv")

# Features and labels
X = data["text"]
y = data["category"]

# Convert text into TF-IDF features
vectorizer = TfidfVectorizer()

X_vector = vectorizer.fit_transform(X)

# Train Naive Bayes model
model = MultinomialNB()

model.fit(X_vector, y)

# Create model folder if it doesn't exist
os.makedirs("model", exist_ok=True)

# Save model and vectorizer
joblib.dump(model, "model/classifier.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("Model Trained Successfully!")
print("Files Saved:")
print("model/classifier.pkl")
print("model/vectorizer.pkl")