from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import json
import os

path = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, template_folder = "templates")

info = {}
info_path = os.path.join(path, "info.json")

with open(info_path, 'r') as info_file:
    info = json.load(info_file)

@app.route("/")
def index():
    return render_template("index.html", info = info)


if __name__ == "__main__":

    app.run(debug = True)