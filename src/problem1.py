"""
PRACTICE Exam 1, problem 1.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Valerie Galluzzi, Mark Hays, Amanda Stouder, Aaron Wilkin,
         their colleagues, and Zachary Juday.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

###############################################################################
# Students:
#
# These problems have DIFFICULTY and TIME ratings:
#  DIFFICULTY rating:  1 to 10, where:
#     1 is very easy
#     3 is an "easy" Test 1 question.
#     5 is a "typical" Test 1 question.
#     7 is a "hard" Test 1 question.
#    10 is an EXTREMELY hard problem (too hard for a Test 1 question)
#
#  TIME ratings: A ROUGH estimate of the number of minutes that we
#     would expect a well-prepared student to take on the problem.
#
#  IMPORTANT: For ALL the problems in this module,
#    if you reach the time estimate and are NOT close to a solution,
#    STOP working on that problem and ASK YOUR INSTRUCTOR FOR HELP
#    on it, in class or via Piazza.
###############################################################################

import testing_helper
import time
import math

def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem1a()
    run_test_problem1b()
    run_test_problem1c()


###############################################################################
# DONE: 2.  READ the green doc-string for the:
#   - is_prime
#   - sum_of_digits
# functions defined below.  You do NOT need to understand their
# implementations, just their specification (per the doc-string).
# You should  ** CALL **  those functions as needed in implementing the
# other functions.  After you have READ this, change its _TODO_ to DONE.
###############################################################################

def is_prime(n):
    """
    What comes in:  An integer n >= 2.
    What goes out:
      -- Returns True if the given integer is prime,
         else returns False.
    Side effects:   None.
    Examples:
      -- is_prime(11) returns  True
      -- is_prime(12) returns  False
      -- is_prime(2)  returns  True
    Note: The algorithm used here is simple and clear but slow.
    """
    for k in range(2, (n // 2) + 1):
        if n % k == 0:
            return False

    return True

    # -------------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  is_prime  function - it has no _TODO_.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # -------------------------------------------------------------------------


def sum_of_digits(number):
    """
    What comes in:  An integer.
    What goes out:  Returns the sum of the digits in the given integer.
    Side effects:   None.
    Example:
      If the integer is 83135,
      this function returns (8 + 3 + 1 + 3 + 5), which is 20.
    """
    # -------------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  sum_of_digits function - it has no _TODO_.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # -------------------------------------------------------------------------
    if number < 0:
        number = -number

    digit_sum = 0
    while True:
        if number == 0:
            break
        digit_sum = digit_sum + (number % 10)
        number = number // 10

    return digit_sum


def run_test_problem1a():
    """ Tests the   problem1a   function. """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement this TEST function.
    #   It TESTS the  problem1a  function defined below.
    #   Include at least **   4   ** tests (we wrote two for you).
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      3
    #    TIME ESTIMATE:   10 minutes.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1a   function:')
    print('--------------------------------------------------')

    format_string = '    problem1a( {}, {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = -1.601  # This is APPROXIMATELY the correct answer.
    print_expected_result_of_test([3, 5], expected, test_results,
                                  format_string)
    actual = problem1a(3, 5)
    print_actual_result_of_test(expected, actual, test_results, precision=3)

    # Test 2:
    expected = 1.278  # This is APPROXIMATELY the correct answer.
    print_expected_result_of_test([30, 100], expected, test_results,
                                  format_string)
    actual = problem1a(30, 100)
    print_actual_result_of_test(expected, actual, test_results, precision=3)

    print_summary_of_test_results(test_results)

    # -------------------------------------------------------------------------
    # TO DO: 2 (continued).
    # Below this comment, add 2 more test cases of your own choosing.
    # You do NOT need to use the above form.  Instead, use the usual:
    #   expected = XXX
    #   actual = problem1a(YYY, YYY)
    #   print('Test 1 expected:', expected)
    #   print('       actual:  ', actual)
    # -------------------------------------------------------------------------

    # Test 3
    expected = -2.046244
    actual = problem1a(4,9)
    print('Test 3 expected:',expected)
    print('        actual:', actual)

    # Test 4
    expected = -1.653648
    actual = problem1a(3,9)
    print('Test 4 expected:',expected)
    print('       actual:',actual)


def problem1a(m, n):
    """
    What comes in:  Integers m and n with abs(m) <= abs(n).
    What goes out:
      -- Returns the sum of the sines of the integers
         from m squared to n squared, inclusive,
         where m and n are the given arguments.
    Side effects:   None.
    Examples:
      -- If m is 3 and n is 5, this function returns:
            sine(9) + sine(10) + sine(11) +  ...  + sine(24) + sine(25),
         which is about -1.601.
      -- If m is 1 and n is -2, this function returns:
            sine(1) + sine(2) + sine(3) + sine(4),
         which is about 1.135.
      -- If m is 30 and n is 100, the correct answer is about 1.278.
    """
    # -------------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      5
    #    TIME ESTIMATE:   10 minutes.
    # -------------------------------------------------------------------------
    a = m**2
    b=n**2
    sum = 0
    for k in range(a,b+1):
        sum = sum + math.sin(k)
    return sum
def run_test_problem1b():
    """ Tests the   problem1b   function. """
    # -------------------------------------------------------------------------
    # DONE: 5. Implement this TEST function.
    #   It TESTS the  problem1b  function defined below.
    #   Include at least **   4   ** tests.  Use the usual form:
    #
    #   expected = XXX
    #   actual = problem1b(YYY, YYY)
    #   print('Test 1 expected:', expected)
    #   print('       actual:  ', actual)
    # -------------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      3
    #    TIME ESTIMATE:   15 minutes.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1b   function:')
    print('--------------------------------------------------')

    # Test 1
    expected = 5
    actual = problem1b(3,5)
    print('Test 1 expected:',expected)
    print('       actual:  ',actual)

    # Test 2
    expected = 15
    actual = problem1b(7, 9)
    print('Test 2 expected:', expected)
    print('       actual:  ', actual)

    # Test 3
    expected = 1
    actual = problem1b(2, 1)
    print('Test 3 expected:', expected)
    print('       actual:  ', actual)

    # Test 4
    expected = 44
    actual = problem1b(5, 40)
    print('Test 4 expected:', expected)
    print('       actual:  ', actual)

def problem1b(m, f):
    """
    What comes in:  Positive integers m and f such that m >= 2.
    What goes out:
      -- Returns the number of integers from m to (f * m),
         inclusive, that are prime.
    Side effects:   None.
    Examples:
      -- If m is 3 and f is 5, this function returns 5,
           since 3, 5, 7, 11, and 13 are the integers between 3 and 15,
           inclusive, that are prime.
      -- If m is 2 and f is 1, this function returns 1,
           since there is one prime (namely, 2) between 2 and 2.
      -- If m is 5 and f is 40, the correct answer is 44,
           since there are 44 primes between 5 and 200.
     """
    # -------------------------------------------------------------------------
    # DONE: 6. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #
    ###########################################################################
    # IMPORTANT:
    #    **  For full credit you must appropriately
    #    **  use (call) the   is_prime   function that is DEFINED ABOVE.
    ###########################################################################
    # -------------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      5
    #    TIME ESTIMATE:   10 to 15 minutes.
    # -------------------------------------------------------------------------

    b = (f * m)
    count = 0
    for k in range(m,(b+1)):
        if is_prime(k):
                count = count + 1
    return count

def run_test_problem1c():
    """ Tests the   problem1c   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1c   function:')
    print('--------------------------------------------------')

    format_string = '    problem1c( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 3
    print_expected_result_of_test([10], expected, test_results, format_string)
    actual = problem1c(10)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 6
    print_expected_result_of_test([11], expected, test_results, format_string)
    actual = problem1c(11)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 33
    print_expected_result_of_test([25], expected, test_results, format_string)
    actual = problem1c(25)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 2
    print_expected_result_of_test([2], expected, test_results, format_string)
    actual = problem1c(2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 6
    print_expected_result_of_test([3], expected, test_results, format_string)
    actual = problem1c(3)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = 19416
    print_expected_result_of_test([10007], expected, test_results,
                                  format_string)
    actual = problem1c(10007)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = 19416
    print_expected_result_of_test([10008], expected, test_results,
                                  format_string)
    actual = problem1c(10008)
    print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)


def problem1c(n):
    """
    What comes in:  An integer n >= 2.
    What goes out:
      -- Returns the sum of the digits in the product
         of all the primes from 2 to n, inclusive.
    Side effects:   None.
    Example:
      -- If n is 10, this function returns 3,
           because the primes less than or equal to 10
           are 2, 3, 5 and 7, and the product of those numbers
           is (2 * 3 * 5 * 7), which is 210,
           and the sum of the digits in 210 is 3.
      -- If n is 11, this function returns 6,
           because the primes less than or equal to 11
           are 2, 3, 5, 7 and 11, and the product of those numbers
           is (2 * 3 * 5 * 7 * 11), which is 2310,
           and the sum of the digits in 2310 is 6.
      -- If n is 25, this function returns 33,
           because the primes less than or equal to 25
           are 2, 3, 5, 7, 11, 13, 17, 19, and 23,
           and the product of those numbers is 223092870,
           and the sum of the digits in 223092870 is 33.
    """
    # -------------------------------------------------------------------------
    # TODO: 7. Implement and test this function.
    #          Tests have been written for you (above).
    #
    ###########################################################################
    # IMPORTANT:
    #    **  For full credit you must appropriately
    #    **  use (call) the   is_prime   and   sum_of_digits
    #    **  functions that are DEFINED ABOVE.
    ###########################################################################
    # -------------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      7
    #    TIME ESTIMATE:   15 to 20 minutes.
    # -------------------------------------------------------------------------
    count = 1
    for k in range(2,n+1):
        if is_prime(k):
            count = count * k
    return sum_of_digits(count)

###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################

def print_expected_result_of_test(arguments, expected,
                                  test_results, format_string):
    testing_helper.print_expected_result_of_test(arguments, expected,
                                                 test_results, format_string)


def print_actual_result_of_test(expected, actual, test_results,
                                precision=None):
    testing_helper.print_actual_result_of_test(expected, actual,
                                               test_results, precision)


def print_summary_of_test_results(test_results):
    testing_helper.print_summary_of_test_results(test_results)


# To allow color-coding the output to the console:
USE_COLORING = True  # Change to False to revert to OLD style coloring

testing_helper.USE_COLORING = USE_COLORING
if USE_COLORING:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_colored
else:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_uncolored

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The   try .. except   prevents error messages on the console from being
# intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
try:
    main()
except Exception:
    print('ERROR - While running this test,', color='red')
    print('your code raised the following exception:', color='red')
    print()
    time.sleep(1)
    raise


def main2():
    even_odd(2)

    
def even_odd(x):
   b = x%2
   if b == 1:
        print('odd')
   else:
       print('even')


