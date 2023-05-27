from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "HELLO World"

if __name__=="__main__":
    app.run("0.0.0.0")