import json
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

def loadUsers():
    with open("users.json", "r", encoding="utf-8") as file:
        return json.load(file)

#loads main page where all songs will be stored
@app.route("/")
def index():
    return render_template("index.html")


#loads login page
@app.route("/login", methods=(["GET", "POST"]))
def login():
    if request.method == "POST":
        #get input and assign variables
        username = request.form.get("username")
        password = request.form.get("password")

        users = loadUsers()

        #check if username exists and password matches
        if username in users and users[username] == password:
            session["username"] = username
            return redirect(url_for("enterSong"))
        return render_template("login.html", error="Invalid username or password")

#loads song submission page
@app.route("/enterSong")
def dashboard():
    if "username" not in session:
        return redirect(url_for("login"))




if __name__ == "__main__":
    app.run(debug=True)
