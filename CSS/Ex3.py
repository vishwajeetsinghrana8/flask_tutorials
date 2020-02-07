from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Knowledge Shelf!!!</h1>'

@app.route('/info')
def info():
    return '<h1>Vishwajeet Singh Rana</h1>'

@app.route('/friend/<name>')
def frined(name):
    return 'Last char of any name {}'.format(name[-1])

if __name__ == '__main__':
    app.run(debug=True)
