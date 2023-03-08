package fr.Alex;

import java.util.ArrayList;

public class Entreprise {
    private ArrayList<Employe> employes;

    public Entreprise() {
    }
    public Entreprise(ArrayList<Employe> employes) {
        this.employes = employes;
    }

    public Entreprise(Employe employe) {
        this.employes.add(employe);
    }

    public void add_employe(Employe employe) {
        this.employes.add(employe);
    }
    public double calcul_salaire_net(){
        double total_net = 0;
        for (Employe employe : this.employes) {
            total_net += employe.get_salaire_net();
        }
        return total_net;
    }

    public double calcul_salaire_brut() {
        double total_brut = 0;
        for (Employe employe : this.employes) {
            total_brut += employe.get_salaire_brut();
        }
        return total_brut;
    }

    public ArrayList<Employe> getEmployes() {
        return employes;
    }
}