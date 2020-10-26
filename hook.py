import logging
import asyncio
from pathlib import Path
from subprocess import Popen
from ssl import get_server_certificate

name = 'SSL'
description = 'Run an SSL proxy in front of the server'
address = ''

async def _check_cert():
    await asyncio.sleep(5)
    default_cert = ''
    server_cert = ''
    server_cert = get_server_certificate(('127.0.0.1', 8443))
    with open(Path('plugins/ssl/conf/insecure_certificate.pem'), 'r') as f:
        default_cert = f.read()
    if server_cert == default_cert:
        logging.warn('Insecure SSL private key and certificate in use. Consider generating and using your own '
                    'to improve security. Documentation found '
                    'here: https://github.com/mitre/caldera/wiki/Plugin:-ssl')


async def enable(services):
    haproxy_conf = Path('plugins/ssl/templates/haproxy.conf')
    user_conf = Path('plugins/ssl/conf/haproxy.conf')
    if user_conf.is_file():
        haproxy_conf = user_conf
    Popen(['haproxy', '-q', '-f', haproxy_conf])
    logging.debug('Serving at https://0.0.0.0:8443')
    loop = asyncio.get_event_loop()
    loop.create_task(_check_cert())