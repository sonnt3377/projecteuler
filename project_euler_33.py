"""
    Project Euler 33: Digit cancelling fractions

    The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
    incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

    We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

    There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing
    two digits in the numerator and denominator.

    If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""
import time

def order_number(number1, number2):
    """
    Order two numbers so that the larger number appears first

    :return: two number in descending order
    """
    if number2 > number1:
        return number2, number1
    else:
        return number1, number2

def gcd(number1, number2):
    """
    Finding the greatest common divisor of the two numbers using Euclid algorithm

    :return: the gcd of the two numbers
    """
    # For simplicity, we assume both numbers >= 0
    large_number, small_number = order_number(number1, number2)

    if small_number == 0:
        return large_number
    else:
        return gcd(small_number, large_number % small_number)

def do_work():
    """
    Analysis:
        Let's call n the nominator, and d the denominator of a fraction after cancelling. We have 0 < n < d <= 9
        Let's call a is the cancelled digit. 'a' can be the larger or smaller digits or either the nominator or
        denominator.
        The original fraction before cancelling therefore can be one of these:
        1. (10*a + n)/(10*a + d) = n/d
        2. (10*n + a)/(10*d + a) = n/d
        3. (10*a + n)/(10*d + a) = n/d
        4. (10*n + a)/(10*a + d) = n/d

        Case 1: it means 10ad + nd = 10an + nd <=> n = d. This is not the case since n < d
        Case 2: it means 10nd + ad = 10dn + an <=> n = d. This is not the case
        Case 3: it means 10ad + nd = 10dn + an <=> 9d(n - a) = a(d - n). Because d > n => n > a.
            The equation is also express as n - a = (ad - an)/(9d) = a/9 - an(9d).
            Since a < n < d <= 9, this equation does not hold.
        Case 4: it means (10n + a)d = (10a + d)n <=> 9nd = 10an - ad <=> 9n(d - a) = a(n - d).
            Since n < d, it means d < a for the equation to hold

        We will then search for case 4 with condition 1 <= n < d < a <= 9
    """
    nominator_product = 1
    denominator_product = 1

    for a in range(1, 10):
        for d in range(1, a):
            for n in range(1, d):
                # If condition in case 4 holds
                if (10*n + a)/(10*a + d) == n/d:
                    print("The fraction is: {0}/{1} = {2}/{3}".format(10*n + a, 10*a + d, n, d))
                    nominator_product *= n
                    denominator_product *= d

    return denominator_product / gcd(nominator_product, denominator_product)

def main():
    start_time = time.time()
    result = do_work()
    print("Result is {0} found in {1}".format(result, time.time() - start_time))

if __name__ == "__main__":
    main()