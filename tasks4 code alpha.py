from flask import Flask, request, jsonify
import re
import random

app = Flask(__name__)

chatbot_responses = [
    {"patterns": [r"hi|hello|hey"], "responses": ["Hello! How can I help you today?", "Hi there!"]},
    {"patterns": [r"how are you"], "responses": ["I'm doing well, thanks!", "All systems operational!"]},
    {"patterns": [r"what can you do"], "responses": ["I can answer questions and help with information"]}
]

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({"error": "Please send a message"}), 400
    
    user_input = data['message'].lower()
    for item in chatbot_responses:
        for pattern in item['patterns']:
            if re.search(pattern, user_input):
                return jsonify({"response": random.choice(item['responses'])})
    
    return jsonify({"response": "I didn't understand that. Try asking differently."})

@app.route('/')
def home():
    return "Chatbot is running. Send POST requests to /chat"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)