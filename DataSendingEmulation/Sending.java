// Remove "JavaSending" When Shipping to FTC Code
package DataSendingEmulation;

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

    public void send(double rotation, double motortl, double motortr, double motorbl, double motorbr, String status) throws UnknownHostException, IOException {
        Sending client = new Sending();
        client.startConnection("AniketsPC", 14892);
        String response = client.sendMessage(String.format(
        "{'Rotation': %.4f, 'Motors': (%.1f,%.1f,%.1f,%.1f), 'Status': '%s'}",
        rotation, motortl, motortr, motorbl, motorbr, status));
        // System.out.println(response);
        client.stopConnection();
    }

    // public static void main(String[] args) throws UnknownHostException, IOException {
    //     // for (int i = 0; i < 10000; i++) {
    //     //     send(String.valueOf(i));
    //     // }
    //     // send("-----------------");
    //     send("Hello!");
    // }
}