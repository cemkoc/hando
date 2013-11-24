from flask import Flask, render_template, request, g, redirect
import sqlite3

app = Flask(__name__)

@app.route("/login", methods=['POST'])
def login():
    return redirect('/push')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/push', methods=['GET', 'POST'])
def push():
    return render_template('push.html', door_is_open=True)

if __name__ == "__main__":
    app.run(debug=True)
