from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify({'message':'succes...'})


if __name__ == '__main__':
    app.run(debug=TRUE, port=500)
