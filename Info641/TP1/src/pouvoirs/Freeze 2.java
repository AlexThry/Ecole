package pouvoirs;

public class Freeze extends Pouvoir {
    private double duration;
    private double speedReductionPourcentage;

    public Freeze(String _nom, String _description, double duration, double speedReductionPourcentage) {
        super(_nom, _description);
        this.duration = duration;
        this.speedReductionPourcentage = speedReductionPourcentage;
    }

    public double getDuration() {
        return duration;
    }

    public double getSpeedReductionPourcentage() {
        return speedReductionPourcentage;
    }

    public void setDuration(double duration) {
        this.duration = duration;
    }

    public void setSpeedReductionPourcentage(double speedReductionPourcentage) {
        this.speedReductionPourcentage = speedReductionPourcentage;
    }
}
