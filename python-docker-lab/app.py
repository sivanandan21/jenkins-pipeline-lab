
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Welcome to Jenkins Docker CD Lab</h1>
    <p>Application successfully deployed using Docker!</p>
    """

@app.route('/health')
def health():
    return jsonify(status="healthy")

@app.route('/add/<int:a>/<int:b>')
def addition(a, b):
    return jsonify(result=a+b)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
