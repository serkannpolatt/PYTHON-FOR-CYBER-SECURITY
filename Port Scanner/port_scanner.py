import os

# Install the required package to run the program
os.system("apt-get install figlet")

# Clear the terminal screen and print the header using figlet
os.system("clear")
os.system("figlet PORT SCAN")

# Print a welcome message and the options for the user
print("""
Welcome to Port Scan!
1: Level 1 Scan
2: Level 2 Scan
3: Level 3 Scan
""")

# Ask the user to choose a scan level
islemnumara = input("Which level of scan do you want to perform? ")

# Perform the scan based on the user's choice
if islemnumara == "1":
    hedefip = input("Enter the target IP: ")
    os.system("nmap " + hedefip)
    
elif islemnumara == "2":
    hedefip = input("Enter the target IP: ")
    os.system("nmap -sS -SV " + hedefip)
    
elif islemnumara == "3":
    hedefip = input("Enter the target IP: ")
    os.system("nmap -O " + hedefip)
    
else:
    print("Invalid option. Please choose one of the following: 1, 2, 3")
