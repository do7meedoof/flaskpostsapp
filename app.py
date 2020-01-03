from flask import Flask, render_template, request, redirect
from flask_cors import CORS
from models import createPost, getPosts, deletePost

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST', 'GET'])
def index():
    if(request.method == 'GET'):
        pass

    if(request.method == 'POST'):
        title = request.form.get('title')
        date = request.form.get('date')
        name = request.form.get('name')
        post = request.form.get('post')

        createPost(title, date, name, post)

    posts = getPosts()

    return render_template('index.html', posts=posts)

@app.route('/del/<int:id>')
def delete(id):
    deletePost(id)

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)