from flask import Flask, render_template, request, redirect, url_for
import scraper
import json

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def form():
    return render_template("form.html")


@app.route('/verify', methods=['POST', 'GET'])
def verify():
    if request.method == 'POST':
        email = request.form['username']
        password = request.form['password']
        json_list = scraper.scrape_canvas(email, password)
        return render_template("home.html", data=json_list)
       # return redirect(f"/user/{email}/{password}")
    else:
        return render_template("test.html")


@app.route('/user/<name>/<password>')
def user(name, password):
    return f"Your name is hello"


app.run(host='localhost', port=5000)
