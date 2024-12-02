import socket
from tqdm import tqdm

def scan_ports(host, port_range):
    open_ports = []
    for port in tqdm(port_range, desc="Scanning ports"):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

if __name__ == "__main__":
    target_host = input("Enter the host to scan: ")
    if target_host.startswith("http://"):
        target_host = target_host[7:]
    elif target_host.startswith("https://"):
        target_host = target_host[8:]
    
    # Remove trailing slash if present
    if target_host.endswith("/"):
        target_host = target_host[:-1]
    
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    
    print(f"Scanning {target_host} from port {start_port} to {end_port}...")
    open_ports = scan_ports(target_host, range(start_port, end_port + 1))
    
    if open_ports:
        print(f"Open ports: {open_ports}")
    else:
        print("No open ports found.")