package fr.Alex.treeClasses;

import fr.Alex.File_Agent;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;

public class Tree {
    private Node root;
    private ArrayList<Node> leaves;
    private File_Agent file;
    private String file_path;
    public Tree(String file_path) throws IOException {
        this.file_path = file_path;
        this.create_leaves();
        this.create_root(this.leaves);
    }

    public void create_leaves() throws IOException {
        File_Agent file_agent = new File_Agent(this.file_path);
        HashMap map = file_agent.to_hash_map();
        ArrayList<Node> leaves = new ArrayList<>();
        for (Object key : map.keySet()) {
            Node node = new Node((String) key, (Integer) map.get(key.toString()));
            leaves.add(node);
        }
        this.leaves = leaves;
    }

    public ArrayList<Node> get_two_smallest() {
        ArrayList<Node> leaves = this.leaves;
        Node t1 = leaves.get(0);
        Node t2 = leaves.get(1);
        if (t1.getFrequence() > t2.getFrequence()) {
            t1 = leaves.get(1);
            t2 = leaves.get(0);
        }
        for (Node node: leaves.subList(2, leaves.size())) {
            if (node.getFrequence() < t1.getFrequence()) {
                t2 = t1;
                t1 = node;
            }
            else if (node.getFrequence() < t2.getFrequence()) {
                t2 = node;
            }
        }
        ArrayList<Node> nodes = new ArrayList<>();
        nodes.add(t1);
        nodes.add(t2);
        return nodes;
    }

    public ArrayList<Node> get_leaves() {
        return leaves;
    }

    public void create_root(ArrayList<Node> leaves) {
        if (leaves.size() == 1) {
            this.root = leaves.get(0);
        }
        else {
            ArrayList<Node> two_smallest = this.get_two_smallest();
            Node t1 = two_smallest.get(0);
            Node t2 = two_smallest.get(1);
            String label = String.valueOf(t1.getFrequence() + t2.getFrequence());
            Integer frequence = t1.getFrequence() + t2.getFrequence();
            Node t = new Node(label, frequence, t1, t2);
            leaves.add(t);
            leaves.remove(t1);
            leaves.remove(t2);
            this.create_root(leaves);
        }
    }

    public Node getRoot() {
        return root;
    }

    public ArrayList<Node> getLeaves() {
        return leaves;
    }

    public File_Agent getFile() {
        return file;
    }

    public String getFile_path() {
        return file_path;
    }
}
