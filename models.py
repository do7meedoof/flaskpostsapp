import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath((__file__)))

def createPost(title, created, name, post):
    conn = sql.connect(path.join(ROOT, 'database.db'))
    cur = conn.cursor()

    cur.execute('insert into posts (title, created, name, content) values (?, ?, ?, ?)', (title, created, name, post))
    conn.commit()
    conn.close()

def getPosts():
    conn = sql.connect(path.join(ROOT, 'database.db'))
    cur = conn.cursor()

    cur.execute('select * from posts')
    posts = cur.fetchall()
    conn.close()

    return posts

def deletePost(id):
    conn = sql.connect(path.join(ROOT, 'database.db'))
    cur = conn.cursor()
    query = f'DELETE from posts where id = {id}'
    cur.execute(query)
    conn.commit()
    conn.close()

