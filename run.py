from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def home():
    return jsonify(name='Flask API', version='0.0.1')


if __name__ == '__main__':
    app.run(debug=True)