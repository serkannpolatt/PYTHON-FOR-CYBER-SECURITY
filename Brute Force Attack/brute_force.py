import os

# Install figlet and clear the terminal
os.system("apt-get install figlet")
os.system("clear")
# Print the title with figlet
os.system("figlet KKSA")

# Print the options
print("""
1: FTP
2: SSH
""")
# Get the input for the chosen option and the target IP
islemno = input("Islem Numarasi: ")
hedefip = input("Hedef IP: ")
# Get the input for the username and password file
kady = input("Kullanici Adi Dosya Yolu: ")
sifre = input("Sifre: ")

if islemno == "1":
    # Run ncrack with FTP option
    os.system("ncrack -P21 -u " + kady + " -P " + sifre + " " + hedefip)
elif islemno == "2":
    # Run ncrack with SSH option
    os.system("ncrack -P22 -u " + kady + " -P " + sifre + " " + hedefip)
else:
    # Print an error message for invalid option
    print("Boyle bir islem numarasi yok.")
