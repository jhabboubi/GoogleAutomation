
#!/usr/bin/env python3


import requests
import socket

def check_localhost():

 localhost = socket.gethostbyname('localhost')
 if localhost == '127.0.0.1':
  return True
 else:
  return False


#print(check_localhost())

def check_connectivity():
 request = requests.get("http://www.google.com")

