from flask import Flask, render_template, request, g, redirect
import sqlite3

app = Flask(__name__)
door_is_open = True
DATABASE = "hando.db"

def get_db():
    db = getattr(g, "_database", None)
    if not db:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def read_user_pass():
    curr = get_db().cursor()
    curr.execute("SELECT * FROM hando")
    return curr.fetchall()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()

@app.route("/submit", methods=['POST'])
def receive():
    return add_user_pass_to_db(request.form['username'], request.form['password'])

def add_user_pass_to_db(username, password):
    cur = get_db().cursor()
    user_pass = (username, password)
    cur.execute("INSERT INTO hando VALUES (?, ?)", user_pass)
    get_db().commit()
    print(read_user_pass())
    for user, pasw in read_user_pass():
        print("User: " + user)
        print("Password: " + pasw)

    return redirect("/push")

@app.route('/')
def index():
    return render_template('index.html')

def is_door_opened():
	return not door_is_open

@app.route('/push', methods=['GET', 'POST'])
def push():
	global door_is_open
	print(door_is_open)
	door_is_open = is_door_opened()
	return render_template('push.html', door_is_open = door_is_open)

if __name__ == "__main__":
    app.run(debug=True)
