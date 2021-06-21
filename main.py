from flask import Flask

app = Flask("Testing Heroku webapp")

@app.route("/",methods=["GET"])
def home():
    return "<h1>This is a Flask Api</h1>"

if __name__ == "__main__":
    app.run(debug=True)