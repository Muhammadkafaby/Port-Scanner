import socket
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
import re

def is_valid_host(host):
    # Simple regex to validate host
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
        r'localhost|' # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, host) is not None

def scan_port(host, port, open_ports, timeout):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    result = sock.connect_ex((host, port))
    if result == 0:
        open_ports.append(port)
    sock.close()

def scan_ports(host, port_range, max_threads=100, timeout=1):
    open_ports = []
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(scan_port, host, port, open_ports, timeout) for port in port_range]
        for future in tqdm(futures, desc="Scanning ports"):
            future.result()  # Wait for each future to complete
    return open_ports

if __name__ == "__main__":
    target_host = input("Enter the host to scan: ")
    if not is_valid_host(target_host):
        print("Invalid host. Please enter a valid host.")
        exit(1)
    
    if target_host.startswith("http://"):
        target_host = target_host[7:]
    elif target_host.startswith("https://"):
        target_host = target_host[8:]
    
    # Remove trailing slash if present
    if target_host.endswith("/"):
        target_host = target_host[:-1]
    
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    max_threads = int(input("Enter the number of threads (default 100): ") or 100)
    timeout = float(input("Enter the timeout in seconds (default 1): ") or 1)
    
    print(f"Scanning {target_host} from port {start_port} to {end_port} with {max_threads} threads and {timeout} seconds timeout...")
    open_ports = scan_ports(target_host, range(start_port, end_port + 1), max_threads, timeout)
    
    if open_ports:
        print(f"Open ports: {open_ports}")
    else:
        print("No open ports found.")