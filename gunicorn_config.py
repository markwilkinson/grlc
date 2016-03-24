workers = 1
worker_class = 'gevent'
bind = '0.0.0.0:5000'
pidfile = '/tmp/gunicorn-grlc.pid'
debug = False
reload = True
loglevel = 'info'
errorlog = '/tmp/gunicorn_grlc_error.log'
accesslog = '/tmp/gunicorn_grlc_access.log'
daemon = True