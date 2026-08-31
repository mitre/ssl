# Caldera plugin: SSL

## Overview:

This plugin switches Caldera from using HTTP to HTTPS.

### Context:
Infrastructure security

### Known Limitations:

Plugins and agents will not automatically update to the service at https://[YOUR_IP]:8443. All agents will need to be redeployed using the HTTPS address to use the secure protocol. The address will not automatically populate in the agent deployment menu. If a self-signed certificate is used, deploying agents may require additional commands to disable SSL certificate checks (such as using the `--insecure` flag to bypass SSL certificate checks in the initial curl request when downloading the new agents).

## Installation:

Note: OpenSSL must be installed on your system to generate a new self-signed certificate
1. install haproxy >= 1.8 using `brew install haproxy` (MacOS) or `sudo apt-get install haproxy` (Linux).
2. In the root Caldera directory, navigate to `plugins/ssl`.
3. Place a PEM file containing SSL public and private keys in `conf/certificate.pem`. 
Follow the instructions below to generate a new self-signed certificate:
- In a terminal, paste the command `openssl req -x509 -newkey rsa:4096  -out conf/certificate.pem -keyout conf/certificate.pem -nodes` and press enter.
- This will prompt you for identifying details. Enter your country code when prompted. You may leave the rest blank by pressing enter.
4. Copy the file `haproxy.conf` from the `templates` directory to the `conf` directory.
5. Open the file `conf/haproxy.conf` in a text editor.
6. On the line `bind *:8443 ssl crt plugins/ssl/conf/insecure_certificate.pem`, replace `insecure_certificate.pem` with `certificate.pem`.
7. On the line `server caldera_main 127.0.0.1:8888 cookie caldera_main`, replace `127.0.0.1:8888` with the host and port defined in Caldera’s `conf/local.yml` file. This should not be required if Caldera’s configuration has not been changed.
8. Save and close the file. Congratulations! You can now use Caldera securely by accessing the UI https://[YOUR_IP]:8443 and redeploying agents using the HTTPS service.

## Dependencies/Requirements:

* Any Linux or MacOS
* HaProxy >= 1.8

> install haproxy using `brew install haproxy` (MacOS) or `sudo apt-get install haproxy` (Linux)

**Warning:** This plugin uses a default self-signed ssl certificate and key which is insecure. It is highly recommended that you generate your own before using the plugin to increase the safety of the system. Find documentation to do so in the full Caldera docs here: http://caldera.readthedocs.io
If using a self-signed certificate, you may have to update your system preferences to trust the certificate. Additionally, when downloading agents with `curl`, you may have to use the `--insecure` flag to ignore the SSL certificate check for the Caldera server.

## Getting Started:

When this plugin has been loaded, Caldera will start the HAProxy service on the machine and then serve Caldera at hxxps://[YOUR_IP]:8443, instead of the normal hxxp://[YOUR_IP]:8888.

All deployed agents should use the correct address to connect to Caldera. 

If you would like to modify any of the proxy details, you can do so by going into the `templates/haproxy.conf` file, modifying the contents and restarting Caldera.
