import socket
from datetime import *
from firebase import firebase
import time

firebase = firebase.FirebaseApplication("https://realtime-d9dca-default-rtdb.firebaseio.com/",None)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '192.168.67.134'
port = 4488
s.bind((host, port))
s.listen(5)
clientSocket, address = s.accept()

while True:
    print(f"Connection {address} established!")
    datarec = clientSocket.recv(1024)
    da = datarec.decode()
    now = datetime.now()
    currentTime = now.strftime(" %d %b, %Y %H:%M:%S")
    date = {
        'info' : da,
        'time' : currentTime
    }
    result = firebase.post('/History', date)
    print(result)
