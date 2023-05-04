import socket

# Bağlanılacak cihazın MAC adresi
server_mac_address = "<MAC address of the PC you are connecting to>"

# Bluetooth socket'i oluşturma
client_socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

# Cihaza bağlanma
client_socket.connect((server_mac_address, 4))

# Bağlantı kurulduğunu yazdırma
print("Connected to server!")

# Sonsuz döngüye girme
while True:
    # Kullanıcıdan mesaj alınması
    message = input("Enter message: ")
    
    # Mesajın gönderilmesi
    client_socket.send(message.encode('utf-8'))
    
    # Sunucudan veri alma
    data = client_socket.recv(1024)
    
    # Verinin boş olup olmadığını kontrol etme
    if not data:
        break
    
    # Alınan veriyi ekrana yazdırma
    print(f"Received: {data.decode('utf-8')}")

# Bağlantı kesilmesi
client_socket.close()

# Bağlantının kesildiğini yazdırma
print("Disconnected from server!")
