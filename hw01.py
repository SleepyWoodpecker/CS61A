""" Homework 1: Control """

from operator import add, sub
# I guess a lot of the solutions try to utilize reverse logic, instead of following the original order given by the question. Got to try to think about solving the problem from the back I guess.


def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> # a check that you didn't change the return statement!
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
    ['return h(a, b)']
    """

    if b >= 0:
        h = lambda a,b: add(a, b)

    else:
        h = lambda a,b: add(a, -b)

    return h(a, b)


def two_of_three(x, y, z):
    """Return a*a + b*b, where a and b are the two smallest members of the
    positive numbers x, y, and z.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    >>> # check that your code consists of nothing but an expression (this docstring)
    >>> # a return statement
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
    ['Expr', 'Return']
    """
    return add(min(x, y, z) ** 2, min(max(x, y), max(x, z), max(y, z)) ** 2)


def largest_factor(x):
    """Return the largest factor of x that is smaller than x.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    # should actually have started from the back... that would have produced the fastest solution...
    largest_factor = 1;
    # goes from 0 all the way up till x - 1, like a traditional for loop
    # range (start, end, skip)
    for i in range (1, x):
        if x % i == 0:
            largest_factor = i
    
    return largest_factor


def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> result = with_if_statement()
    6
    >>> print(result)
    None
    """

    if c():
        return t()
    else:
        return f()


def with_if_function():
    """
    >>> result = with_if_function()
    5
    6
    >>> print(result)
    None
    """
    return if_function(c(), t(), f())


def c():
    "*** YOUR CODE HERE ***"
    return False


def t():
    "*** YOUR CODE HERE ***"
    print(5)


def f():
    "*** YOUR CODE HERE ***"
    print(6)



def hailstone(x):
    """Print the hailstone sequence starting at x and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    def print_and_count(x, counter):
        print(x) 
        return counter + 1
    # start with 1 because taking in the first input is already the first print
    counter = 0

    while (x != 1):
        counter = print_and_count(x, counter)
        if x % 2 == 0:
            x//=2
        else:
            x = x * 3 + 1

    counter = print_and_count(x, counter)
        
    return counter
   

