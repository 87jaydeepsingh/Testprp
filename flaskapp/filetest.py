from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os
import psycopg2
app = Flask(__name__)
UPLOAD_FOLDER = './static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/upload')
def upload_file():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file1():
    conn = psycopg2.connect(
    database="postgres", user='postgres', password='root', host='127.0.0.1', port= '5431')
    cursor = conn.cursor()
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],"abc"+f.filename))
        sql = "INSERT INTO photo VALUES ('"+"abc"+f.filename+"')"
        cursor.execute(sql)
        conn.commit()
        conn.close()
        return 'file uploaded successfully'

@app.route('/photo', methods=['GET','POST'])
def adash():
    conn = psycopg2.connect(
    database="postgres", user='postgres', password='root', host='127.0.0.1', port= '5431')
    cursor = conn.cursor()
    cursor.execute("select *from photo")
    chk=cursor.fetchone()
    print(chk)
    conn.commit()
    conn.close()
    return render_template('photo.html',data=chk)

if __name__ == '__main__':
   app.run(debug = True)