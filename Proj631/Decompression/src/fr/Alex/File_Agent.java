package fr.Alex;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.io.*;


public class File_Agent {
    private String file_path;
    public File_Agent(String file_path) {
        this.file_path = file_path;
    }
    public String read() throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(this.file_path));
        StringBuilder sb = new StringBuilder();
        String line;
        while ((line = reader.readLine()) != null) {
            sb.append(line);
            sb.append(System.lineSeparator());
        }
        reader.close();
        return sb.toString();

    }

    public ArrayList<String> split_frequence() throws IOException {
        ArrayList<String> characters = new ArrayList<>();
        for (String str : this.read().split("\n")) {
            characters.add(str);
        }
        characters.remove(0);
        return characters;
    }

    public HashMap to_hash_map() throws IOException {
        HashMap<String, Integer> map = new HashMap<>();
        for (String element: this.split_frequence()) {
            if (element.equals("")) {}
            else if ((String.valueOf(element.charAt(0)).equals(" ")) && (String.valueOf(element.charAt(1)).equals(" "))) {
                map.put(" ", Integer.parseInt(element.substring(2, element.length() - 1)));
            }
            else if ((String.valueOf(element.charAt(0)).equals(" ")) && !(String.valueOf(element.charAt(1)).equals(" "))) {
                map.put("\n", Integer.parseInt(element.substring(1, element.length() - 1)));
            }
            else {
                map.put(String.valueOf(element.charAt(0)), Integer.parseInt(element.substring(2, element.length() - 1)));
            }
        }
        return map;
    }

    public String binaryToString() {
        File file = new File(this.file_path);
        StringBuilder sb = new StringBuilder();
        try {
            FileInputStream fileInputStream = new FileInputStream(file);
            int data;
            while ((data = fileInputStream.read()) != -1) {
                sb.append((char) data);
            }
            fileInputStream.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        String binaryString = sb.toString();
        return binaryString;

    }
}
