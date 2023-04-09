import java.util.ArrayList;

public class Membre implements ConcertListener {
    private String nom;
    private String prenom;
    private int seuilPrix;
    private ArrayList<Billet> billets = new ArrayList<>();

    public Membre(String nom, String prenom, int seuilPrix) {
        this.nom = nom;
        this.prenom = prenom;
        this.seuilPrix = seuilPrix;
    }

    @Override
    public void nouveauConcert(ConcertEvent event) {
        System.out.println("Membre : " + this.prenom + " " + this.nom);
        Club club = (Club) event.getSource();
        System.out.println("Club : " + club.getNom());
        if (event.getConcert().getPrixPlace() > this.seuilPrix) {
            System.out.println("Trop Cher !");
        } else {
            System.out.println("Je peux y aller !");
        }
    }

    public void addBillet(Concert concert) {
        this.billets.add(new Billet(concert));
    }
}
