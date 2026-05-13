from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {}


@app.route("/")
def home():
    """Handle the root URL."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Return a JSON response with a list of all usernames."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Return the API status."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Return the full object for a specific username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Handle POST requests to add a new user."""
    # Check if request body is valid JSON
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()
    username = data.get("username")

    # Validation: username is required
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Validation: check if user already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add the new user to the dictionary
    users[username] = data

    response = {
        "message": "User added",
        "user": data
    }
    return jsonify(response), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
