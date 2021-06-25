from flask import *
import psycopg2

app = Flask(__name__)


@app.route('/')
def abc():
    return render_template('login.html')

@app.route('/add', methods=['GET','POST'])
def bar():
    conn = psycopg2.connect(
    database="postgres", user='postgres', password='root', host='127.0.0.1', port= '5431')
    cursor = conn.cursor()
    if request.method=='POST':
        fname=request.form['t1']
        lname=request.form['t2']
        sql = "INSERT INTO test VALUES ('"+fname+"','"+lname+"')"
        cursor.execute(sql)
        conn.commit()
        sel="select * from test"
        cursor.execute(sel)
        chk=cursor.fetchall()
    conn.commit()
    conn.close()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
