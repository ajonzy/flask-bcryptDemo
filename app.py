from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_heroku import Heroku
from flask_bcrypt import Bcrypt

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = ""

heroku = Heroku(app)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

if __name__ == "__main__":
    app.debug = True
    app.run()