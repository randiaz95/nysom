from app1 import app
from flask import render_template, jsonify

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create")
def add():
    return jsonify({"status": "success",
                    "message": "Created a contact"})

@app.route("/update")
def update():
    return jsonify({"status": "success",
                    "message": "Updated a contact"})

@app.route("/delete")
def delete():
    return jsonify({"status": "success",
                    "message": "Deleted a contact"})

