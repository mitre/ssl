# CALDERA plugin: Proxy

This plugin contains logic to run a reverse proxy in front of the CALDERA application.

The Proxy plugin provides TLS/SSL termination and reverse proxying service for the Sandcat agents/web services. The 
proxying service will ensure that 54ndc47 agents render correctly to the reverse proxy external IP and port.

## Requirements

HAProxy must be installed on the same host CALDERA is running on.