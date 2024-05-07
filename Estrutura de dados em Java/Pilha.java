import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Stack;

public class Pilha {
    public static void main(String[] args) {
        Stack<String> p = new Stack<>(); // versão original

        // Adicionando elementos na pilha
        p.push("F");
        p.push("L");
        p.push("A");

        System.out.println("Topo da pilha: " + p.peek());

        // Removendo elementos da pilha
        p.pop();

        System.out.println("Topo da pilha: " + p.peek());

        System.out.println("Tamanho da pilha: " + p.size());

        System.out.println("A pilha está vazia: " + p.empty());

        System.out.println("Posição da letra 'F' na pilha");
        System.out.println("Posição: " + p.search("F"));

        Deque<Integer> stack = new ArrayDeque<>(); // a partir de Java 6

        // Adicionando elementos na pilha
        stack.addFirst(7);
        stack.addFirst(3);
        stack.addFirst(9);

        System.out.println("Topo da pilha: " + stack.getFirst());

        // Removendo elementos da pilha
        stack.removeFirst();

        System.out.println("Topo da pilha: " + stack.getFirst());



        
        
    }
}
