from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
        <h1>Welcome! hello-flsk project!</h1>
        <a href="/hello">hello</a>
    """

@app.route('/hello')
def hello():
    return "<p>Hello, World!</p>"
