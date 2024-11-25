from flask import Flask, render_template, request, jsonify
import webview
from pymongo import MongoClient, errors
import threading

# MongoDB Connection
try:
    client = MongoClient("mongodb+srv://prabhathhemasiri:PMXpxiZ5g9rsoIdp@possystem.dvwzo.mongodb.net/")
    db = client["possystem"]
    print("MongoDB connection successful!")
except errors.ConnectionError as ce:
    print(f"Connection failed: {ce}")
except errors.ConfigurationError as conf_err:
    print(f"Configuration error: {conf_err}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

users_collection = db["users"]

# Flask App
app = Flask(__name__)

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/dashboard")
def test_page():
    return render_template("dashboard.html")


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    users = users_collection.find()
    for user in users:
        if user["username"] == username:
            if user["password"] == password:
                return jsonify({"success": True, "message": "Login Successful!"})
            else:
                return jsonify({"success": False, "message": "Incorrect password!"})

    return jsonify({"success": False, "message": "Username does not exist!"})

def start_flask():
    # Disable the reloader to avoid issues with threading
    app.run(debug=True, port=5000, use_reloader=False)

if __name__ == "__main__":
    # Start Flask in a thread
    flask_thread = threading.Thread(target=start_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Create a webview window
    webview.create_window("POS System", "http://127.0.0.1:5000")
    webview.start()
