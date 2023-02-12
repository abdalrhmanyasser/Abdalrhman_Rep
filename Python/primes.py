import threading

def find_primes(min_value, max_value, thread_count):
    # Create a list of booleans, with True representing a prime number
    is_prime = [True] * (max_value + 1)

    # Set 0 and 1 to not be prime
    is_prime[0] = False
    is_prime[1] = False

    # Divide the work among the specified number of threads
    step = (max_value - min_value) // thread_count
    threads = []
    for i in range(thread_count):
        start = min_value + i * step
        end = min_value + (i + 1) * step - 1
        if i == thread_count - 1:
            # Make sure the last thread processes all remaining values
            end = max_value
        thread = threading.Thread(target=sieve, args=(is_prime, start, end))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Return a list of all prime numbers within the specified range
    return [i for i in range(min_value, max_value + 1) if is_prime[i]]

def sieve(is_prime, start, end):
    # Mark all non-prime numbers within the specified range
    for i in range(2, end + 1):
        if is_prime[i]:
            for j in range(start, end + 1, i):
                is_prime[j] = False

# Find all prime numbers between 10 and 20 using 2 threads
print(find_primes(10, 1000000, 4))
