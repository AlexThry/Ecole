package fr.Alex.treeClasses;

public class Node {
    private String label;
    private int frequence;
    private Node left_children;
    private Node right_children;

    public Node(String label, int frequence) {
        this.label = label;
        this.frequence = frequence;
        this.left_children = null;
        this.right_children = null;
    }

    public Node(String label, int frequence, Node left_children, Node right_children) {
        this.label = label;
        this.frequence = frequence;
        this.left_children = left_children;
        this.right_children = right_children;
    }

    @Override
    public String toString() {
        return "Node{" +
                "label='" + label + '\'' +
                ", frequence=" + frequence +
                ", left_children=" + left_children +
                ", right_children=" + right_children +
                '}';
    }

    public boolean isLeaf() {
        Boolean res;
        if (this.getLeft_children() == null && this.getRight_children() == null) {
            res = true;
        }
        else {
            res = false;
        }
        return res;
    }

    public String getChars(String code) {
        Node node = this; // commence à la racine
        String label = null;
        for (int i = 0; i < code.length(); i++) {
            char c = code.charAt(i);
            if (c == '0') {
                node = node.left_children;
            } else if (c == '1') {
                node = node.right_children;
            } else {
                throw new IllegalArgumentException("Code binaire invalide : " + code);
            }
            if (node == null) {
                throw new IllegalArgumentException("Code binaire invalide : " + code);
            }
            if (node.left_children == null && node.right_children == null) {
                // on a atteint une feuille
                if (label == null) {
                    label = node.label;
                } else {
                    label += node.label;
                }
                node = this; // recommence à la racine
            }
        }
        if (label == null) {
            throw new IllegalArgumentException("Code binaire invalide : " + code);
        }
        return label;
    }


    public String getLabel() {
        return label;
    }

    public int getFrequence() {
        return frequence;
    }

    public Node getLeft_children() {
        return left_children;
    }

    public Node getRight_children() {
        return right_children;
    }
}
