import java.util.Scanner;  // Import the Scanner class

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // Create a Scanner object
        System.out.print("Podaj imię: "); // Display prompt
        String i = scanner.nextLine(); // Read user input
        System.out.println(i); // Print the input
        scanner.close(); // Close the scanner
    }
}
