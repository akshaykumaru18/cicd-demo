from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    print("Hello  fadf")
    return 'Hello, bombay error!'

if __name__ == '__main__':
    app.run(debug=True)