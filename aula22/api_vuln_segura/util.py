
import ipaddress, socket
from urllib.parse import urlparse

def is_internal_address(url):
    hostname = urlparse(url).hostname
    ip = socket.gethostbyname(hostname)
    ip_obj = ipaddress.ip_address(ip)
    return ip_obj.is_private or ip_obj.is_loopback or ip.startswith("169.254.")
