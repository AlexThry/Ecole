public class JeuDeTest {
    public static void main(String[] args) {
        Club club = new Club("Club des fifous");
        Membre Alex = new Membre("Thierry", "Alexis", 100);
        club.addMembre(Alex);

        club.emitEvent("Paleo", "12/11/2024", "Nyon", 60, 2000);
        club.emitEvent("Paleo1", "12/11/2024", "Nyon", 200, 2000);
    }
}