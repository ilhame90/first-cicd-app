from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    x = "Hellooo!!! from Ilhama test 2 teting 2nd case"
    return x
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
