import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class PrimeNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Podaj liczbę N: ");
        int N = scanner.nextInt();
        scanner.close();
        
        int count = 0;
        int num = 2;
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("primes.txt"))) {
            while (count < N) {
                if (isPrime(num)) {
                    writer.write(num + "\n");
                    count++;
                }
                num++;
            }
        } catch (IOException e) {
            System.err.println("Błąd zapisu do pliku: " + e.getMessage());
        }
    }

    public static boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}
