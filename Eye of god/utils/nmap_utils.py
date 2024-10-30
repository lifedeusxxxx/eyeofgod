import nmap

def scan_ip(ip_address):
    nm = nmap.PortScanner()
    nm.scan(ip_address, arguments='-sV')
    scan_data = {host: nm[host].all_protocols() for host in nm.all_hosts()}
    return scan_data
