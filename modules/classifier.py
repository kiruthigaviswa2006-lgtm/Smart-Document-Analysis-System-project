import joblib

# Load trained model and vectorizer
model = joblib.load("model/classifier.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")


def classify_document(text):

    # Convert text to TF-IDF features
    text_vector = vectorizer.transform([text])

    # Predict category
    category = model.predict(text_vector)[0]

    # Predict confidence
    confidence = model.predict_proba(text_vector).max() * 100

    return category, round(confidence, 2)