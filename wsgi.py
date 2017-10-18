from flask import Flask, render_template, request

import requests

app = Flask("MyForm")

@app.route("/helloworld")
def hello_someone():
    return "hello world"

app.run(debug=True)
