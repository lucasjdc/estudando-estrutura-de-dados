import java.util.LinkedList;

public class Fila {
    public static void main(String[] args) {
        LinkedList<Integer> f = new LinkedList<>();
        f.add(2);
        f.add(6);
        f.add(8);

        System.out.println("Primeiro da fila: " + f.peek());

        // Para retirar o primeiro elemento da fila
        System.out.println("Atendendo o cliente: " + f.poll());

        System.out.println("Primeiro da fila: " + f.peek());
        System.out.println("Quantidade de elementos na fila: " + f.size());
        System.out.println("A fila está vazia?");
        System.out.println("Resposta: " + f.isEmpty());

        // Fila de prioridades o Java tem a classe PriorityQueue
        // Filas com dois finais, a classe ArrayDeque
    }    
}