from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Your Hugging Face API key
api_key = "APIKEY"

# Hugging Face Inference API endpoint
hf_endpoint = "https://api-inference.huggingface.co/models/microsoft/Phi-3-mini-4k-instruct"

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Flask app! Use the '/process' endpoint to interact with the API."

@app.route('/process', methods=['POST'])
def process_request():
    # Parse the JSON payload from the incoming request
    data = request.get_json()

    if not data or 'prompt' not in data:
        return jsonify({"error": "Invalid request, 'prompt' field is required"}), 400

    # Forward the request to Hugging Face API
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": data['prompt'],  # You can customize this based on the model type
        "parameters": {
            "temperature": data.get("temperature", 0.7),
            "max_length": data.get("max_tokens", 1000)
        }
    }

    try:
        response = requests.post(hf_endpoint, headers=headers, json=payload)
        response.raise_for_status()  # Raise an error for bad status codes
        result = response.json()

        # Return the result back to the client
        return jsonify(result)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
