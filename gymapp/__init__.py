from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'ndkjauoa8D0dj2meM,AUD09D90e524@$@$)((DKPAd0'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:1111@localhost/gymdb29?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)
login_manager = LoginManager(app)