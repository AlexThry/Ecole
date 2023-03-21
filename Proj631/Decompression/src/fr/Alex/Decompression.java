package fr.Alex;

import fr.Alex.treeClasses.Node;
import fr.Alex.treeClasses.Tree;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;

public class Decompression {
    private String freqFile;
    private Tree tree;
    private File_Agent freqFileAgent;
    private File_Agent compressedFileAgent;
    private String byteCode;
    private Node root;

    public Decompression(String freqFile, String compressedFile) throws IOException {
        this.freqFile = freqFile;
        this.freqFileAgent = new File_Agent(freqFile);
        this.compressedFileAgent = new File_Agent(compressedFile);
        this.byteCode = this.compressedFileAgent.readBinaryFile();
        this.tree = new Tree(freqFile);
        this.root = this.tree.getRoot();
    }

    public void writeFile(String text, String fileName) throws IOException {
        File file = new File(fileName);

        // créer le fichier s'il n'existe pas
        if (!file.exists()) {
            file.createNewFile();
        }

        FileWriter fw = new FileWriter(file.getAbsoluteFile());
        BufferedWriter bw = new BufferedWriter(fw);
        bw.write(text);
        bw.close();
    }
    public void run() throws IOException {
        ArrayList<String> list = new ArrayList<>(Arrays.asList(this.freqFile.split("/")));
        String fileName = list.get(list.size()-1);
        String path = "src/fr/Alex/donnees/" + fileName.substring(0, fileName.length()-8) + "decompressed";
        this.writeFile(this.root.getChars(this.byteCode), path);

    }
}
