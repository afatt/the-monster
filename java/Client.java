// Java UDP client
// Example run: java Client 127.0.0.1 33001
//

import java.io.*;
import java.net.*;
import java.util.Scanner;

public class Client {
 
    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Syntax: client <hostname> <port>");
            return;
        }

        String hostname = args[0];
        int port = Integer.parseInt(args[1]);

        try {
            InetAddress address = InetAddress.getByName(hostname);
            DatagramSocket socket = new DatagramSocket();
            Scanner scanner = new Scanner(System.in);

            while (true) {

                System.out.print("Type Something (q or Q to quit): ");
                String data = scanner.nextLine();
                if (data.equals("q") || data.equals("Q")) {
                    break;
                }
                byte[] senddata = data.getBytes();

                DatagramPacket packet = new DatagramPacket(senddata, senddata.length, address, port);
                socket.send(packet);
 
                // byte[] buffer = new byte[1024];
                // DatagramPacket response = new DatagramPacket(buffer, buffer.length);
                // socket.receive(response);

                // String quote = new String(buffer, 0, response.getLength());

                // System.out.println(quote);
                // System.out.println();

                Thread.sleep(1000);
            }

        } catch (SocketTimeoutException ex) {
            System.out.println("Timeout error: " + ex.getMessage());
            ex.printStackTrace();
        } catch (IOException ex) {
            System.out.println("Client error: " + ex.getMessage());
            ex.printStackTrace();
        } catch (InterruptedException ex) {
            ex.printStackTrace();
        }
    }
}