from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import json

app = Flask(__name__, template_folder = "templates")

info = {}
info_path = "C:/Users/usuario/repositories/Portfolio/info.json"

with open(info_path, 'r') as info_file:
    info = json.load(info_file)

@app.route("/")
def index():
    return render_template("index.html", info = info)


if __name__ == "__main__":

    app.run(debug = True)