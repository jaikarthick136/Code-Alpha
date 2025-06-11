from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory ticket storage
bookings = {}

# Home route
@app.route('/')
def home():
    return "Welcome to the Cloud-Based Bus Pass System!"

# Ticket booking route
@app.route('/book_ticket', methods=['POST'])
def book_ticket():
    data = request.get_json()
    user = data.get('user')
    route = data.get('route')

    if not user or not route:
        return jsonify({"error": "Missing user or route"}), 400

    ticket_id = str(uuid.uuid4())
    bookings[ticket_id] = {"user": user, "route": route}

    return jsonify({"message": "Ticket booked successfully", "ticket_id": ticket_id})

if __name__ == '__main__':
    app.run(debug=True)
