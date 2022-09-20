import logging

#logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
#logging.basicConfig(level=logging.INFO)
logging.basicConfig(format='%(threadName)s:%(thread)s:%(levelname)s:%(message)s', level=logging.INFO)
logging.debug('loggingの使い方')
logging.info('loggingの使い方')
logging.warning('loggingの使い方')
logging.error('loggingの使い方')
logging.critical('loggingの使い方')