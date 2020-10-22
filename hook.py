import logging
from pathlib import Path
from subprocess import Popen

name = 'SSL'
description = 'Run an SSL proxy in front of the server'
address = None


async def enable(services):
    haproxy_conf = Path('plugins/ssl/templates/haproxy.conf')
    user_conf = Path('plugins/ssl/conf/haproxy.conf')
    if user_conf.is_file():
        haproxy_conf = user_conf
    Popen(['haproxy', '-q', '-f', haproxy_conf])
    logging.debug('Serving at https://127.0.0.1:8443')
    cert = Path("plugins/ssl/conf/insecure_certificate.pem")
    if cert.is_file():
        logging.warn('Found insecure SSL private key and certificate. Consider generating your own and removing'
                     ' the insecure certificate from the conf directory to improve security. Documentation found '
                     'here: https://github.com/mitre/caldera/wiki/Plugin:-ssl')
