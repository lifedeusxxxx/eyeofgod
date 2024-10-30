import subprocess

def scan_web_server(ip_address):
    result = subprocess.run(['nikto', '-h', ip_address], capture_output=True, text=True)
    return {"scan_output": result.stdout}
