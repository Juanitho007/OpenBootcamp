//Ejercicio 2
class coche{
    public int puertas=4;
    public void Incrementarpuertas() {
        this.puertas++;
    }
}
public class Ejercicio3_2 {
    public static void main(String[] args) {
        coche micoche = new coche();
        micoche.Incrementarpuertas();
        System.out.println(micoche.puertas);
    }
}
