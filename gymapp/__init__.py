from flask import Flask

app = Flask(__name__)
app.secret_key = 'ndkjauoa8D0dj2meM,AUD09D90e524@$@$)((DKPAd0'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:1111@localhost/gymdb?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True