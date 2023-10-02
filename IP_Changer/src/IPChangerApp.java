import java.awt.*;
import java.awt.event.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Timer;
import java.util.TimerTask;

public class IPChangerApp extends Frame {
    private Button startButton;
    private Button stopButton;
    private TextField intervalField;
    private Label ipLabel;
    private boolean changingIP = false;

    public IPChangerApp() {
        super("IP Address Time Changer");
        setLayout(new FlowLayout());

        startButton = new Button("Start");
        startButton.setBackground(Color.GREEN);
        startButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                startChangingIP();
            }
        });

        stopButton = new Button("Stop");
        stopButton.setBackground(Color.RED);
        stopButton.setEnabled(false);
        stopButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                stopChangingIP();
            }
        });

        intervalField = new TextField("30", 5);
        ipLabel = new Label("Current IP Address:");
        ipLabel.setFont(new Font("Arial", Font.BOLD, 20));

        ipLabel.setPreferredSize(new Dimension(450, 30));

        add(startButton);
        add(stopButton);
        add(new Label("Interval (seconds):"));
        add(intervalField);
        add(ipLabel);

        setSize(500, 200);
        setLocationRelativeTo(null);
        setResizable(false);
        setVisible(true);

        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent windowEvent) {
                System.exit(0);
            }
        });

        updateIPAddress();
    }

    private void startChangingIP() {
        if (!changingIP) {
            changingIP = true;
            int interval = Integer.parseInt(intervalField.getText());
            startButton.setEnabled(false);
            stopButton.setEnabled(true);

            Timer timer = new Timer();
            timer.scheduleAtFixedRate(new TimerTask() {
                @Override
                public void run() {
                    changeIP();
                }
            }, 0, interval * 1000);
        }
    }

    private void stopChangingIP() {
        changingIP = false;
        startButton.setEnabled(true);
        stopButton.setEnabled(false);
    }

    private void changeIP() {
        try {
            Process processRelease = Runtime.getRuntime().exec("ipconfig /release");
            processRelease.waitFor();
            Process processRenew = Runtime.getRuntime().exec("ipconfig /renew");
            processRenew.waitFor();
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }

    private void updateIPAddress() {
        try {
            Process process = Runtime.getRuntime().exec("ipconfig /all");
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                if (line.contains("IPv4 Address")) {
                    ipLabel.setText("Current IP Address: " + line.split(":")[1].trim());
                    break;
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        new IPChangerApp();
    }
}
