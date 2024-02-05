from flask import Flask, render_template, request, redirect, url_for
from modules.ContactForm import ContactForm
import json
import os

path = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, template_folder = "templates")
app.config['SECRET_KEY'] = 'secretkey'

info = {}
info_path = os.path.join(path, "info.json")

with open(info_path, 'r') as info_file:
    info = json.load(info_file)

@app.route("/", methods = ["GET", "POST"])
def index():

    contactForm = ContactForm()
    info["contact"]["form"] = contactForm

    if contactForm.is_submitted():

        name = contactForm.name
        email = contactForm.email
        subject = contactForm.subject
        message = contactForm.message

        return render_template("contact_form_response.html")

    return render_template("index.html", info = info, contactForm = contactForm)

if __name__ == "__main__":

    app.run(debug = True)