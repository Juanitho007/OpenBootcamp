public class Ejercicio4_5 {
    public static void main(String[] args){
        var estacion = "Otoño";
                switch(estacion){
            case "Primavera":
                System.out.println("Estamos en Primavera");
            break;
            case "Verano":
                System.out.println("Estamos en Verano");
            break;
            case "Otoño":
                System.out.println("Estamos en Otoño");
            break;
            case "Invierno":
                System.out.println("Estamos en Invierno");
            break;
            default:
                System.out.println("Lo variable ingresada no es una estación del año");
        }
    }
}
