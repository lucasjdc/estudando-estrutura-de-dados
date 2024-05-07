public class Vetor {
    public static void main(String[] args) {
        int[] v = new int[5];
        int[] v1 = {10,25};
        int[] v2 = new int[] {1,2,3};
        v[0] = 70;
        v[3] = 45;

        int iV = v[0];
        int tamanho = v.length;
        System.out.println("Tamanho do vetor: " + tamanho);
    }
}