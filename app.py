from flask import Flask, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# ------------------------------
# Step 1: Training Data (Demo Dataset)
# ------------------------------
data = {
    "review": [
        "Great company culture and supportive colleagues.",
        "Poor management and no work-life balance.",
        "Excellent opportunities for freshers.",
        "Salary is very low compared to market standards.",
        "Amazing learning experience and good placement support.",
        "Toxic environment and biased HR policies."
    ],
    "label": [1, 0, 1, 0, 1, 0]  # 1=Positive, 0=Negative
}
df = pd.DataFrame(data)

# ------------------------------
# Step 2: Train Model
# ------------------------------
vectorizer = TfidfVectorizer(stop_words="english")
X_vec = vectorizer.fit_transform(df["review"])
y = df["label"]

model = LogisticRegression()
model.fit(X_vec, y)

# ------------------------------
# Step 3: Flask App
# ------------------------------
app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Welcome to Placement Review Sentiment API 🎓"}

@app.route("/predict", methods=["POST"])
def predict_sentiment():
    try:
        data = request.get_json()
        print(data)
        review = data.get("review", "")
        print(review)
        
        if not review:
            return jsonify({"error": "No review text provided"}), 400
        
        # Vectorize and predict
        review_vec = vectorizer.transform([review])
        prediction = model.predict(review_vec)[0]
        
        #sentiment = "Positive 😊" if prediction == 1 else "Negative 😡"
        sentiment = "Positive ..." if prediction == 1 else "Negative ???"

        return jsonify({
            "review": review,
            "sentiment": sentiment,
            "label": int(prediction)
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ------------------------------
# Step 4: Run App
# ------------------------------
if __name__ == "__main__":
    app.run(debug=True)
