// Remove "JavaSending" When Shipping to FTC Code
package JavaSending;

import java.io.IOException;
import java.net.UnknownHostException;

public class Main {
    public static void main(String[] args) throws UnknownHostException, IOException, InterruptedException {
        Sending client = new Sending();

        double rotation;
        double motortl = 1.0;
        double motortr = -1.0;
        double motorbl = 1.0;
        double motorbr = -1.0;

        for (int i = -182; i < 182; i = i + 2) {
            Thread.sleep(50);
            rotation = i;
            client.send(String.format("{'Rotation': %.4f, 'Motors': (%.1f,%.1f,%.1f,%.1f)}", rotation, motortl, motortr, motorbl, motorbr));
        }

        motortl = -1.0;
        motortr = 1.0;
        motorbl = -1.0;
        motorbr = 1.0;

        for (int i = 180; i > 0; i--) {
            Thread.sleep(50);
            rotation = i;
            client.send(String.format("{'Rotation': %.4f, 'Motors': (%.1f,%.1f,%.1f,%.1f)}", rotation, motortl, motortr, motorbl, motorbr));
        }

        for (int i = 0; i < 50; i++) {
            Thread.sleep(50);
            rotation = Math.random() * 360;
            motortl = Math.random();
            motortr = Math.random();
            motorbl = Math.random();
            motorbr = Math.random();
            client.send(String.format("{'Rotation': %.4f, 'Motors': (%.1f,%.1f,%.1f,%.1f)}", rotation, motortl, motortr, motorbl, motorbr));
        }
        
        System.out.println("Tests Complete!");
        // client.send("Hello World!");
    }
}
