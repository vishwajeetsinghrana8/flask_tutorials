from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    name = "Vishwajeet"
    list1 = list(name)
    dict1= {"YouTube":"Knowledge Shelf"}
    return render_template('main.html', name=name, list1=list1,dict1 = dict1)

if __name__ == '__main__':
    app.run(debug=True)
