from flask import Flask, render_template, request
from block import *

app = Flask(__name__)


@app.route('/')
def index():
    if request.method == 'POST':
        lender = request.form['lender']
        amount = request.form['amount']
        borrower = request.form['borrower']
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
