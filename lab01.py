"""Lab 1: Expressions and Control Structures"""

def both_positive(a, b):
    """Returns True if both a and b are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    return a > 0 and b > 0 # You can replace this line!

def sum_digits(x):
    """Sum all the digits of x.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    string_of_numbers = str(x)
    sum = 0
    for digit in string_of_numbers:
        sum += int(digit)
    return sum

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    # bruh should always try to start from the 0 case, rather than jump ahead to the 1 case, so that you can also account for the 0 case without having to write extra code
    counter = 0
    sum = 1
    while counter < k:
        sum = sum * (n - counter)
        counter += 1
    return sum
    

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    def exact_divisor(x, n):
        """Returns the quotient and remainder of X divided by N"""
        return x // n, x % n
    
    # loop only continues if n has >= 2 digits left
    # loop starts by checking from the back
    while n > 10: 
        quotient, remainder = exact_divisor(n, 10)
        if quotient % 10 == 8 and remainder == 8:
            return True
        n = quotient
          
    return False 
        
