from flask import Flask, render_template

print(__name__)
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")