package fr.Alex.typeEmploye;

import fr.Alex.Employe;

public class Consultant extends Employe {
    private String date_premiere_prestation;
    private int nb_heures;
    double cout_horaire;

    public Consultant(String nom, String prenom, String date_premiere_prestation, int nb_heures, double cout_horaire) {
        super(nom, prenom);
        this.date_premiere_prestation = date_premiere_prestation;
        this.nb_heures = nb_heures;
        this.cout_horaire = cout_horaire;
        this.salaire_net = cout_horaire * nb_heures;
        this.salaire_brut = this.salaire_net;
    }
    public void add_heures(int nb_heures) {
        this.nb_heures += nb_heures;
    }

    @Override
    public double get_salaire_net() {
        return this.salaire_net;
    }

    @Override
    public double get_salaire_brut() {
        return this.salaire_brut;
    }
}
