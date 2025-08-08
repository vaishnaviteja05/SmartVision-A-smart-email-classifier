import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Sample training data (you can replace with real email data later)
data = {
    'text': [
        'Congratulations, you won a lottery!',
        'Update your bank account details now.',
        'Limited-time offer just for you.',
        'Meeting scheduled at 3 PM today.',
        'Verify your email address to continue.',
        'Your Amazon order has been shipped.',
        'Click this link to reset your password.',
        'Win free tickets to Maldives!',
        'Final reminder: Pay your invoice.',
        'Join us for a project discussion tomorrow.'
    ],
    'label': [
        'spam',
        'phishing',
        'promotion',
        'safe',
        'phishing',
        'safe',
        'phishing',
        'promotion',
        'spam',
        'safe'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Build pipeline: TF-IDF + Naive Bayes
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', MultinomialNB())
])

# Train the model
model.fit(df['text'], df['label'])

# Save the model to file
joblib.dump(model, "spamvision_model.pkl")

print("✅ SpamVision model trained and saved as 'spamvision_model.pkl'")
