package pouvoirs;


public class Shock extends Pouvoir {
    private double duration;
    private double radius;
    private double damagePerSecond;

    public Shock(String _nom, String _description, double duration, double radius, double damagePerSecond) {
        super(_nom, _description);
        this.duration = duration;
        this.radius = radius;
        this.damagePerSecond = damagePerSecond;
    }

    public double getDuration() {
        return duration;
    }

    public double getRadius() {
        return radius;
    }

    public double getDamagePerSecond() {
        return damagePerSecond;
    }

    public void setDuration(double duration) {
        this.duration = duration;
    }

    public void setRadius(double radius) {
        this.radius = radius;
    }

    public void setDamagePerSecond(double damagePerSecond) {
        this.damagePerSecond = damagePerSecond;
    }
}
