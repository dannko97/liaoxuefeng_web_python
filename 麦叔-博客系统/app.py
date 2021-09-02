from flask import Flask, render_template



app = Flask(__name__)


@app.route('/')
def index():
    return render_template("templates/index.html")

#set Flask_APP=blog;set Flask_ENV=development;flask run
