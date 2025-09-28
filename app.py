from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world! Welcome to my flask App! Learning Jenkins is Fun 😃"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
