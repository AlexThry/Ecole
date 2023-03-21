package pouvoirs;

public abstract class Pouvoir {
    private String nom;
    private String description;

    public Pouvoir(String _nom, String _description) {
        this.nom = _nom;
        this.description = _description;
    }
}
