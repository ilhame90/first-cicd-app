from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    x = "Hellooo from 8"
    y = "Ilhama and"
    z = "Aggun"
    return " ".join(x, y, z)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
