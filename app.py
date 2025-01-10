from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/message")
def message():
    return "This is the Flask App!"

if __name__=="__main__":
    app.run()