from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)




def create_table():
    conn = sqlite3.connect('lfs.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, id INTEGER PRIMARY KEY AUTOINCREMENT,password TEXT, number TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS sale (name TEXT, description TEXT, price TEXT, rollno TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS lost (name TEXT, colourmodel TEXT, description TEXT, rollno TEXT)")
    conn.commit()
    conn.close()

create_table()



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['POST'])
def sign():
    if request.method == "POST":
        song_name = request.form['Name']
        print(song_name)






if __name__ == '__main__':
    app.run(debug=True)
