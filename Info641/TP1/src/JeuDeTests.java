public class JeuDeTests {
    public static void main(String[] arg) {
        // Création des objets
        Personnage alex = new Personnage("Alex", "Un garcon");
        Livre lotr = new Livre("Le Seigneur Des Anneaux", "Tolkien", 1954);
        Bibliotheque bibliotheque = new Bibliotheque();


        // Tests méthodes Personnage
        System.out.println();
        System.out.println("########################################################################");
        System.out.println("Méthodes personnage :");
        System.out.println(alex);


        // Tests méthodes Livre
        System.out.println();
        System.out.println("########################################################################");
        System.out.println("Méthodes Livres");
        lotr.ajoutPersonnage(alex);
        lotr.affichePersonnages();
        System.out.println(lotr.contientPersonnage("Alex"));
        System.out.println(lotr.getAnneePremiereParution());
        System.out.println(lotr);


        // Tests méthodes Bibliothèque
        System.out.println();
        System.out.println("########################################################################");
        System.out.println("Méthodes Bibliothèque");
        bibliotheque.ajoutLivre(lotr);
        System.out.println(bibliotheque);
        System.out.println(bibliotheque.contient("Le Seigneur Des Anneaux"));
        System.out.println(bibliotheque.ecritsPar("Tolkien"));
        System.out.println(bibliotheque.ecritsPar("Alex"));


        //


    }
}
