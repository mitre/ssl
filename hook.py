from subprocess import Popen

name = 'Proxy'
description = 'Spawn a reverse proxy service in front of the Caldera app'
address = None


async def initialize(app, services):
    proxy_args = ['haproxy', '-V', '-f', 'plugins/proxy/templates/haproxy.conf']
    return Popen(proxy_args)


