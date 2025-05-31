import socket

def scan_ports(host, start_port, end_port):
    print(f"Scanning {host} from port {start_port} to {end_port}...")
    open_ports = []
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
    return open_ports

if __name__ == "__main__":
    host = input("Enter target host (e.g., 127.0.0.1): ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))
    open_ports = scan_ports(host, start_port, end_port)
    if open_ports:
        print("Open ports:", open_ports)
    else:
        print("No open ports found.")
