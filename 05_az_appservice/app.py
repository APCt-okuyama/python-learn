from flask import Flask

app = Flask(__name__)

@app.route('/')
def top():
    return 'top page.'

@app.route('/hello')
@app.route('/hello/<username>')
def hell_world(username=None):
    return 'hello my flask app! {}'.format(username);

def main():
    #app.debug = True
    app.run()

if __name__ == '__main__':
    main()