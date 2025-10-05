from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
FILE_PATH = os.path.join(os.path.dirname(__file__), "user_details.json")

# Ensure JSON file exists
if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, "w") as f:
        json.dump([], f)

@app.route("/api/page", methods=["GET"])
def homePage():
    return "Home Page"
@app.route("/api/submit", methods=["POST"])
def submit():
    data = request.json
    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "Name and Email are required"}), 400

    # Read existing data
    with open(FILE_PATH, "r") as f:
        users = json.load(f)

    # Add new user
    users.append({"name": name, "email": email})

    # Save back
    with open(FILE_PATH, "w") as f:
        json.dump(users, f, indent=2)

    return jsonify({"message": "User details saved!", "users": users}), 201



if __name__ == "__main__":
    app.run(debug=True, port=6001, host='0.0.0.0')
