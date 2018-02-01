from flask import Flask
import os


app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

listen = os.environ['NINED_SERVER_SERVICE_HOST'] # = 172.30.249.186
port = '8080'


@app.route("/")
def hello():
    return "Hello World!"

#if __name__ == "__main__":
app.run(host=listen, port = port)
