import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Load email data
df = pd.read_csv("sample_emails.csv")

# Split data
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2)

# Convert text to numbers (vectors)
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

# Train the model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Save model and vectorizer
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("✅ Model and vectorizer saved!")
