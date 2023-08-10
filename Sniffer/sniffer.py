import socket
from scapy.all import *

# Create a socket: Listen to low-level network packets using AF_PACKET, SOCK_RAW, and ntohs(3).
# Socket oluşturuluyor: AF_PACKET, SOCK_RAW ve ntohs(3) kullanılarak düşük seviyeli ağ paketleri dinleniyor.
sniffer_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

# Define the interface to listen on (e.g., "eth0").
# Dinlenen ağ arayüzü belirleniyor (örneğin, "eth0").
interface = "eth0"

# Bind the sniffer socket to the specified interface.
# Sniffer soketi belirtilen arayüze bağlanıyor.

sniffer_socket.bind((interface, 0))

try:
    while True:
        # Receive data and source address up to 65535 bytes.
        # 65535 bayta kadar veri ve kaynak adres alınıyor.
        raw_data, addr = sniffer_socket.recvfrom(65535)

        # Process the captured raw data as a packet.
        # Yakalanan ham veri paket olarak işleniyor.

        packet = Ether(raw_data)

        # Print the summary of the packet.
        # Paket özetini (summary) yazdırarak ekrana basılıyor.

        print(packet.summary())

except KeyboardInterrupt:
    # Close the socket when Ctrl+C is pressed.
    # Klavyeden Ctrl+C kombinasyonuyla çıkıldığında soket kapatılıyor.

    sniffer_socket.close()
