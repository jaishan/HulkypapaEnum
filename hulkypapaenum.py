import socket
import sys
from termcolor import colored

def banner():
    """
    Display the tool banner.
    """
    banner_text = "HULKYPAPA ENUM"
    print(colored(banner_text, "red", attrs=["bold", "italic"]))

def scan(target):
    """
    Perform a basic port scan on the target.
    """
    try:
        for port in range(1, 1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is open")
            sock.close()
    except KeyboardInterrupt:
        print("\nExiting due to user interruption.")
        sys.exit(0)
    except socket.gaierror:
        print("Hostname could not be resolved. Exiting.")
        sys.exit(1)
    except socket.error:
        print("Could not connect to the server. Exiting.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python HULKYPAPA-ENUM.py <target>")
        sys.exit(1)

    target_ip = sys.argv[1]
    banner()
    scan(target_ip)
