from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

@app.route("/")
def periodic_table():
    with open('static/data/periodic_table.json') as file:
        data_set = json.load(file)
    return render_template("overview.html.j2", elements = data_set['elements'])

if __name__ == "__main__":
    app.run(debug=True)