from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CROS(app)

API_KEY = "5a5016bed6d4414862e795c51367f019"
API_URL = "https://api.sunoapi.org/v1/generate"

@app.route('/generate_music', methods=['POST'])
def generate_music():
    user_prompt = request.json.get('prompt', '')
    payload = {
        "model": "suno-v4",
        "prompt": user_prompt,
        "options": {
            "genre": "hiphop",
            "tempo": "fast",
            "duration": 60,
            "vocals": True
        }
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
