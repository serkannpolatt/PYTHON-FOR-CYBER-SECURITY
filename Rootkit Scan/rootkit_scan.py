import os

# Install figlet
os.system("apt-get install figlet")

# Clear the terminal screen and display a banner
os.system("clear")
os.system("figlet ROOTKIT SCAN TOOL")

# Display a welcome message
print("Welcome to the Rootkit Scan Tool!")

# Run the chkrootkit command
os.system("chkrootkit")
