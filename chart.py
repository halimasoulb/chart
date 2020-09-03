from flask import Flask, render_template, request
import mysql.connector as MC
import pymysql

app = Flask(__name__)

def getConnection ():
    return pymysql.connect (
        host = 'localhost',
        db = 'consomation',
        user = 'root',
        password = 'password',
        charset = 'utf8',
        cursorclass = pymysql.cursors.DictCursor
    )

@ app.route ('/chart')
def select_sql ():
    #connection = getConnection ()
    conn = MC.connect(host = 'localhost', database = 'consomation', user = 'root', password = 'password')
    cursor = conn.cursor()
    req = 'SELECT * FROM request'
    cursor.execute(req)
    request_list = cursor.fetchall()

    data = list()
    for n in request_list:
        data.append(format(n[4]))
        #print(data)
        #print('Date :{}'.format(n[1]), 'Intensite :{}'.format(n[4]) )

    labels = list()
    for date in request_list:
        labels.append(format(date[1]))
    

    return render_template ('chart.html', data=data, labels=labels)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()