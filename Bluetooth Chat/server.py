import socket

# Bluetooth socket'i oluşturma
server_socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

# MAC adresi ve kanal 4 ile bağlantı yapma
server_socket.bind(("<your BT adapter MAC address>", 4))

# İstemci bağlantısı beklenmesi
server_socket.listen(1)

# Bağlantı kurulduğunu yazdırma
print("Waiting for connection...")

# İstemciden gelen bağlantıyı kabul etme
client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address}")

# Sonsuz döngüye girme
while True:
    # İstemciden veri alma
    data = client_socket.recv(1024)
    
    # Verinin boş olup olmadığını kontrol etme
    if not data:
        break
    
    # Alınan veriyi ekrana yazdırma
    print(f"Received: {data.decode('utf-8')}")
    
    # Kullanıcıdan mesaj alınması
    message = input("Enter message: ")
    
    # Mesajın gönderilmesi
    client_socket.send(message.encode('utf-8'))

# Bağlantıların kesilmesi
client_socket.close()
server_socket.close()

# Bağlantının kesildiğini yazdırma
print("Disconnected")
