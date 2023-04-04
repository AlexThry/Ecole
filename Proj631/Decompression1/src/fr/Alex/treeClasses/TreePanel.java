package fr.Alex.treeClasses;

import javax.swing.*;
import java.awt.*;


public class TreePanel extends JPanel {

    private Node root;
    private int radius = 2;

    public TreePanel(Node root) {
        this.root = root;
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        if (root != null) {
            int width = getWidth();
            int height = getHeight();
            drawNode(g, root, width / 2, 50, width / 4, height / 10);
        }
    }

    private void drawNode(Graphics g, Node node, int x, int y, int dx, int dy) {
        g.drawOval(x - radius, y - radius, 2 * radius, 2 * radius);
        g.drawString(node.getLabel(), x - radius / 2, y + radius / 2);
        if (node.getLeft_children() != null) {
            int x2 = x - dx;
            int y2 = y + dy;
            g.drawLine(x, y + radius, x2, y2 - radius);
            drawNode(g, node.getLeft_children(), x2, y2, dx / 2, dy);
        }
        if (node.getRight_children() != null) {
            int x2 = x + dx;
            int y2 = y + dy;
            g.drawLine(x, y + radius, x2, y2 - radius);
            drawNode(g, node.getRight_children(), x2, y2, dx / 2, dy);
        }
    }

}
