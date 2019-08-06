import logging
import filecmp
from subprocess import Popen

name = 'SSL'
description = 'Run an SSL proxy in front of CALDERA'
address = None


async def initialize(app, services):
    Popen(['haproxy', '-q', '-f', 'plugins/ssl/templates/haproxy.conf'])
    logging.debug('Serving at https://127.0.0.1:443')
    config = open('plugins/ssl/templates/haproxy.conf', 'r').read()
    path = config[config.index('crt') + 4:config.index('.pem') + 4]
    if filecmp.cmp('plugins/ssl/conf/ssl_cert.pem', path):
        logging.debug('Warning: Using insecure ssl private key and certificate. Consider generating your own to improve security. Documentation found here: https://github.com/mitre/caldera/wiki/Plugin:-ssl')




