# https://realpython.com/flask-connexion-rest-api/
# app.py

# from flask import Flask, render_template
# app = Flask(__name__)

from flask import render_template # Remove: import Flask
import connexion

app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")


@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)