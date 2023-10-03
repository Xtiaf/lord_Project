import java.net.*;
import java.io.*;
import java.util.Scanner;

public class The_Script {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Nmap Java Tool (v.1)");
        System.out.println("by Lord s");
        System.out.println("____________________");
        System.out.println("[1] Scan Manual");
        System.out.println("[2] Local Host, Your Internet");
        System.out.println("[00] Exit");

        System.out.print("Enter your choice: ");
        int choice = scanner.nextInt();

        if (choice == 1) {
            System.out.print("Enter the IP address to scan: ");
            String host = scanner.next();
            scanPorts(host);
        } else if (choice == 2) {
            // Localhost and your internet scanning
            scanPorts("localhost");
            scanPorts("your_internet_ip_here");
        } else if (choice == 00) {
            System.out.println("Exiting the program.");
        } else {
            System.out.println("Invalid choice. Exiting the program.");
        }

        System.out.println("Done.");
    }

    private static void scanPorts(String host) {
        int startPort = 1;
        int endPort = 65535;
        boolean scanned = false;

        System.out.println("Scanning ports on " + host + "...");
        for (int port = startPort; port <= endPort; port++) {
            try {
                Socket socket = new Socket();
                socket.connect(new InetSocketAddress(host, port), 1000); // 1000ms timeout
                socket.close();
                System.out.println("Port " + port + " is open");
                scanned = true;
            } catch (IOException e) {
                // Port is closed or filtered
            }
        }

        if (!scanned) {
            System.out.println("No open ports found.");
        }
    }
}
