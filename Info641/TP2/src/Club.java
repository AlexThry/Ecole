import java.util.ArrayList;

public class Club {
    private ArrayList<ConcertListener> membres = new ArrayList<>();
    private String nom;

    public Club(String nom) {
        this.nom = nom;
    }

    public void emitEvent(String nom, String date, String salle, int prixPlace, int nbPlaces) {
        ConcertEvent concert = new ConcertEvent(this, nom, date, salle, prixPlace, nbPlaces);
        for (ConcertListener membre : this.membres) {
            membre.nouveauConcert(concert);
        }
    }

    public void addMembre(Membre membre) {
        this.membres.add(membre);
    }

    public String getNom() {
        return nom;
    }

    public void reserverBillet(Membre membre, Concert concert) {
        membre.addBillet(concert);
    }
}
