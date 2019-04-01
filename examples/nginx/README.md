# Nginx Reverse Proxy

Based on [nginx-proxy](https://github.com/jwilder/nginx-proxy), it will be sensitive to exported ports in docker and then nginx will regenerate proxy config and reload it.

This is good for service discovery and make nginx to be more flexible.