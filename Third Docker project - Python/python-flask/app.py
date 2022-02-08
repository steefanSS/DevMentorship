import os
from flask import flask, render_template, abort, url_for, json, jsponify
import json

app = Flask(__name__,template_folder='.')
with open('file.json', 'r') as myfile:
    data=myfile.read()

@app.route("/")
def index():
    return render_template('index.html', title="page", jsonfile=json.dumps(data))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port= 8084)