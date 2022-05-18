# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
evenList = list()
for num in numbers:
    if num % 2 == 0:
        evenList.append(num)

# 2. Print the difference between the largest and smallest value:
# numbers.sort()     #I commented this out because it was messing stuff up with the later questions 
range = numbers[(len(numbers)-1)] - numbers[0]

# 3. Print True if the list contains a 2 next to a 2 somewhere. 
"""
I'm certain there's a better way of doing this but I spent so long
doing this that I'm weirdly attached to it
"""
index_location_1 = 0
index_location_2 = 0
i = 0
for num in numbers:
    if num == 2:
        index_location_1 = i
        break
    i = i + 1
i = 0
for num in numbers:
    if num == 2:
        index_location_2 = i
    i = i + 1

    
# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

# count until it gets to a six and stop THEN count until it starts at a 7 and start



# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5.
sum_stop_at_13 = 0
for num in numbers:
    if num != 13:
        sum_stop_at_13=sum_stop_at_13+num
    else:
        break



# print(evenList)
# print(range)
# print(index_location_2 - index_location_1 == 1)

# print(sum_stop_at_13)

print(numbers)





