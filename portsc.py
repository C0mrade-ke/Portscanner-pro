import socket
import sys
import time
from datetime import datetime

def typing_print(text, speed=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

BANNER = """
██████   ██████  ██████  ████████ 
██   ██ ██    ██ ██   ██    ██    
██████  ██    ██ ██████     ██    
██      ██    ██ ██   ██    ██    
██       ██████  ██   ██    ██    
                                  
███████  ██████  █████  ███    ██ ███    ██ ███████ ██████  
██      ██      ██   ██ ████   ██ ████   ██ ██      ██   ██ 
███████ ██      ███████ ██ ██  ██ ██ ██  ██ █████   ██████  
     ██ ██      ██   ██ ██  ██ ██ ██  ██ ██ ██      ██   ██ 
███████  ██████ ██   ██ ██   ████ ██   ████ ███████ ██   ██ 
                                                            
██████  ██████   ██████  
██   ██ ██   ██ ██    ██ 
██████  ██████  ██    ██ 
██      ██   ██ ██    ██ 
██      ██   ██  ██████  
"""

vulnerable_ports = {
    21: "FTP",
    22: "SSH", 
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    111: "RPC",
    135: "MSRPC",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    993: "IMAPS",
    995: "POP3S",
    1433: "MSSQL",
    1723: "PPTP",
    1812: "RADIUS",
    1900: "UPnP",
    2121: "CCProxy",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    8080: "HTTP-Proxy",
    8443: "HTTPS-Alt"
}

print(BANNER)
typing_print(">>> WELCOME TO PORTSCANNER PRO!!..", 0.08)
typing_print(">>> ßყ   𝓬0𝓶ɾαԃҽ", 0.05)

keep_scanning = True

while keep_scanning:
    try:
        target = input("\n𝗘𝗻𝘁𝗲𝗿 𝗜𝗣 𝗼𝗿 𝗗𝗼𝗺𝗮𝗶𝗻:")
        target_ip = socket.gethostbyname(target)
        
        print(f"\nScanning {target} ({target_ip})...")
        print(f"Start Time: {datetime.now().strftime('%H:%M:%S')}\n")
        
        for port, service in vulnerable_ports.items():
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.3)
            result = s.connect_ex((target_ip, port))
            
            if result == 0:
                print(f"[!] PORT {port} IS OPEN: {service}")
            
            s.close()
            
    except socket.gaierror:
        print("\n[x] Error: Invalid Hostname or IP.")

    choice = input("\nDo you want to scan another target? (y/n): ").lower()
    if choice != 'y':
        keep_scanning = False

typing_print("\n𝗚𝗢𝗢𝗗𝗢𝗕𝗬𝗘 𝗙𝗥𝗜𝗘𝗡𝗗 𝗛𝗔𝗣𝗣𝗬 𝗛𝗔𝗖𝗞𝗜𝗡𝗚! ", 0.05)
