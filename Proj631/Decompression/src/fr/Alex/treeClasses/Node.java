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

    @Override
    public String toString() {
        return "Node{" +
                "label='" + label + '\'' +
                ", frequence=" + frequence +
                ", left_children=" + left_children +
                ", right_children=" + right_children +
                '}';
    }

    public Node(String label, int frequence, Node left_children, Node right_children) {
        this.label = label;
        this.frequence = frequence;
        this.left_children = left_children;
        this.right_children = right_children;
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

    public String getChar(String binaryCode) {
        Node node = this;
        String res = new String();
        if (node.isLeaf()) {
            res =  node.getLabel();
        }
        else if (binaryCode.substring(0, 0).equals("0")) {
            return  this.getChar(binaryCode.substring(1, binaryCode.length()), node.getLeft_children());
        }
        else if (binaryCode.substring(0, 0).equals("1")) {
            return this.getChar(binaryCode.substring(1, binaryCode.length()), node.getRight_children());
        }
        return res;
    }
    public String getChar(String binaryCode, Node node) {
        String res = new String();
        if (node.getLeft_children() == null && node.getRight_children() == null) {
            res = node.getLabel();
        }
        else if (binaryCode.substring(0, 1).equals("0")) {
            return  this.getChar(binaryCode.substring(1, binaryCode.length()), node.getLeft_children());
        }
        else if (binaryCode.substring(0, 1).equals("1")) {
            return this.getChar(binaryCode.substring(1, binaryCode.length()), node.getRight_children());
        }
        return res;
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
