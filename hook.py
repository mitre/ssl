from subprocess import Popen

name = 'SSL'
description = 'Run an SSL proxy in front of CALDERA'
address = None


async def initialize(app, services):
    proxy_args = ['haproxy', '-V', '-f', 'plugins/proxy/templates/haproxy.conf']
    return Popen(proxy_args)


