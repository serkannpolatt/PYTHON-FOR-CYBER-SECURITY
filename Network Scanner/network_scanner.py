# Port Scanning Tool
# Description: This code snippet performs port scanning on the specified target IP address or hostname.
# It determines whether ports are open or closed and displays the results.
# Highly customizable and extensible.

# Port Tarama Aracı
# Açıklama: Bu kod parçası, belirtilen hedef IP adresi veya ana makine adına port taraması yapar.
# Portların açık veya kapalı olup olmadığını belirler ve sonuçları görüntüler.
# İleri düzeyde özelleştirilebilir ve genişletilebilir.

import socket
import subprocess
from datetime import datetime

subprocess.call('clear', shell=True)

# Take the target IP address or hostname from the user.
# Kullanıcıdan hedef IP adresini veya ana makine adını alınır.
target = input("Enter the target IP address or hostname: ")

def port_scan(target):
    try:
        ip = socket.gethostbyname(target)

        print("-" * 50)
        print("Scanning target:", ip)
        print("Time started:", datetime.now())
        print("-" * 50)

        for port in range(1, 65635):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Set a timeout for the connection attempt
            result = sock.connect_ex((ip, port))
            if result == 0:
                print("Port {}: Open".format(port))
            sock.close()

    except socket.gaierror:
        print("Hostname could not be resolved.")

    except socket.error:
        print("Could not connect to the server.")

port_scan(target)
