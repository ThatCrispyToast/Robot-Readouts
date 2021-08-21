// Remove "JavaSending" When Shipping to FTC Code
package DataSendingEmulation;

import java.io.IOException;
import java.net.UnknownHostException;

public class Main {
    public static void main(String[] args) throws UnknownHostException, IOException, InterruptedException {
        Sending client = new Sending();

        double rotation = 0.0000;
        double motortl = 1.0;
        double motortr = -1.0;
        double motorbl = 1.0;
        double motorbr = -1.0;
        String status = "Running Test 1...";

        for (int i = -182; i < 182; i = i + 2) {
            Thread.sleep(50);
            rotation = i;
            client.send(rotation, motortl, motortr, motorbl, motorbr, status);
        }

        motortl = -1.0;
        motortr = 1.0;
        motorbl = -1.0;
        motorbr = 1.0;
        status = "Running Test 2...";

        for (int i = 180; i > -1; i--) {
            Thread.sleep(50);
            rotation = i;
            client.send(rotation, motortl, motortr, motorbl, motorbr, status);
        }

        status = "Running Test 3...";

        for (int i = 0; i < 5; i++) {
            Thread.sleep(500);
            rotation = Math.random() * 360;
            motortl = Math.random();
            motortr = Math.random();
            motorbl = Math.random();
            motorbr = Math.random();
            client.send(rotation, motortl, motortr, motorbl, motorbr, status);
        }

        rotation = 0.0000;
        motortl = 0.0;
        motortr = 0.0;
        motorbl = 0.0;
        motorbr = 0.0;
        status = "Tests Complete!";

        client.send(rotation, motortl, motortr, motorbl, motorbr, status);

        System.out.println("Tests Complete!");

        // client.send("Hello World!");
    }
}
