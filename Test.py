import requests
import json

# Define the API endpoint URL
url = 'http://127.0.0.1:5000/predict'

# Define the data to be sent in the request body
# The 'review' value corresponds to the 'd' argument in the curl command.
#payload = {
#    "review": "The placement process was smooth and HR was very helpful."
#}

payload = {
    "review": "Great company culture and supportive colleagues."
}



# The headers specify that the request body is JSON, 
# corresponding to the '-H "Content-Type: application/json"' in the curl command.
headers = {
    'Content-Type': 'application/json'
}

# Make the POST request
# The json=payload argument automatically serializes the dictionary to a JSON string
# and sets the Content-Type header if it wasn't explicitly set.
try:
    response = requests.post(url, headers=headers, json=payload)
    
    # Check for a successful response status code (e.g., 200)
    response.raise_for_status()

    # Print the response content
    print(f"Status Code: {response.status_code}")
    
    # Try to parse and print the JSON response if the server returns JSON
    try:
        data = response.json()
        print("Response Data (JSON):")
        print(json.dumps(data, indent=4))
    except requests.exceptions.JSONDecodeError:
        print("Response Data (Text):")
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the request: {e}")