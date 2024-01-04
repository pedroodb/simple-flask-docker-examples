import os, time
from flask import Flask, render_template

from api import api


app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, Docker!'

# define route that creates a file with a timestamp as name at ./data
@app.route('/create_file')
def create_file():
    filename = str(time.time()) + '.txt'
    with open(os.path.join('data', filename), 'w') as f:
        f.write('Hello, Docker!')
    return 'File created: ' + filename

@app.route('/html')
def html_example():
    return render_template('html-demo.html')

@app.route('/json')
def json_example():
    return {'hello': 'docker'}

@app.route('/users/<username>')
def show_user(username):
    return f'{username}'

@app.route('/posts/<int:post_id>')
def show_post(post_id):
    return f'{post_id}'

@app.route('/template/<title>')
def template_example(title):
    return render_template('index.html', title=title)

@app.route('/loop')
def template_loop():
    return render_template('loop.html', items=['Juan', 'Pedro', 'Pablo'])

@app.route('/form')
def form():
    return render_template('form.html')

app.register_blueprint(api)

if __name__ == '__main__':
    app.run(host='0.0.0.0')