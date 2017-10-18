from flask import Flask, render_template, request

import requests

app = Flask(__name__)

@app.route("/helloworld")
def hello_someone():
    return "hello world"

@app.route("/symptomchecker")
def symptomchecker():
    return render_template("project.html")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
