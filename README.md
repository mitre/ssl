# CALDERA plugin: SSL

A plugin swapping CALDERA from HTTP to HTTPS.

> This plugin only works if CALDERA is running on a Linux or MacOS machine. It requires HaProxy (>= 1.8) to be installed prior to using it.

When this plugin has been loaded, CALDERA will start the HAProxy service on the machine and then serve CALDERA at hxxps://[YOUR_IP]:8443, instead of the normal hxxp://[YOUR_IP]:8888.

CALDERA will **only** be available at https://[YOUR_IP]:8443 when using this plugin. All deployed agents should use the correct address to connect to CALDERA. 

**Warning:** This plugin uses a default self-signed ssl certificate and key which is insecure.
It is highly recommended that you generate your own before using the plugin to increase the safety of the system.
Find documentation to do so in the full docs below. 

