from flask import Flask, render_template, request

import requests

app = Flask("MyForm")

@app.route("/symptomchecker")
def hello_someone():
    return render_template("project.html")
    print form_data["name"]
    print form_data["admission"]

app.run(debug=True)
