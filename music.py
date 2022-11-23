from flask import Flask, render_template
import pymysql

app = Flask(__name__)

@app.route('/')
def hello_world():
    MYSQL_HOST = 'localhost'
    MYSQL_CONN = pymysql.connect(
        host = MYSQL_HOST,
        port = 3306,
        user = 'root',
        passwd= '1234',
        db = 'song_db',
        charset='utf8'
    )
    db_cursor = MYSQL_CONN.cursor()
    sql = "SELECT * FROM song"
    db_cursor.execute(sql)
    song_lst = db_cursor.fetchall()
    MYSQL_CONN.commit()
    return render_template('test.html',song_lst = song_lst)


if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = '8080', debug = True)