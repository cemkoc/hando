from flask import Flask, render_template, request
app = Flask(__name__)
door_is_open = True

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
