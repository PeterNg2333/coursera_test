'''
調用相關package 
'''
from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL, MySQLdb



app = Flask(__name__)


USERNAME = "share"
PASSWORD = "Take@@2022Xie"
HOST = "1.13.186.67"
DB = "lims-meinv"
PORT = 33307
'''
import pymysql
conn = pymysql.connect(host=HOST, port=PORT, user=USERNAME, passwd=PASSWORD, db=DB)
cursor = conn.cursor()
print (cursor)
'''

app.config['MYSQL_HOST'] = HOST
app.config['MYSQL_USER'] = USERNAME
app.config['MYSQL_PASSWORD'] = PASSWORD
app.config['MYSQL_DB'] = DB
app.config['MYSQL_PORT'] = PORT
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

def OK():
    with app.app_context():
        mysql = MySQL(app)
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(""" SELECT id, batch_id,operation \
                           FROM `lims-meinv`.t_batch_specimen_operation \
                           Where id in ("1325", "1326", "1328") """)
        extracted_data = cursor.fetchall()
        cursor.close()
        print (extracted_data)


# OK()

@app.route('/', methods = ['GET'])
def index():
    with app.app_context():
        mysql = MySQL(app)
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(""" SELECT id, batch_id,operation \
                           FROM `lims-meinv`.t_batch_specimen_operation \
                           Where id in ("1325", "1326", "1328") """)
        extracted_data = cursor.fetchall()
        cursor.close()
        '''
        results = []
        for each_record in extracted_database:
            results.append({"id": each_record[0], "batch_id": each_record[1], "batch_id":each_record[2]})
        # results = [{"id": 123, "batch_id": 246}, {"id": 456, "batch_id": 579}]
        '''
    return jsonify(extracted_data)

if __name__ == "__main__":
   app.run()
