import java.util.ArrayList;
import java.util.EventObject;

public class ConcertEvent extends EventObject {
    private Concert concert;

    public ConcertEvent(Club source, String nom, String date, String salle, int prixPlace, int nbPlaces) {
        super(source);
        this.concert = new Concert(nom, date, salle, prixPlace, nbPlaces);
    }

    public Concert getConcert() {
        return concert;
    }
}
