# Here we import two modules, socket and time
 
import socket
import time
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# here we asking for the target website
# or host
target = input('What you want to scan?: ')
 
# next line gives us the ip address
# of the target
target_ip = socket.gethostbyname(target)
print('Starting scan on host:', target_ip)
def port_scan(port):
     try:
        s.connect((target_ip, port))
        return True
     except:
        return False
start = time.time()
#Enter the port you want to scan for
#it will check if the conditions are true
port =int(input("Enter port to scan:"))
if port_scan(port):
     print(f'port {port} is open')
else:
      print(f'port {port} is closed')
 
end = time.time()
print(f'Time taken {end-start:.2f} seconds')
