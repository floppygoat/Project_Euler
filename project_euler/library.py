from math import sqrt, log
from functools import reduce


def gcd(a, b):
    """
    This algorithm uses Euclid's algorithm with modulation to determine gcd(a,b)
    :type a: int
    :type b: int
    :return: the greatest common denominator of a and b
    :rtype: int
    """
    a, b = abs(a), abs(b)
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    if a == 0:
        return b
    return a


def lcm(a, b):
    """
    :type a: int
    :type b: int
    :return: the least common multiple of a and b
    :rtype int
    """
    try:
        return abs(a * b) // gcd(a, b)
    except ZeroDivisionError:
        return 0


def is_palindrome(number):
    """
    :type number: int
    :return: True if num is a palindrome in base 10, False otherwise
    :rtype: bool
    """
    palindrome = 0
    temp = number

    # Reverse the num
    while temp > 0:
        palindrome = (palindrome * 10) + (temp % 10)
        temp //= 10
    return number == palindrome


def list_primes(limit):
    """
    Uses the Sieve of Eratosthenes with only odd numbers to find all primes less than limit
    :type limit: int
    :return: prime numbers less than limit (and greater than one)
    :rtype: list
    """
    if limit < 2:
        return []

    # To account for the num 2
    primes = [2]

    # A sieve that only contains odd numbers (the only even prime num is 2).
    # Sieve indices i correspond to the num (i * 2) + 1
    sieve = [True] * (limit // 2)

    # 1 is not a prime num
    sieve[0] = False

    # Make the sieve and find all primes less than sqrt(limit)
    # Only less than or equal sqrt(limit) contribute to the sieve
    for i in range((int(sqrt(limit)) // 2) + 1):
        if sieve[i]:
            primes.append((i * 2) + 1)
            for j in range((i * 3) + 1, limit // 2, (i * 2) + 1):
                sieve[j] = False

    # Find all remaining prime numbers in the sieve that are greater than sqrt(limit)
    # and less than limit
    for i in range((int(sqrt(limit)) // 2) + 1, len(sieve)):
        if sieve[i]:
            primes.append((i * 2) + 1)

    return primes


def list_n_primes(n):
    """
    Uses the Sieve of Eratosthenes with only odd numbers to find all primes less than limit
    :type n: int
    :return: prime numbers less than limit (and greater than one)
    :rtype: list
    """
    if n < 6:
        primes = {
            1: [2],
            2: [2, 3],
            3: [2, 3, 5],
            4: [2, 3, 5, 7],
            5: [2, 3, 5, 7, 11]
        }
        return primes[n]

    # The upper bound for the nth prime number is n * (log(n) + log(log(n))))
    limit = int(n * (log(n) + log(log(n)))) + 1
    count = 1

    # To account for the num 2
    primes = [2]

    # A sieve that only contains odd numbers (the only even prime num is 2).
    # Sieve indices i correspond to the num (i * 2) + 1
    sieve = [True] * (limit // 2)

    # 1 is not a prime num
    sieve[0] = False

    # Make the sieve and find all primes less than sqrt(limit)
    # Only less than or equal sqrt(limit) contribute to the sieve
    for i in range((int(sqrt(limit)) // 2) + 1):
        if sieve[i]:
            primes.append((i * 2) + 1)
            count += 1
            for j in range((i * 3) + 1, limit // 2, (i * 2) + 1):
                sieve[j] = False

    # Find all remaining prime numbers in the sieve that are greater than sqrt(limit)
    # and less than limit
    for i in range((int(sqrt(limit)) // 2) + 1, len(sieve)):
        if sieve[i]:
            primes.append((i * 2) + 1)
            count += 1
            if count == n:
                return primes

    return primes


def number_of_divisors(num, primes=None):
    """
    :type num: int
    :param primes: list of primes with at least all positive prime numbers less than (num // 2 + 1)
    :type primes: list
    :return: the num of divisors num has, including itself and 1
    :rtype: int
    """
    if primes is None:
        primes = list_primes((num // 2) + 2)
    itr = iter(primes)
    divisor_count = 1
    while num > 1:
        next_prime = itr.__next__()
        if num < next_prime * next_prime:
            return divisor_count * 2
        count = 0
        while num % next_prime == 0:
            count += 1
            num //= next_prime
        if count != 0:
            divisor_count *= count + 1
    return divisor_count


def is_prime(num, primes=None):
    return 2 == number_of_divisors(num, primes)


def n_choose_k(n, k):
    """
    Use the multiplicative formula to compute the binomial coefficient of (n, k)^{T}
    :type n: int
    :type k: int
    :return: n_choose_k
    :rtype: int
    """
    return reduce(lambda i, j: i * j, range(n - k + 1, n + 1)) // reduce(lambda i, j: i * j, range(1, k + 1))


def file_to_matrix(filename, separator):
    f = open(filename, "r")
    strings = f.readlines()
    f.close()
    array = []
    for x in range(0, len(strings)):
        array.append(list(map(int, strings[x].split(separator))))
    return array


def digit_factorial(number):
    digit_fact = [1, 1, 2, 6, 24, 120, 720, 5_040, 40_320, 362_880]
    answer = 0
    while number > 0:
        digit, number = number % 10, number // 10
        answer += digit_fact[digit]
    return answer
