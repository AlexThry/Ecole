public class Concert {

    private String nom;
    private String date;
    private String salle;
    private int prixPlace;
    private int nbPlaces;

    public Concert(String nom, String date, String salle, int prixPlace, int nbPlaces) {
        this.nom = nom;
        this.date = date;
        this.salle = salle;
        this.prixPlace = prixPlace;
        this.nbPlaces = nbPlaces;
    }

    public void removePlace() {
        this.nbPlaces -= 1;
    }

    public String getNom() {
        return nom;
    }

    public String getDate() {
        return date;
    }

    public String getSalle() {
        return salle;
    }

    public int getPrixPlace() {
        return prixPlace;
    }

    public int getNbPlaces() {
        return nbPlaces;
    }
}
