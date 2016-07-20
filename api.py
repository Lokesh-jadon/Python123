from flask import Flask
app = Flask(__name__)
app.config['DEBUG']=True
@app.route("/hello")
def hello():
    return "Hello World!"
@app.route("/username")
def fname():
    return "No User Name"

if __name__ == "__main__":
    app.run()
