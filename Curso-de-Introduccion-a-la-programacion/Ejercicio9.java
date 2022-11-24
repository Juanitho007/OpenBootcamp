public class Ejercicio9 {
    public static void main(String[] args) {
        Persona persona = new Persona();
        Cliente cliente = new Cliente();
        Trabajador trabajador = new Trabajador();
        persona.nombre = "Juan Manuel Nuñez de la Cruz";
        persona.edad = 25;
        persona.telefono = 9211677507L;
        System.out.println("Mi nombre es " + persona.nombre + " ,y tengo " + persona.edad +
                " años, me puedes contactar por Whatsapp, al: " + persona.telefono);

        cliente.nombre = "Sandra Vanessa Gallegos";
        cliente.edad = 24;
        cliente.telefono = 9211778662L;
        cliente.credito = 5000;
        System.out.println("Mi nombre es " + cliente.nombre + " ,y tengo " + cliente.edad +
                " años, me puedes contactar por Whatsapp, al: " + cliente.telefono + " mi credito disponible es de $" + cliente.credito);

        trabajador.nombre = "Juan Nuñez Gallegos";
        trabajador.edad = 4;
        trabajador.telefono = 100000000000L;
        trabajador.salario = 5;
        System.out.println("Mi nombre es " + trabajador.nombre + " ,y tengo " + trabajador.edad +
                " años, me puedes contactar por Whatsapp, al: " + trabajador.telefono + " gano $" + trabajador.salario);


    }
}
class Persona {
   int edad;
   String nombre;
   long telefono;
}

class Cliente extends Persona {
    double credito;
}

 class Trabajador extends Persona{
    double salario;
}
