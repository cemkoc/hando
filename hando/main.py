from flask import Flask, render_template, request, g, redirect
import json

app = Flask(__name__)

door_should_open = False

@app.route("/login", methods=['POST'])
def login():
    return redirect('/push')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/push', methods=['GET'])
def push():
    return render_template('push.html')

@app.route('/status', methods=['GET'])
def status():
    return json.dumps(door_should_open)

@app.route('/command', methods=['POST'])
def command():
    global door_should_open
    door_should_open = not door_should_open
    return 'OK'

@app.route('/endpoint', methods=['POST'])
def endpoint():
    jstatus = request.stream.read()
    status = json.loads(jstatus)
    command = {'action': ['closed', 'open'][door_should_open]}
    jcommand = json.dumps(command)
    return jcommand

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
