import sqlite3
from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def welcome():
    return "WELCOME TO ABC BANK"

@app.route('/register', methods = ['POST'])
def register():
    data = request.get_json()
    connection = sqlite3.connect('abc.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS client (id text , password text,balance text)')
    cursor.execute("INSERT INTO client VALUES ('{}','{}','{}')".format(data['id'],data['password'],data['balance']))
    connection.commit()
    return 'Account created successfully...'





@app.route('/show')
def show():
        connection = sqlite3.connect('abc.db')
        cursor = connection.cursor()
        return {'client': list(cursor.execute("SELECT * FROM client"))}


@app.route('/showindi',methods = ['POST'])
def showindi():
    data = request.get_json()
    connection = sqlite3.connect('abc.db')
    cursor = connection.cursor()
    return "'client': {} , {} ".format(data['id'],data['password'])


@app.route('/update', methods = ['POST'])
def update():
        data = request.get_json()
        connection = sqlite3.connect('abc.db')
        cursor = connection.cursor()
        cursor.execute("UPDATE  client  SET password = '{}' WHERE id = '{}'".format(data['password'],data['id']))
        connection.commit()
        return 'Account details changed successfully...'


@app.route('/delete', methods = ['POST'])
def delete():
        data = request.get_json()
        connection = sqlite3.connect('abc.db')
        cursor = connection.cursor()
        cursor.execute("DELETE FROM  client  WHERE id = '{}'".format(data['id']))
        connection.commit()
        return 'Account deleted successfully...'


@app.route('/updatebal',methods = ['POST'])
def upbal():
    data = request.get_json()
    connection = sqlite3.connect('abc.db')
    cursor = connection.cursor()
    cursor.execute("UPDATE client SET balance = '{}' WHERE id = '{}'".format(data['balance'],data['id']))
    connection.commit()
    return 'Account balance updated succesfully'




app.run(port=5000)