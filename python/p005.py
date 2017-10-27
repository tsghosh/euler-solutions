# Solution to Project Euler problem 5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#LCM

#short ans Way - 1 school style
#The number from 1 to 10 can be written as 

    # 1
    # 2
    # 3
    # 4 = 2 power(2)
    # 5
    # 6 = 2 X 3
    # 7 
    # 8 = 2 power(3)
    # 9 = 3 power(2)
    # 10 = 2 X 5

# Lets pick one unique element from the above list and multiply , If any number is repeated we take the maximum power
# so product  =  1 X 2 power (3) X 3 power (2) X 5 X 7 = 2520

# Way - 2 Computer friendly way
# Now lets create a function that will take the range as input and determine its LCM (least common multiple), 
# i.e LCM of 10, 9, 8, 7, 6, 5, 4, 3, 2, 1  should match 2520

# 2 |_1_,_2_,_3_,_4_,_5_,_6_,_7_,_8_,_9_,10__
# 2  |_1_,_1_,_3_,_2_,_5_,_3_,_7_,_4_,_9_,5__
# 2   |_1_,_1_,_3_,_1_,_5_,_3_,_7_,_2_,_9_,5__
#     3   |_1_,_1_,_1_,_1_,_5_,_1_,_7_,_1_,_3_,5__
#     3   |_1_,_1_,_1_,_1_,_5_,_1_,_7_,_1_,_1_,5__
#         5   |_1_,_1_,_1_,_1_,_1_,_1_,_7_,_1_,_1_,1__
#         7   |_1_,_1_,_1_,_1_,_1_,_1_,_1_,_1_,_1_,1__

# so LCM = 2X2X2 X 3X3 #X 5X7 = 2 power (3) X 3 power (2) X 5 X 7 = 2520
# It is easy to create a function through Way - 2 as we loop through the records

def compute_lcm(*numbers):
    lst_numbers = list(numbers)
    lcm = 1

    while len(lst_numbers) > 0:
        min_value = min(lst_numbers)
        divisor = 1
        #lets find the divisors
        if min_value % 2 == 0 :
            divisor = 2
        elif min_value % 3 == 0:
            divisor = 3
        elif min_value % 5 == 0:
            divisor = 5   
        else:
            divisor = min_value

        #loop through all numbers and check if they are divisible
        for x in range(0,len(lst_numbers)):        
            quotient =  lst_numbers[x] / divisor
            reminder =  lst_numbers[x] % divisor
            if reminder == 0:
                #ifthe reminder is 0 quotent will be our new value
                lst_numbers[x] = quotient
                
        lcm = lcm*divisor
        min_value = min(lst_numbers)
        if min_value == 1:
            lst_numbers.remove(min_value)


    print lcm

if __name__ == "__main__":
	#compute_lcm(1,2,3,4,5,6,7,8,9,10)
	#compute_lcm(1,2,3,4)

#the same function canbe used to compute lcm of 1 to 20
    compute_lcm(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

