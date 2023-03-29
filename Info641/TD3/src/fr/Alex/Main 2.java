package fr.Alex;

import fr.Alex.typeEmploye.Consultant;
import fr.Alex.typeEmploye.Titulaire;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");
        Entreprise entreprise = new Entreprise();
        Titulaire alexis_thierry = new Titulaire("Thierry", "Alexis", 2700, "17 mars 2021");
        Consultant pierre_thierry = new Consultant("Thierry", "Pierre", "20 aout 2020", 20, 12.3);
        entreprise.add_employe(alexis_thierry);
    }
}