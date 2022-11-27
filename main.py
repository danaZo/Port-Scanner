# Script that scans ports of chosen host to find which port is open.

import socket
import sys


try:
    target_name = input('Enter target hostname: ')
    target_ip = socket.gethostbyname(target_name)

except socket.gaierror:
    print("\n Hostname Could Not Be Resolved\n")
    sys.exit()


try:
    for port in range(1, 65535):
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = soc.connect_ex((target_ip, port))
        if result == 0:
            protocol = socket.getservbyport(port)
            print("Port {} / {} is open".format(port, protocol))
        soc.close()

except KeyboardInterrupt:
    print("\n Exiting Program\n")
    sys.exit()
except socket.error:
    print("\n Server not responding\n")
    sys.exit()