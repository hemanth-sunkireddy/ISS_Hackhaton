from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)




def create_table():
    conn = sqlite3.connect('lfs.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, id INTEGER PRIMARY KEY AUTOINCREMENT,password TEXT, number TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS sale (name TEXT, description TEXT, price TEXT, rollno TEXT, status TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS lost (name TEXT, colourmodel TEXT, description TEXT, rollno TEXT)")
    conn.commit()
    conn.close()

create_table()



@app.route('/signup', methods=['POST'])
def signup():
    if request.method == "POST":
        student_name = request.form['name']
        student_rollno=request.form['rollNo']
        student_mobile=request.form['mobile']
        student_password=request.form['password']
        conn = sqlite3.connect('lfs.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (name, id,password,number) VALUES (?, ?,?,?)", (student_name, student_rollno,student_mobile,student_password))
        conn.commit()
        conn.close()
        render_template('homepage.html')
    


@app.route('/signin', methods=['POST', 'GET'])
def signin():
    if request.method == "POST":
        student_rollno=request.form['rollNo']
        student_password=request.form['password']
        print(student_password)
        print(student_rollno)
        render_template('homepage.html')


@app.route('/')
def index():
    return render_template('sell.html')


@app.route('/submit', methods=['POST'])
def submit():
   
    name = request.form['name']
    description = request.form['description']
    price=request.form['price']
    action=request.form['action']

    conn = sqlite3.connect('lfs.db')
    c = conn.cursor()
    c.execute("INSERT INTO sale (name, description, price, status) VALUES (?, ?, ?, ?)", (name, description, price, 0 if action=='Sell' else 1 if action=='Lend' else 2))
    conn.commit()
    conn.close()
    return render_template('sell.html')



@app.route('/submit1', methods=['POST'])
def submit1():
    name = request.form['name']
    description = request.form['description']
    colourmodel=request.form['colourmodel']

    conn = sqlite3.connect('lfs.db')
    c = conn.cursor()
    c.execute("INSERT INTO lost (name, description, colourmodel) VALUES (?, ?, ?)", (name, description,colourmodel))
    conn.commit()
    conn.close()
    return render_template('found.html')


@app.route('/submit2', methods=['POST'])
def submit2():
    name = request.form['name']
    description = request.form['description']
    colourmodel=request.form['colourmodel']

    conn = sqlite3.connect('lfs.db')
    c = conn.cursor()
    c.execute("INSERT INTO lost (name, description, colourmodel) VALUES (?, ?, ?)", (name, description,colourmodel))
    conn.commit()
    conn.close()
    return render_template('lost.html')

@app.route('/view.html')
def view():
    return render_template('view.html')


@app.route('/lost.html')
def loss():
    return render_template('lost.html')

@app.route('/sell.html')
def sell():
    return render_template('sell.html')


@app.route('/buy.html')
def buy():
    return render_template('buy.html')


@app.route('/foundView.html')
def foundView():
    return render_template('foundView.html')

@app.route('/successFoundAdd.html', methods=['POST', 'GET'])
def successFoundAdd():
    if request.method == "POST":
        return "Added successfully"


@app.route('/foundAdd.html')
def foundAdd():
    return render_template('foundAdd.html')

@app.route('/lostAdd.html')
def lostAdd():
    return render_template('lostAdd.html')


@app.route('/lostView.html')
def lostView():
    return render_template('/lostView.html')


@app.route('/borrow.html')
def borrow():
    return render_template('borrow.html')
if __name__ == '__main__':
    app.run(debug=True)
