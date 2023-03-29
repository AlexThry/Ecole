import java.util.ArrayList;

public class Livre {
    private String titre;
    private String auteur;
    private int anneePremiereParution;
    private ArrayList<Personnage> personnages = new ArrayList<>();


    public Livre(String _titre, String _auteur, int _anneePremiereParution) {
        this.titre = _titre;
        this.auteur = _auteur;
        this.anneePremiereParution = _anneePremiereParution;
    }

    public Livre(String _titre, String _auteur, int _anneePremiereParution, ArrayList<Personnage> _personnages) {
        this.titre = _titre;
        this.auteur = _auteur;
        this.anneePremiereParution = _anneePremiereParution;
        this.personnages = _personnages;
    }

    public void affichePersonnages() {
        System.out.println(this.personnages);
    }

    public void ajoutPersonnage(Personnage _personnage) {
        this.personnages.add(_personnage);
    }

    public boolean contientPersonnage(String _nomPersonnage) {
        for (int i = 0 ; i < this.personnages.size() ; i++) {
            if (this.personnages.get(i).getNom() == _nomPersonnage) {
                return true;
            }
        }
        return false;
    }

    @Override
    public String toString() {
        return "Livre{" +
                "titre='" + titre + '\'' +
                ", auteur='" + auteur + '\'' +
                ", anneePremiereParution=" + anneePremiereParution +
                ", personnages=" + personnages +
                '}';
    }

    public String getTitre() {
        return titre;
    }

    public String getAuteur() {
        return auteur;
    }

    public int getAnneePremiereParution() {
        return anneePremiereParution;
    }

    public ArrayList<Personnage> getPersonnages() {
        return personnages;
    }
}
