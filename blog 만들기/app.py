from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

# DB 설정
db_config = yaml.safe_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db_config['mysql_host']
app.config['MYSQL_USER'] = db_config['mysql_user']
app.config['MYSQL_PASSWORD'] = db_config['mysql_password']
app.config['MYSQL_DB'] = db_config['mysql_db']

mysql = MySQL(app)

# 게시글 목록
@app.route('/posts')
def get_posts():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM posts")
    posts = cur.fetchall()
    cur.close()
    return render_template('posts.html', posts=posts)

# 게시글 상세 보기
@app.route('/posts/<int:id>')
def get_post(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM posts WHERE id = %s", (id,))
    post = cur.fetchone()
    cur.close()
    return render_template('post_detail.html', post=post)

# 게시글 작성 폼
@app.route('/posts/new')
def new_post_form():
    return render_template('new_post.html')

# 게시글 작성 처리
@app.route('/posts', methods=['POST'])
def create_post():
    title = request.form['title']
    content = request.form['content']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO posts (title, content) VALUES (%s, %s)", (title, content))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('get_posts'))

# 게시글 수정
@app.route('/posts/<int:id>/edit', methods=['GET', 'POST'])
def update_post(id):
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        cur.execute("UPDATE posts SET title = %s, content = %s WHERE id = %s", (title, content, id))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('get_post', id=id))
    else:
        cur.execute("SELECT * FROM posts WHERE id = %s", (id,))
        post = cur.fetchone()
        cur.close()
        return render_template('edit_post.html', post=post)

# 게시글 삭제
@app.route('/posts/<int:id>/delete', methods=['POST'])
def delete_post(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM posts WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('get_posts'))

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def home():
    return redirect(url_for('get_posts'))
