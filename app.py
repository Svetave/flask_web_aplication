import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
import os

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        organization = request.form['organization']
        analit = request.form['analit']
        genome = request.form['genome']
        samples = request.form['samples']
        mode = request.form['mode']
        genes = request.form['genes']
        comment = request.form['comment']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, organization, analit, genome, samples, mode, genes, comment) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                         (title, organization, analit, genome, samples, mode, genes, comment))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/about', methods=('GET', 'POST'))
def about():
    return render_template('about.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        organization = request.form['organization']
        analit = request.form['analit']
        genome = request.form['genome']
        samples = request.form['samples']
        mode = request.form['mode']
        genes = request.form['genes']
        comment = request.form['comment']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, organization = ?, analit = ?, genome = ?, samples = ?, mode = ?, genes = ?, comment = ?'
                        ' WHERE id = ?',
                        (title, organization, analit, genome, samples, mode, genes, comment, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))

@app.route('/upload-file', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'There is file is submitted form.'
        file = request.files['file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return 'File upload successful.'
    else:
        return 'Invalid request.'

if __name__ == "__main__":
   app.run()