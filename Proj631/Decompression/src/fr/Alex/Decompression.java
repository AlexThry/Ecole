package fr.Alex;

import fr.Alex.treeClasses.Tree;
import fr.Alex.treeClasses.Node;

import java.io.IOException;

public class Decompression {
    private Tree tree;
    private File_Agent fileAgent;
    private Node root;
    private String byteCode;

    public Decompression(String freqFile) throws IOException {
        this.fileAgent = new File_Agent(freqFile);
        this.tree = new Tree(freqFile);
        this.root = this.tree.getRoot();
        this.byteCode = fileAgent.read();
    }

    public void decompress() {

    }
}
