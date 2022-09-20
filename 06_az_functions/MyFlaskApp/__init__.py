from flask import Flask

# from logging.config import dictConfig
# dictConfig({
#     'version': 1,
#     'formatters': {'default': {
#         'format': '%(threadName)s:%(thread)s:[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
#     }},
#     'handlers': {'wsgi': {
#         'class': 'logging.StreamHandler',
#         'stream': 'ext://flask.logging.wsgi_errors_stream',
#         'formatter': 'default'
#     }},
#     'root': {
#         'level': 'INFO',
#         'handlers': ['wsgi']
#     }
# })

app = Flask(__name__)

@app.route('/')
def top():
    app.logger.debug('loggingの使い方')
    app.logger.info('loggingの使い方')
    app.logger.warning('loggingの使い方')
    app.logger.error('loggingの使い方')
    app.logger.critical('loggingの使い方')
    return 'top page.'

@app.route('/hello')
@app.route('/hello/<username>')
def hell_world(username=None):
    logging.info('hello start.')    
    return 'hello my flask app! {}'.format(username);

def main():
    #app.debug = True
    app.run()

if __name__ == '__main__':
    main()