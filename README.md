# Robot Readouts

> **Victorious warriors win first and then go to war, while defeated warriors go to war first and then seek to win.** - Sun Tzu on The Art of War

Objective: Easily and Effectively Obtain Information from the Robot for Debugging and Planning.

[GitHub - ThatCrispyToast/Robot-Readouts](https://github.com/ThatCrispyToast/Robot-Readouts)

# TODO

- [x]  [Establish Inter-Device Communation](#sockets)
    - [x]  Sending Class
    - [x]  Recieving Script
    - [x]  Sub Decisecond Communcation
- [ ]  Send Appropriate Data from Robot to Client
- [ ]  Develop Client-Side Readout of Recieved Data
    - [x]  (Pre-Build) Emulate Recieved Data
    - [x]  Parse Recieved Data
    - [ ]  Interpret Data Visually
        - [x]  Movement Data
        - [ ]  Manipulator Data
        - [ ]  IMU and Sensor Data
            - [x]  Rotation
            - [ ]  Sensors
- [ ]  Send Data Back to Robot for Debugging
    - [ ]  Remote Control

## Sockets

After a lot of thinking and experimentation, I landed on using sockets as the communiation between the robot and the client.

> Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket(node) listens on a particular port at an IP, while the other socket reaches out to the other to form a connection. The server forms the listener socket while the client reaches out to the server. - [GeeksforGeeks](https://www.geeksforgeeks.org/socket-programming-python/)

Using a java sending class in the robot's codebase and a python receiving script on the client's device, I can (theoretically) communicate between the robot and the readout device. The primary advantage of this system is that it only uses default modules, removing the need to import external libraries.

*The code samples below are the sending and recieving ends of the socket communication system.*

```java
import java.net.*;
import java.io.*;

public class Sending {
    private Socket clientSocket;
    private PrintWriter out;
    private BufferedReader in;

    public void startConnection(String ip, int port) throws UnknownHostException, IOException {
        clientSocket = new Socket(ip, port);
        out = new PrintWriter(clientSocket.getOutputStream(), true);
        in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
    }

    public String sendMessage(String msg) throws IOException {
        out.println(msg);
        String resp = in.readLine();
        return resp;
    }

    public void stopConnection() throws IOException {
        in.close();
        out.close();
        clientSocket.close();
    }

    public void send(String msg) throws UnknownHostException, IOException {
        Sending client = new Sending();
        client.startConnection("AniketsPC", 14892);
        String response = client.sendMessage(msg);
        // System.out.println(response);
        client.stopConnection();
    }
}
```

```python
import socket

response = ''

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
```

Socket communication relies the usage of a port to listen for and send data to. In this case, I opted to use our team number (14892) as the port, as it is a generally unused port in other networking systems, won't interfere with other processes, and is easy to remember. The commented out portions of both files are for backwards communcation.

Using the java client is as easy as intantiating the `Sending` class and calling the `send()` method.

```java
import java.io.IOException;
import java.net.UnknownHostException;

public class Main {
    public static void main(String[] args) throws UnknownHostException, IOException {
        Sending client = new Sending();
        client.send("Hello!");
    }
}
```

The python server, on the other hand, is a little more complicated to handle. The `s.accept()` function is blocking, meaning it stops any code in it's thread from executing while it waits for a client to connect to it. I worked around this limitation by simply making the `response` variable global. This allows me to access the module's response variable in a different thread while the `recieve()` function runs.

```python
import threading
import recieving
import time

def recieve():
    recieving.recieve()
  
def main():
    while True:
        time.sleep(0.01)
        print(recieving.response)
  
if __name__ == "__main__":
    t1 = threading.Thread(target=recieve)
    t2 = threading.Thread(target=main)
		t1.daemon = True
  
    t1.start()
    t2.start()
  
    t1.join()
```