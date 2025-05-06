import nmap
import sys

def nmap_scan(target, port_range="1-1000", scan_type="-sS"):
    """
    Perform an Nmap scan on the target host.
    
    :param target: IP address or hostname to scan
    :param port_range: Port range to scan (default: 1-1000)
    :param scan_type: Nmap scan type (default: -sS for TCP SYN scan)
    """
    try:
        # Initialize Nmap PortScanner
        nm = nmap.PortScanner()
        
        # Perform the scan
        print(f"Scanning {target} on ports {port_range} with {scan_type} scan...")
        nm.scan(target, port_range, arguments=scan_type)
        
        # Check if the host is up
        if target not in nm.all_hosts():
            print(f"Host {target} is not responding.")
            return
        
        # Print scan results
        for proto in nm[target].all_protocols():
            print(f"\nProtocol: {proto}")
            ports = nm[target][proto].keys()
            for port in sorted(ports):
                state = nm[target][proto][port]['state']
                service = nm[target][proto][port]['name']
                print(f"Port: {port}\tState: {state}\tService: {service}")
                
    except nmap.PortScannerError as e:
        print(f"Nmap error: {e}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    # Check for command-line arguments or set defaults
    if len(sys.argv) < 2:
        target = input("Enter target IP or hostname (e.g., 192.168.1.1): ")
    else:
        target = sys.argv[1]
        
    port_range = input("Enter port range (e.g., 1-1000) or press Enter for default (1-1000): ") or "1-1000"
    scan_type = input("Enter scan type (e.g., -sS for TCP SYN, -sU for UDP) or press Enter for default (-sS): ") or "-sS"
    
    # Run the scan
    nmap_scan(target, port_range, scan_type)

if __name__ == "__main__":
    main()