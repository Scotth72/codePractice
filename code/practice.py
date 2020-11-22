# print("Hello world")

# Find all the pairs of two integers in an unsorted array that sum up to a given S. For example, if the array is [3, 5, 2, -4, 8, 11] and the sum is 7, your program should return [[11, -4], [2, 5]] because 11 + -4 = 7 and 2 + 5 = 7.

#  Given
# have an array of unsorted
# - the sum

# plan
# for loop
    # for loop
# if statement
#     return answer

# return "no match"

arr = [3, 5, 2, -4, 8, 11]
sum = 7

def find_pair(s, arr ):
    for i in range( len(s) -1):
        for j in range(i +1, len(s)):
            if s(i) + s(j) == sum:
                print( i, j)
                return


