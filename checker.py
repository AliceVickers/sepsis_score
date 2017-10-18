from flask import Flask, render_template, request

import requests

app = Flask("MyForm")

@app.route("/symptomchecker")
def hello_someone():
    return render_template("project.html")

app.run(debug=True)
