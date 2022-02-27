from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    with open('static/data/periodic_table.json') as file:
        data_set = json.load(file)
    return render_template("overview.html.j2", name = 'Hydrogen', 
                            elements = data_set['elements'])

app.run(debug=True)