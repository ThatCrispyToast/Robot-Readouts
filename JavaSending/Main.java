// Remove "JavaSending" When Shipping to FTC Code
package JavaSending;

import java.io.IOException;
import java.net.UnknownHostException;

public class Main {
    public static void main(String[] args) throws UnknownHostException, IOException {
        Sending client = new Sending();
        // for (int i = 0; i <= 1000; i++) {
        //     System.out.println(i);
        //     client.send(String.valueOf(i));
        // }
        client.send("Hello World!");
    }
}
