import requests
from flask import Flask, render_template, url_for, request

app = Flask("MyApp")

@app.route("/") 
def first_page():
	return render_template("first_page.html")


@app.route("/symptomchecker", methods=["POST"])
def symptom_checker():
	systolic = request.form['systolic_pressure']
	return "ok"

@app.route("/project")
def load_thing():
	return render_template("project.html")

app.run(debug=True)


#Make new template file that I will render using the render_template function 
#Get request.form into the template so you can extract the data and then put this into my page 
#This may involve importing a new function/class 