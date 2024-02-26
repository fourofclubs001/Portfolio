from flask import Flask, render_template, request, redirect, url_for
from modules.ContactForm import ContactForm
import requests
import secrets
import json
import os

path = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, template_folder = "templates")
app.config['SECRET_KEY'] = secrets.token_hex(32)

email_api_key = os.environ.get('MAILGUN_API_KEY')

info = {}
info_path = os.path.join(path, "info.json")

with open(info_path, 'r') as info_file:
    info = json.load(info_file)

@app.route("/", methods = ["GET", "POST"])
def index():

    contactForm = ContactForm()
    info["contact"]["form"] = contactForm

    if contactForm.validate_on_submit():

        name = contactForm.name.data
        email = contactForm.email.data
        subject = contactForm.subject.data
        message = contactForm.message.data

        body = 'Name: ' + name + ' Email: ' + email + '\n' + message

        response = requests.post(
		"https://api.mailgun.net/v3/sandbox4f5311015adf4863ba3ea4f0ade788be.mailgun.org/messages",
		auth=("api", email_api_key),
		data={"from": "postmaster@sandbox4f5311015adf4863ba3ea4f0ade788be.mailgun.org",
			"to": ["lucasvitali001@gmail.com"],
			"subject": subject,
			"text": body})

        isEmailSent = False

        return render_template("contact_form_response.html", isEmailSent = isEmailSent)

    return render_template("index.html", info = info)

if __name__ == "__main__":

    app.run(debug = True)