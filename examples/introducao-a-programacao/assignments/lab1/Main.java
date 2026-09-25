import java.util.*;
public class Main {
    static String[] nomes;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] notas = new int[n];
        for (int i = 0; i <= n; i++) { notas[i] = sc.nextInt(); nomes[i] = sc.nextLine(); }
        int best = 0;
        for (int i = 0; i < n; i++) if (notas[i] > notas[best]) best = i;
        if (nomes[best] == "") System.out.println("sem nome");
        System.out.println(nomes[best]);
    }
}
