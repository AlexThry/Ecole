package fr.Alex;


import fr.Alex.treeClasses.Tree;

import java.io.IOException;
public class Main {
    public static void main(String[] args) throws IOException {
        Tree tree = new Tree("src/fr/Alex/donnees/alice_freq.txt");
//        System.out.println(tree.getRoot());
//        System.out.println(tree.getRoot().getChar("010110", tree.getRoot()));
        File_Agent fileAgent = new File_Agent("src/fr/Alex/donnees/alice_compressed.bin");
        System.out.println(fileAgent.binaryToString());




// Affichage de l'arbre

//        JFrame frame = new JFrame("Tree Example");
//        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Ajouter le panneau de l'arbre à la fenêtre
//        TreePanel treePanel = new TreePanel(tree.getRoot());
//        frame.add(treePanel);
//
//        // Afficher la fenêtre
//        frame.setSize(3000, 2000);
//        frame.setVisible(true);
    }
}