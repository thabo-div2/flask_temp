from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)


@app.route('/<name>')
def home(name):
    return render_template('homepage.html', name=name)


@app.route('/looping/<int:number>')
def looping(number):
    return render_template('Loopy.html', number=number)


@app.route('/times/<int:math>')
def timestable(math):
    return render_template('TimesTable.html', number=math)


if __name__ == "__main__":
    app.debug = True
    app.run()
