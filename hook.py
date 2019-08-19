import logging
from pathlib import Path
from subprocess import Popen

name = 'SSL'
description = 'Run an SSL proxy in front of the server'
address = None


async def initialize(app, services):
    Popen(['haproxy', '-q', '-f', 'plugins/ssl/templates/haproxy.conf'])
    logging.debug('Serving at https://127.0.0.1:443')
    cert = Path("plugins/ssl/conf/insecure_certificate.pem")
    if cert.is_file():
        logging.warn('Found insecure ssl private key and certificate. Consider generating your own and removing the insecure certificate from the conf directory to improve security. Documentation found here: https://github.com/mitre/caldera/wiki/Plugin:-ssl')




