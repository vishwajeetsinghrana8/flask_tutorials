from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    list1 = ["Vishwajeet","Ravi","Sunil","Micky","Adarsh"]
    return render_template('main.html',list1=list1)


if __name__ == '__main__':
    app.run(debug=True)
