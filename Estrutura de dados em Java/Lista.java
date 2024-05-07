import java.util.ArrayList;

public class Lista {
    public static void main(String[] args) {
        ArrayList<String> l = new ArrayList<>();
        l.add("Fla");
        l.add("men");
        l.add("go");
    
        System.out.println("Primeiro elemento da lista: " + l.get(0));
        System.out.println(l.remove(1)+ " removido da lista");
        System.out.println(l.remove(1)+ " removido da lista");

        System.out.println("Quantidade de elementos: " + l.size());
        System.out.println("A lista está vazia: " + l.isEmpty());
    }  
}