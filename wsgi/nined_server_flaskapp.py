from flask import Flask
app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.route("/")
def hello():
    return "Hello World!"

#if __name__ == "__main__":
app.run()
