# Solution to Project Euler problem 6

# Sum of square of consecutive natural numbers
# Square of the sum of consecutive natural numbers

# The sum of the squares of the first ten natural numbers is,

#                     1 power(2) + 2 power(2) + ... + 10 power(2) = 385
# The square of the sum of the first ten natural numbers is,

#                     (1 + 2 + ... + 10) power(2) = 55 power(2) = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 minus 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# it's  a no brainer
# Sum of square of consecutive natural numbers

# 1 power(2) = 1 
# 2 power(2) = 4
# 3 power(2) = 9
# 4 power(2) = 16
# 5 power(2) = 25
# 6 power(2) = 36
# 7 power(2) = 49
# 8 power(2) = 64
# 9 power(2) = 81
# 10 power(2) = 100

# Sum of Square = 1 + 4 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 100 = 385

# This can also be achived by a formula  n(n+1)(2n+1)       10(10+1)(2X10+1)
#                                         ____________  =    ________________ =  385
#                                             6                      6


# Square of the sum of consecutive natural numbers

#   (1 + 2 + ... + 10) power(2) = 55 power(2) = 3025

# This can also be achived by a formula = n(n+1)     10(10+1)
#                                         ________  = ________   55 power (2) 3025
#                                            2           2


def compute_diff_of_squares(first_n):

    sum_of_squares = (first_n*(first_n+1)*(2*first_n+1))/6
    
    sum_of_n = (first_n*(first_n+1))/2 
    square_of_sum = sum_of_n*sum_of_n

    diff = square_of_sum - sum_of_squares
    print diff

if __name__ == "__main__":
	#compute_diff_of_squares(10)
    compute_diff_of_squares(100)


