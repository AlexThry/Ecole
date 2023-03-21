package fr.Alex;


import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        Decompression dec = new Decompression("src/fr/Alex/donnees/alice_compressed/alice_freq.txt", "src/fr/Alex/donnees/alice_compressed/alice_compressed.bin");
        dec.run();
    }
}