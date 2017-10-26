# Solution to Project Euler problem 4

# Largest palindrome product
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 \xc3 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

#assume AZZA is the number we are searching then AZZA = YY x XX 
#lets create a program to find the largest palindrom from the product of two 2-digit numbers as explained in problem

#largest 2 digit number = 99 and smallest is 10, so we loop through each and check plaindrom


def find_largest_plaindrom_from_product_2_digit():
    max_pal=0
    for x in range(10,100):
        for y in range(10,100):
            prod = str(x*y)
            rev_str = str(x*y)[::-1] 
            if prod == rev_str:
                if x*y > max_pal:
                    max_pal = x*y

    print max_pal, 'is a largest palindrome which is product of two 2-digit numbers'

# similarly largest 3 digit number = 999 and smallest is 100, so we loop through each and check plaindrom

def find_largest_plaindrom_from_product_3_digit():
    max_pal=0
    for x in range(100,1000):
        for y in range(100,1000):
            prod = str(x*y)
            rev_str = str(x*y)[::-1] 
            if prod == rev_str:
                if x*y > max_pal:
                    max_pal = x*y

    print max_pal, 'is a largest palindrome which is product of two 3-digit numbers'

if __name__ == "__main__":
	#find_largest_plaindrom_from_product_2_digit()
    find_largest_plaindrom_from_product_3_digit()