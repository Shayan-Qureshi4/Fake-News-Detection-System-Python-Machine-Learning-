from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

app = Flask(__name__)
# Load true news dataset
true_df = pd.read_csv(r"True.csv")
true_df['label'] = 0  # 0 = True News

# Load fake news dataset
fake_df = pd.read_csv(r"Fake.csv")
fake_df['label'] = 1  # 1 = Fake News

# Combine datasets
df = pd.concat([true_df, fake_df], ignore_index=True)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

# Train model
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(X_train, y_train)

# Flask routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        news_article = data.get('news')

        if not news_article:
            return jsonify({'error': 'Please provide a news article'}), 400

        prediction = model.predict([news_article])[0]
        result = "True News" if prediction == 0 else "Fake News"

        return jsonify({'prediction': result})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'An error occurred during prediction'}), 500

if __name__ == '__main__':
    app.run(debug=True)
