public class Ejercicio8 {
    public static void main(String[] args) {
        persona persona = new persona();
        persona.setNombre("Juan Manuel Nuñez de la Cruz");
        System.out.println("Mi nombre es " + persona.getNombre());
        persona.setEdad(17);
        System.out.println("Tengo " + persona.getEdad() + " años");
        persona.setNumero(9211677507L);
        System.out.println("Mi número telefónico es " + persona.getNumero());
    }
}
    class persona {
        private String nombre;
        private int edad;
        private long numero;
        public void setNombre(String nombre) {
            this.nombre = nombre;
        }
        public String getNombre() {
            return this.nombre;
        }
        public void setEdad(int edad){
            this.edad = edad;
        }
        public int getEdad() {
            return this.edad;
        }
        public void setNumero(long numero){
            this.numero = numero;
        }
        public long getNumero() {
            return this.numero;
        }
}
