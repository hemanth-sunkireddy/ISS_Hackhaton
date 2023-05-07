from flask import Flask, render_template, request, jsonify, url_for, redirect,flash, make_response
import sqlite3
from datetime import datetime
import os
os.urandom(24)


app = Flask(__name__)
app.secret_key = "your_secret_key"



def create_table():
    conn = sqlite3.connect('lfs.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, ROLLNO INTEGER PRIMARY KEY ,password TEXT, number TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS currentuser (name TEXT, ROLLNO TEXT,password TEXT, number TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS sale (name TEXT, description TEXT, price TEXT, rollno TEXT, status TEXT, user TEXT, mobile TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS lost (name TEXT, colourmodel TEXT, description TEXT, status TEXT, rollno TEXT, user TEXT, mobile TEXT)")
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
        c.execute("DELETE FROM currentuser;")
        c.execute("INSERT INTO users (name, ROLLNO,number,password) VALUES (?, ?,?,?)", (student_name, student_rollno,student_mobile,student_password))
        c.execute("INSERT INTO currentuser (name, ROLLNO,number,password) VALUES (?, ?,?,?)", (student_name, student_rollno,student_mobile,student_password))
        conn.commit()
        conn.close()
        return render_template('homepage.html')
    

@app.route('/signin', methods=['POST', 'GET'])
def signin():
    error = None
    if request.method == 'POST':
        student_rollno=request.form['rollNo']
        student_password=request.form['password']
        conn = sqlite3.connect('lfs.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE ROLLNO = ?", (student_rollno,))
        user = c.fetchone()
        if user is None:
            error = 'Incorrect username.'
            return (render_template('index.html', error=error))
            

        elif student_password == user[2]:
            c.execute("INSERT INTO currentuser (name, ROLLNO,password,number) VALUES (?, ?,?,?)", (user[0], student_rollno,user[3],student_password))
            conn.commit()
            print("hi")
            return render_template('homepage.html')
        else:
            error = 'Incorrect password.'
            return (render_template('index.html', error=error))


@app.route('/')
def index3():
    conn = sqlite3.connect('lfs.db')
    c = conn.cursor()
    # c.execute("DELETE FROM currentuser;")
    return render_template('index.html',error=None)

@app.route('/index.html')
def index4():
    conn = sqlite3.connect('lfs.db')
    c = conn.cursor()
    c.execute("DELETE FROM currentuser;")
    conn.commit()
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    description = request.form['description']
    price=request.form['price']
    action=request.form['action']
    conn = sqlite3.connect('lfs.db')
    c = conn.cursor()
    
    c.execute("SELECT * FROM currentuser")
    current_user = c.fetchone()
    rollno = current_user[1]
    user=current_user[0]
    mobile=current_user[3]
    c.execute("INSERT INTO sale (name, description, price, rollno, user, mobile, status) VALUES (?, ?, ?, ?, ?, ?, ?)", (name, description, price, rollno, user, mobile, 0 if action=='Sell' else 1 if action=='Lend' else 2))
    conn.commit()
    conn.close()
    return render_template('sell.html')



@app.route('/submit1', methods=['POST'])
def submit1():
    name = request.form['name']
    description = request.form['description']
    colourmodel=request.form['colourmodel']
    action=request.form['action']
    conn = sqlite3.connect('lfs.db')
    c = conn.cursor()
    c.execute("SELECT * FROM currentuser")
    current_user = c.fetchone()
    rollno = current_user[1]
    user=current_user[0]
    mobile=current_user[3]
    c.execute("INSERT INTO lost (name, description, colourmodel, rollno, user, mobile, status) VALUES (?, ?, ?, ?, ?, ?, ?)", (name, description,colourmodel,rollno,user,mobile, 0 if action=='Lost' else 1))
    conn.commit()
    conn.close()
    return render_template('lostfoundAdd.html')


@app.route('/submit2', methods=['POST'])

def submit2():
    name = request.form['name']
    description = request.form['description']
    colourmodel=request.form['colourmodel']
    action=request.form['action']
    conn = sqlite3.connect('lfs.db')
    c = conn.cursor()
    c.execute("SELECT * FROM currentuser")
    current_user = c.fetchone()
    rollno = current_user[1]
    user=current_user[0]
    mobile=current_user[3]
    c.execute("INSERT INTO lost (name, description, colourmodel, rollno, user, mobile, status) VALUES (?, ?, ?, ?, ?, ?, ?)", (name, description,colourmodel,rollno,user,mobile, 0 if action=='Lost' else 1))
    conn.commit()
    conn.close()
    return render_template('lostfoundAdd.html')






# Form for adding the items to sell
@app.route('/sell.html')
def sell():
    return render_template('sell.html')



# List of Items up for buying or borrowing
@app.route('/buy.html')
def buy():
    conn = sqlite3.connect('lfs.db')
    c = conn.cursor()
    c.execute("SELECT * FROM sale WHERE status != 1")
    rows = c.fetchall()
    conn.close()
    return render_template('buy.html',rows=rows)

@app.route('/borrow.html')
def borrow():
    conn = sqlite3.connect('lfs.db')
    c = conn.cursor()
    c.execute("SELECT * FROM sale WHERE status != 0")
    rows = c.fetchall()
    conn.close()
    return render_template('borrow.html',rows=rows)

# List of Items which are found
@app.route('/foundView.html')
def foundView():
    conn = sqlite3.connect('lfs.db')
    c = conn.cursor()
    c.execute("SELECT * FROM lost WHERE status != 0")
    rows = c.fetchall()
    conn.close()
    return render_template('foundView.html', rows=rows)



# Form for adding the items which are lost/found  
@app.route('/lostfoundAdd.html')
def foundAdd():
    return render_template('lostfoundAdd.html')





# @app.route('/lostAdd.html')
# def lostAdd():
#     return render_template('lostAdd.html')

# List of Items which are lost
@app.route('/lostView.html')
def lostView():
    conn = sqlite3.connect('lfs.db')
    c = conn.cursor()
    c.execute("SELECT * FROM lost WHERE status != 1")
    rows = c.fetchall()
    conn.close()
    return render_template('/lostView.html', rows=rows)

@app.route('/homepage.html')
def home():
    return render_template('homepage.html')

@app.route('/studentProfile.html')
def studentProfile():

    conn = sqlite3.connect('lfs.db')
    c = conn.cursor()

    c.execute("SELECT * FROM currentuser")
    unique_rollID = c.fetchone()[1]
    c.execute("SELECT * FROM users WHERE ROLLNO = ?", (unique_rollID,))
    user_details=c.fetchall()

    c.execute("SELECT * FROM lost WHERE ROLLNO = ? AND status = ?", (unique_rollID, 0))
    lost_details=c.fetchall()

    c.execute("SELECT * FROM lost WHERE ROLLNO = ? AND status = ?",(unique_rollID, 1))
    found_details = c.fetchall()

    c.execute("SELECT * FROM sale WHERE ROLLNO = ? AND status != ?",(unique_rollID, 1))
    sell_details = c.fetchall()

    c.execute("SELECT * FROM sale WHERE ROLLNO = ? AND status != ?",(unique_rollID, 0))
    buy_details = c.fetchall()
    
    
    conn.close()
    return render_template('studentProfile.html', user=user_details, lost=lost_details, found=found_details, sell=sell_details, buy=buy_details)



@app.route('/remove-from-sell', methods=['POST'])
def remove_from_sell():
    song_id = request.json['name']
    conn = sqlite3.connect('lfs.db')
    c = conn.cursor()
    c.execute("DELETE FROM sale WHERE name=?", (song_id,))
    conn.commit()
    conn.close()
    return jsonify({'success': True})


@app.route('/remove-from-lost', methods=['POST'])
def remove_from_lost():
    song_id = request.json['name']
    conn = sqlite3.connect('lfs.db')
    c = conn.cursor()
    c.execute("DELETE FROM lost WHERE name=?", (song_id,))
    conn.commit()
    conn.close()
    return jsonify({'success': True})





if __name__ == '__main__':
    app.run(debug=True)
