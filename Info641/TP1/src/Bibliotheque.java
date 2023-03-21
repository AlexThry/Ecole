import java.util.ArrayList;

public class Bibliotheque {
    private ArrayList<Livre> livres = new ArrayList<>();

    public Bibliotheque() {}

    public Bibliotheque(ArrayList<Livre> _livres) {
        this.livres = _livres;
    }

    public void ajoutLivre(Livre _livre) {
        this.livres.add(_livre);
    }

    public boolean contient(String _titre) {
        for (int i = 0 ; i < this.livres.size() ; i++) {
            if (livres.get(i).getTitre() == _titre) {
                return true;
            }
        }
        return false;
    }

    public ArrayList<Livre> ecritsPar(String _auteur) {
        ArrayList<Livre> ecritsPar = new ArrayList<>();
        for (int i = 0 ; i < this.livres.size() ; i++) {
            if (this.livres.get(i).getAuteur() == _auteur) {
                ecritsPar.add(this.livres.get(i));
            }
        }
        return ecritsPar;
    }

    public ArrayList<Livre> getLivres() {
        return livres;
    }

    public void setLivres(ArrayList<Livre> livres) {
        this.livres = livres;
    }

    @Override
    public String toString() {
        return "Bibliotheque{" +
                "livres=" + livres +
                '}';
    }
}
