from flask import Flask

server = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello docker!!!"


if __name__ == "__main__":
    server.run(debug=True)