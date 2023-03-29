public class Toutou {
    private String nom;
    private int nbPuces;
    public Toutou(String _nom, int _nbPuces) throws IllegalArgumentException {
        if ((_nom == null) || (_nom.length() == 0)) {
            throw new IllegalArgumentException("Un toutou doit avoir un nom.");
        }
        if (_nbPuces < 0) {
            throw new IllegalArgumentException("Le nombre de puces ne peut être négatif.");
        }
        this.nom = _nom;
        this.nbPuces = _nbPuces;
    }

    public String getNom() {
        return nom;
    }

    public int getNbPuces() {
        return nbPuces;
    }
}
