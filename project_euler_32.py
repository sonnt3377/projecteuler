# encoding=utf-8
"""
    Project Euler 32: Pandigital products

    We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
    for example, the 5-digit number, 15234, is 1 through 5 pandigital.

    The product 7254 is unusual, as the identity, 39 × 186 = 7254,
    containing multiplicand, multiplier, and product is 1 through 9 pandigital.

    Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

    HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""
import time

def is_pandigital(multiplicand, multiplier, product):
    """
    Check if three numbers forms a 1 through 9 pandigital

    :param multiplicand:
    :param multiplier:
    :param product:
    :return: True if those three inputs from a 1 through 9 pandigital, False otherwise
    """

    # Position i in this 'list' representing the numbers of digit 'i' in the three numbers above
    # For example, if the multiplicand has one digit 1, while multiplier and product numbers does not have digit 1
    # then list[1] = 1
    list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Break numbers into digits, and update the corresponding position in 'list' with that number
    for i in str(multiplicand):
        list[int(i)] += 1

    for i in str(multiplier):
        list[int(i)] += 1

    for i in str(product):
        list[int(i)] += 1

    is_pandigital = True

    # If there is a digit 0, then it is not pandigital
    if list[0] > 0:
        is_pandigital = False

    # Checking if the three numbers form a 1 through 9 pandigital
    # This means each number from 1 to 9 only appears once
    for i in range(1, len(list)):
        if list[i] != 1:
            is_pandigital = False
            break

    return is_pandigital

def find_list_of_product():
    """
    Find the list of all product values, where their multiplicand/multiplier/ and the values themselves can be
    written as a 1 through 9 pandigital

    :return: List of products

    Ref: http://www.mathblog.dk/project-euler-32-pandigital-products/
    """
    product_list = []

    for multiplicand in range(2, 100):
        # If a multiplicand is a two-digit number, then the other multiplier is a three-digit number
        if multiplicand > 9:
            # Only care about pandigital numbers
            multiplier_start = 123
        else:
            multiplier_start = 1234

        multiplier_end = 10000 // multiplicand + 1

        # Loop through multiplier range
        for multiplier in range(multiplier_start, multiplier_end):
            product = multiplicand * multiplier
            if is_pandigital(multiplicand, multiplier, product):
                print("{0} {1} {2}".format(multiplicand, multiplier, product))
                if product not in product_list:
                    product_list.append(product)

    return product_list

def main():
    start_time = time.time()
    result_list = find_list_of_product()
    result = 0

    for i in result_list:
        result += i

    print("Result is {0} found in {1}".format(result, time.time() - start_time))

if __name__ == "__main__":
    main()