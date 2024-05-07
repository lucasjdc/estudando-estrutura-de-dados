public class Matriz {
    public static void main(String[] args) {
        int[][] m = new int[5][5];
        int[][] m1 = new int[][] {{1,2},{3,4}};
        int[][] m2 = {{5,6},{7,8}};
        int[][][] m3 = new int[][][] {{{1,2},{3,4}},{{5,6},{7,8}}};
        int[][][] m4 = {{{9,10},{11,12}},{{13,14},{15,16}}};

        m[0][0] = 65;
        m[3][2] = 17;

        int iM = m[0][0];
        int tamanho = m.length;
        System.err.println("Tamanho da matriz: " + tamanho);

        tamanho = m[0].length + m[1].length + m[2].length + m[3].length + m[4].length;
        System.err.println("Tamanho da matriz: " + tamanho);
    }
}