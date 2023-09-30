package from_a;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.List;

public class AnalysisCSV_v_1 {
    public static void main(String[] args) {
        JFrame frame = new JFrame("AnalysisCSV (version 1.0 )");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);

        JPanel panel = new JPanel();
        panel.setLayout(new BorderLayout());

        // تعيين اللون الأسود للعنوان
        JLabel titleLabel = new JLabel("AnalysisCSV");
        titleLabel.setHorizontalAlignment(JLabel.CENTER);
        titleLabel.setForeground(Color.WHITE); // تعيين لون النص إلى الأبيض
        titleLabel.setOpaque(true); // تفعيل خلفية عنوان
        titleLabel.setBackground(Color.BLACK); // تعيين لون الخلفية إلى الأسود
        titleLabel.setPreferredSize(new Dimension(frame.getWidth(), 40)); // تعيين ارتفاع العنوان
        panel.add(titleLabel, BorderLayout.NORTH);

        JTextArea textArea = new JTextArea();
        textArea.setEditable(false);
        textArea.setFont(new Font("Arial", Font.PLAIN, 20)); // تعيين حجم الخط للنص
        textArea.setWrapStyleWord(true); // التمرير الأفقي
        textArea.setLineWrap(true); // التمرير الأفقي
        JScrollPane scrollPane = new JScrollPane(textArea);
        panel.add(scrollPane, BorderLayout.CENTER);

        JButton csvButton = new JButton("CSV");
        JButton antibioticButton = new JButton("Antibiotic");
        JButton infoButton = new JButton("Info");

        csvButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                textArea.setText("معلومات حول CSV");
            }
        });

        antibioticButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                textArea.setText("معلومات حول Antibiotic");
            }
        });

        infoButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                textArea.setText("معلومات عامة");
            }
        });

        JPanel buttonPanel = new JPanel();
        buttonPanel.setLayout(new FlowLayout());
        buttonPanel.add(csvButton);
        buttonPanel.add(antibioticButton);
        buttonPanel.add(infoButton);

        panel.add(buttonPanel, BorderLayout.SOUTH);

        // إعداد قائمة السنوات
        List<String> years = new ArrayList<>();
        for (int i = 2014; i <= 2023; i++) {
            years.add(Integer.toString(i));
        }
        JList<String> yearList = new JList<>(years.toArray(new String[0]));

        // إعداد زر "Select"
        JButton selectButton = new JButton("Select");
        selectButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // احصل على السنة المحددة
                String selectedYear = yearList.getSelectedValue();
                if (selectedYear != null) {
                    textArea.setText("السنة المحددة: " + selectedYear);
                } else {
                    textArea.setText("لم يتم تحديد سنة.");
                }
            }
        });

        // إعداد لوحة جانبية تحتوي على القائمة وزر "Select"
        JPanel sidePanel = new JPanel();
        sidePanel.setLayout(new BorderLayout());
        sidePanel.add(new JScrollPane(yearList), BorderLayout.CENTER);
        sidePanel.add(selectButton, BorderLayout.SOUTH);
        sidePanel.setPreferredSize(new Dimension(100, frame.getHeight())); // تعيين العرض الجانبي

        panel.add(sidePanel, BorderLayout.WEST);

        frame.add(panel);
        frame.setVisible(true);
    }
}
