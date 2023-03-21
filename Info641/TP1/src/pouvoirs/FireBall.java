package pouvoirs;

public class FireBall extends Pouvoir {
    private double damage;
    private double ignitionChances;

    public FireBall(String _nom, String _description, double damage, double ignitionChances) {
        super(_nom, _description);
        this.damage = damage;
        this.ignitionChances = ignitionChances;
    }

    public double getDamage() {
        return damage;
    }

    public double getIgnitionChances() {
        return ignitionChances;
    }

    public void setDamage(double damage) {
        this.damage = damage;
    }

    public void setIgnitionChances(double ignitionChances) {
        this.ignitionChances = ignitionChances;
    }
}
