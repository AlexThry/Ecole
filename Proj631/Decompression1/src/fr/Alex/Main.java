package fr.Alex;


import fr.Alex.treeClasses.Tree;
import fr.Alex.treeClasses.TreePanel;

import javax.swing.*;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        Decompression dec = new Decompression("src/fr/Alex/donnees/textesimple_compressed/textesimple_freq.txt", "src/fr/Alex/donnees/textesimple_compressed/textesimple_compressed.bin");
        Tree tree = new Tree("src/fr/Alex/donnees/textesimple_compressed/textesimple_freq.txt");
        TreePanel visu = new TreePanel(tree.getRoot());
        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(visu);
        frame.pack();
        frame.setVisible(true);
        dec.run();
    }
}