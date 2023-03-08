package fr.Alex;

public abstract class Employe {
    protected String nom;
    protected String prenom;
    protected double salaire_net;
    protected double salaire_brut;

    public Employe(String nom, String prenom) {
        this.nom = nom;
        this.prenom = prenom;
    }

    public abstract double get_salaire_net();
    public abstract double get_salaire_brut();

}
