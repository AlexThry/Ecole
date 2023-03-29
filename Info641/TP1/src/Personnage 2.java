import pouvoirs.Pouvoir;

import java.util.ArrayList;

public class Personnage {
    private String nom;
    private String description;

    private ArrayList<Pouvoir> pouvoirs = new ArrayList<>();
    public Personnage(String _nom, String _description) {
        this.nom = _nom;
        this.description = _description;
    }

    public void addPouvoir(Pouvoir _pouvoir) {
        this.pouvoirs.add(_pouvoir);
    }
    public String getNom() {
        return nom;
    }

    public String getDescription() {
        return description;
    }

    @Override
    public String toString() {
        return "Personnage{" +
                "nom='" + nom + '\'' +
                ", description='" + description + '\'' +
                '}';
    }
}
