# CALDERA plugin: SSL

This plugin switches CALDERA from using HTTP to HTTPS.

## Overview

When this plugin has been loaded, CALDERA will start the HAProxy service on the machine and then serve CALDERA at hxxps://[YOUR_IP]:8443, instead of the normal hxxp://[YOUR_IP]:8888.

All deployed agents should use the correct address to connect to CALDERA. 

If you would like to modify any of the proxy details, you can do so by going into the `templates/haproxy.conf` file, modifying the contents and restarting CALDERA.

## Requirements
* Any Linux or MacOS
* HaProxy >= 1.8

> install haproxy using `brew install haproxy` (MacOS) or `sudo apt-get install haproxy` (Linux)


**Warning:** This plugin uses a default self-signed ssl certificate and key which is insecure. It is highly recommended that you generate your own before using the plugin to increase the safety of the system. Find documentation to do so in the full CALDERA docs here: http://caldera.readthedocs.io
