from flask import Blueprint, request, render_template, redirect, url_for, jsonify, current_app
from MySQLdb.cursors import DictCursor  # 추가

posts_bp = Blueprint('posts', __name__, url_prefix='/posts')

@posts_bp.route('/')
def get_all_posts():
    mysql = current_app.config['MYSQL']
    cur = mysql.connection.cursor(DictCursor)  # 수정
    cur.execute("SELECT * FROM posts ORDER BY created_at DESC")
    posts = cur.fetchall()
    cur.close()
    return render_template('index.html', posts=posts)

@posts_bp.route('/<int:id>')
def get_post(id):
    mysql = current_app.config['MYSQL']
    cur = mysql.connection.cursor(DictCursor)  # 수정
    cur.execute("SELECT * FROM posts WHERE id = %s", (id,))
    post = cur.fetchone()
    cur.close()
    return render_template('post.html', post=post)

@posts_bp.route('/create')
def create_form():
    return render_template('create.html')

@posts_bp.route('/create', methods=['POST'])
def create_post():
    mysql = current_app.config['MYSQL']
    title = request.form['title']
    content = request.form['content']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO posts (title, content) VALUES (%s, %s)", (title, content))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('posts.get_all_posts'))

@posts_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit_post(id):
    mysql = current_app.config['MYSQL']
    cur = mysql.connection.cursor(DictCursor)  # 수정
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        cur.execute("UPDATE posts SET title=%s, content=%s WHERE id=%s", (title, content, id))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('posts.get_post', id=id))
    else:
        cur.execute("SELECT * FROM posts WHERE id=%s", (id,))
        post = cur.fetchone()
        cur.close()
        return render_template('edit.html', post=post)

@posts_bp.route('/<int:id>/delete', methods=['POST'])
def delete_post(id):
    mysql = current_app.config['MYSQL']
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM posts WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('posts.get_all_posts'))

@posts_bp.route('/api', methods=['GET'])
def api_get_all_posts():
    mysql = current_app.config['MYSQL']
    cur = mysql.connection.cursor(DictCursor)  # 수정
    cur.execute("SELECT * FROM posts ORDER BY created_at DESC")
    posts = cur.fetchall()
    cur.close()
    return jsonify(posts)

@posts_bp.route('/api/<int:id>', methods=['GET'])
def api_get_post(id):
    mysql = current_app.config['MYSQL']
    cur = mysql.connection.cursor(DictCursor)  # 수정
    cur.execute("SELECT * FROM posts WHERE id = %s", (id,))
    post = cur.fetchone()
    cur.close()
    return jsonify(post)
