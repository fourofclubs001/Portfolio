from flask import Flask, render_template, request, redirect, url_for
from modules.ContactForm import ContactForm
import requests
import secrets
import json
import os

path = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, template_folder = "templates")
app.config['SECRET_KEY'] = secrets.token_hex(32)

info = {}
info_path = os.path.join(path, "info.json")

with open(info_path, 'r') as info_file:
    info = json.load(info_file)

@app.route('/portfolio-details/<title>', methods = ["GET", "POST"])
def portfolio_details(title):
    item_info = {"title": title}
    return render_template("portfolio-details.html", info = info, item_info = item_info)

@app.route('/hero')
def hero():
    return redirect("/#hero")

@app.route('/about')
def about():
    return redirect("/#about")

@app.route('/resume')
def resume():
    return redirect("/#resume")

@app.route('/portfolio')
def portfolio():
    return redirect("/#portfolio")

@app.route('/services')
def services():
    return redirect("/#services")

@app.route('/contact')
def contact():
    return redirect("/#contact")

@app.route("/", methods = ["GET", "POST"])
def index():

    return render_template("index.html", info = info)

if __name__ == "__main__":

    app.run(debug = True)