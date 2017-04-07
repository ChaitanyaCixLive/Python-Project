from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/post/<int:post_id>')
def post(post_id):
    return "<h1>this is post with id "+str(post_id)+"</h2>"


if __name__ == '__main__':
    app.run()
