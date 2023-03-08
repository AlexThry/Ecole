package fr.Alex.typeEmploye;

import fr.Alex.Employe;

public class Titulaire extends Employe {
    private String date_embauche;
    private final double taux_cotisation = 0.2;



    public Titulaire(String nom, String prenom, double salaire_net, String date_embauche) {
        super(nom, prenom);
        this.date_embauche = date_embauche;
        this.salaire_brut = this.salaire_net/(1-this.taux_cotisation);
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
