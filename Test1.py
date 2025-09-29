import requests

# API endpoint
url = "http://127.0.0.1:5000/predict"

# Example reviews
reviews = [
    "The placement process was smooth and HR was very helpful.",
    "No growth opportunities and salary is terrible.",
    "Good learning experience but workload is heavy."
]

for review in reviews:
    payload = {"review": review}
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        result = response.json()
        print(f"Review: {result['review']}")
        print(f"Sentiment: {result['sentiment']} (Label={result['label']})")
        print("-" * 50)
    else:
        print("Error:", response.text)