import socket

response = "{'Rotation': 0.0000, 'Motors': ('PWR','PWR','PWR','PWR')}"

def recieve():
    global response
    s = socket.socket()
    print("Socket successfully created")

    port = 14892

    s.bind(('', port))
    print("Binded to %s" % (port))

    s.listen(5)
    print("Listening...")

    while True:
        c, addr = s.accept()
        response = c.recv(1024)[:-2].decode()
        # c.send(f'Recieved {response}!'.encode())
        c.close()