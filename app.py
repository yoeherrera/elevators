from flask import Flask

app = Flask(__name__)

@app.route('/')
def home_page():
    return "<h1> Yoe rocks!!!!!</h1>"

if '__main__' == '__name__':
    app.run()