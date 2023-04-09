import javax.swing.*;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

public class Window extends JFrame {
    // statiques :
    private JLabel nomForm = new JLabel("Nom :");
    private JLabel nomSelect = new JLabel("Nom :");
    private JLabel nbPucesForm = new JLabel("NbPuces : ");
    private JLabel nbPucesSelect = new JLabel("NbPuces : ");

    // pas statiques


    private JFrame window;
    private JTextField nameField = new JTextField("Nom Toutou");
    SpinnerNumberModel model = new SpinnerNumberModel(0, 0, Integer.MAX_VALUE, 1);

    private JSpinner nbPucesField = new JSpinner(model);
    private JButton validate = new JButton("Valider");
    private DefaultListModel<Toutou> listModelToutous = new DefaultListModel<>();
    private DefaultListModel<String> listModelNomsToutous = new DefaultListModel<>();
    private JList<String> toutous = new JList<>(listModelNomsToutous);
    private JLabel nomLabel = new JLabel();
    private JLabel nbPucesLabel = new JLabel();
    private JScrollPane scrollPane = new JScrollPane();


    private ArrayList<String> listeToutous = new ArrayList<>();



    public Window(String _name) {
        this.window = new JFrame();
        this.window.setName(_name);
        this.initialize();
        this.setVisible();
    }

    public void setVisible() {
        this.window.setVisible(true);
    }

    private void initialize() {
        this.window.setResizable(false);
        this.window.setLayout(null);
        this.window.setSize(730, 130);

        this.nomForm.setBounds(10, 10, 80, 20);
        this.window.add(nomForm);

        this.nbPucesForm.setBounds(10, 40, 80, 20);
        this.window.add(nbPucesForm);

        this.nameField.setBounds(100, 10, 160, 20);
        this.window.add(nameField);

        this.nbPucesField.setBounds(100, 40, 160, 20);
        this.window.add(nbPucesField);

        this.validate.setBounds(10, 70, 250, 20);
        this.window.add(validate);


        //270, 10
        //this.toutous.setBounds(270, 10, 250, 80);
        this.scrollPane.setViewportView(toutous);
        this.scrollPane.setBounds(270, 10, 250, 80);
        this.window.add(scrollPane);


        this.nomSelect.setBounds(530, 10, 80, 20);
        this.window.add(nomSelect);

        this.nomLabel.setBounds(620, 10, 100, 20);
        this.window.add(nomLabel);

        this.nbPucesSelect.setBounds(530, 40, 100, 20);
        this.window.add(nbPucesSelect);

        this.nbPucesLabel.setBounds(620, 40, 100, 20);
        this.window.add(nbPucesLabel);


        this.validate.addActionListener(e -> {
            String nom = this.nameField.getText();
            int nbPuces = (Integer) this.nbPucesField.getValue();
            Toutou toutou = new Toutou(nom, nbPuces);
            this.listModelToutous.add(listModelToutous.getSize(), toutou);
            this.listModelNomsToutous.add(listModelNomsToutous.getSize(), nom);
            System.out.println(toutou.getNom());
            System.out.println(toutou.getNbPuces());
        });
        this.toutous.addListSelectionListener(new ListSelectionListener() {
            @Override
            public void valueChanged(ListSelectionEvent e) {
                if (!e.getValueIsAdjusting()) {
                    int selectedIndex = toutous.getSelectedIndex();
                    nbPucesLabel.setText(String.valueOf(listModelToutous.get(selectedIndex).getNbPuces()));
                    nomLabel.setText(String.valueOf(listModelToutous.get(selectedIndex).getNom()));
                }
            }
        });
    }
}
