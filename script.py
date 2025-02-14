def read_primes(filename):
    with open(filename, 'r') as file:
        primes = [int(line.strip()) for line in file]
    return primes

def calculate_sum_and_average(primes):
    total_sum = sum(primes)
    average = total_sum / len(primes) if primes else 0
    return total_sum, average

def main():
    primes = read_primes('primes.txt')
    total_sum, average = calculate_sum_and_average(primes)
    print(f"Suma: {total_sum}")
    print(f"Średnia: {average}")

if __name__ == "__main__":
    main()
