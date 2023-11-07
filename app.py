from flask import Flask, render_template, request

app = Flask(__name__)


# make a homepage
@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/hello/<name>')
def hello(name):
    listOfNames = [name, "Yoyo", "Yennifer"]
    return render_template('name.html', name=name, nameList=listOfNames)

@app.route('/')
def aboutMe(name1):
    aboutlist = [name1, "Kayla"]
    return render_template('name.html', name1=name1, aboutlist=aboutlist)

@app.route('/form', methods=['GET', 'POST'])
def formDemo(name=None):
    if request.method == 'POST':
        name=request.form['name']
    return render_template('form.html', name=name)

@app.route('/interest/')
def favorite():
    return render_template('interest.html')

# add the option to run this file directly 
if __name__ == "__main__":
    app.run(debug=True)
    