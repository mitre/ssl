import logging
from subprocess import Popen

name = 'SSL'
description = 'Run an SSL proxy in front of CALDERA'
address = None


async def initialize(app, services):
    Popen(['haproxy', '-V', '-f', 'plugins/ssl/templates/haproxy.conf'])
    logging.debug('Serving CALDERA at https://127.0.0.1:443')

