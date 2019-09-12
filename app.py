from flask import Flask
from flask import request
from werkzeug import secure_filename

app = Flask(__name__)

@app.route("/")
def get():
    return "Hello World!"

if __name__=='__main__':
    app.run(debug=True)