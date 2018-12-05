"""
PRACTICE Exam 1, problem 0.

These problems illustrate concepts that previous problems have not emphasized:
  -- determining whether a number is odd or even (Problem 0a)
  -- returning True or False (Problem 0a)
  -- is_prime (Problem 0b)
  -- animation (Problem 0c)

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Valerie Galluzzi, Mark Hays, Amanda Stouder, Aaron Wilkin,
         their colleagues, and PUT_YOUR_NAME_HERE.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg
import testing_helper
import time


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem0a()
    run_test_problem0b()
    run_test_problem0c()


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


def run_test_problem0a():
    """ Tests the   problem0a   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem0a   function:')
    print('--------------------------------------------------')

    format_string = '    problem0a( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = False
    print_expected_result_of_test([83135], expected, test_results,
                                  format_string)
    actual = problem0a(83135)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)
    if actual == 'False':
        print('Your function returned the STRING "False",')
        print('which is WRONG.  It should have returned')
        print('the built-in constant False.')
        print('Ask for help as needed.')

    # Test 2:
    expected = True
    print_expected_result_of_test([306], expected, test_results, format_string)
    actual = problem0a(306)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)
    if actual == 'True':
        print('Your function returned the STRING "True",')
        print('which is WRONG.  It should have returned')
        print('the built-in constant True.')
        print('Ask for help as needed.')

    # Test 3:
    expected = False
    print_expected_result_of_test([246], expected, test_results, format_string)
    actual = problem0a(246)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = False
    print_expected_result_of_test([830931], expected, test_results,
                                  format_string)
    actual = problem0a(830931)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = True
    print_expected_result_of_test([730931], expected, test_results,
                                  format_string)
    actual = problem0a(730931)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = False
    print_expected_result_of_test([200], expected, test_results, format_string)
    actual = problem0a(200)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = True
    print_expected_result_of_test([562], expected, test_results,
                                  format_string)
    actual = problem0a(562)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = True
    print_expected_result_of_test([555], expected, test_results,
                                  format_string)
    actual = problem0a(555)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = False
    print_expected_result_of_test([13], expected, test_results,
                                  format_string)
    actual = problem0a(13)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)


def problem0a(n):
    """
    What comes in:  An integer.
    What goes out:
      -- Returns True if the sum of the digits in the given integer
         is odd, else returns False.
    Side effects:   None.
    Examples:
      -- If the given integer is 83135, this function returns False,
           since (8 + 3 + 1 + 3 + 5) is 20, which is NOT odd.
      -- If the given integer is 306, this function returns True,
           since (3 + 0 + 6) is 9, which IS odd.
      -- If the given integer is 246, this function returns False,
           since (2 + 4 + 6) is 12, which is NOT odd.
    """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #          Tests have been written for you (above).
    #
    ###########################################################################
    # IMPORTANT:
    #    **  For full credit you must appropriately
    #    **  use (call) the   sum_of_digits   function
    #    **  that is DEFINED ABOVE.
    ###########################################################################
    #
    # HINT:  To test whether a number  m   is even or odd,
    #        compute m % 2, i.e., the REMAINDER from m // 2.
    #        If that remainder is 0, the number is even.
    #        If that remainder is 1, the number is odd.
    #        Simply try a few examples to convince yourself of this.
    #        ASK FOR HELP if you do not understand this hint.
    # -------------------------------------------------------------------------
    # sum = sum_of_digits(n)
    # if sum % 2 == 0:
    #     return False
    # else:
    #     return True
    return sum_of_digits(n) % 2 == 1
def run_test_problem0b():
    """ Tests the   problem0b   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem0b   function:')
    print('--------------------------------------------------')

    format_string = '    problem0b( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 6
    print_expected_result_of_test([13], expected, test_results, format_string)
    actual = problem0b(13)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 1
    print_expected_result_of_test([2], expected, test_results, format_string)
    actual = problem0b(2)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 46
    print_expected_result_of_test([200], expected, test_results, format_string)
    actual = problem0b(200)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 168
    print_expected_result_of_test([997], expected, test_results, format_string)
    actual = problem0b(997)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)


def problem0b(n):
    """
    What comes in:  An integer n >= 2.
    What goes out:
      -- Returns the number of integers from 2 to n, inclusive,
         that are prime.
    Side effects:   None.
    Examples:
      -- If n is 13, this function returns 6,
           since there are 6 primes -- namely, 2, 3, 5, 7, 11, and 13 --
           between 2 and 13.
      -- If n is 2, this function returns 1,
           since there is one prime (namely, 2) between 2 and 2.
      -- If n is 200, the correct answer is 46,
           since there are 46 primes between 2 and 200.
     """
    # -------------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    #          Tests have been written for you (above).
    #
    ###########################################################################
    # IMPORTANT:
    #    **  For full credit you must appropriately
    #    **  use (call) the   is_prime   function that is DEFINED ABOVE.
    ###########################################################################
    # ------------------------------------------------------------------
    count = 0
    for k in range(n-1):
        if is_prime(k + 2):
            count += 1

    return count

def run_test_problem0c():
    """ Tests the   problem0c  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  problem0c  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # TWO tests on ONE window.
    title = 'Tests 1 & 2 of problem0c: blue circle + 6 circles;'
    title += ' then green circle + 3 circles'
    window1 = rg.RoseWindow(650, 300, title)

    circle1 = rg.Circle(rg.Point(100, 50), 30)
    circle1.fill_color = 'blue'
    problem0c(circle1, 6, window1)
    window1.continue_on_mouse_click()

    circle2 = rg.Circle(rg.Point(75, 200), 75)
    circle2.fill_color = 'green'
    problem0c(circle2, 3, window1)
    window1.close_on_mouse_click()

    # A third test on ANOTHER window.
    title = 'Test 3 of problem0c:  red circle + 10 circles'
    window2 = rg.RoseWindow(600, 200, title)

    circle3 = rg.Circle(rg.Point(50, 50), 20)
    circle3.fill_color = 'red'
    problem0c(circle3, 10, window2)
    window2.close_on_mouse_click()


def problem0c(circle, n, window):
    """
    See   problem0c_picture.pdf   in this project for pictures
    that may help you better understand the following specification:
    
    What comes in:
      -- An rg.Circle.
      -- A positive integer n.
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      Draws the given rg.Circle and n additional rg.Circles
      on the given rg.RoseWindow such that:
        -- The circles form a row of touching rg.Circles with the
             leftmost circle being the given rg.Circle.
        -- There is a 0.5 second pause after each rg.Circle is drawn.
      Must  ** NOT close **   the window.

    Type hints:
      :type circle: rg.Circle
      :type n: int
      :type window: rg.RoseWindow
    """
    # -------------------------------------------------------------------------
    # DONE: 5. Implement and test this function.
    #          Tests have been written for you (above).
    #
    ###########################################################################
    # HINT:   render(0.5)
    #   renders with a half-second pause after rendering.
    ###########################################################################
    # -------------------------------------------------------------------------
    circle.attach_to(window)
    x_val = circle.center.x + (circle.radius * 2)
    for _ in range(n):
        new_circle = rg.Circle(rg.Point(x_val,circle.center.y),circle.radius)
        new_circle.attach_to(window)
        x_val = x_val + (circle.radius*2)
        window.render(0.5)


    window.render()
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
