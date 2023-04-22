import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet GDTA")
print("Welcome to the GDTA (Firewall Detection Tool)")

site = input("Enter Site Address: ")
os.system("wafoof - " + site)
