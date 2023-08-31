# # # # abcd = (1,2,3)
# # # # print(abcd)
# # # set1 = {10,50,90,40}
# # # print(set1)
# # def add():
# #     print("Hello I am Amar Patil from Latur.\nI have completedbmy BCA from COCSIT.\n I am 25 year old.")
# # add()
# # def add():
# #     a = str(input("Enter Name:"))
# #     print("hello,",a)
# # add()
# # def fun(abc,xyz):
# #     print(abc+xyz)
# # fun(1,3)
# # 
# # print("Enter three Numbers: ")
# # numOne = int(input())
# # numTwo = int(input())
# # numThr = int(input())

# # if numOne>numTwo:
# #     if numTwo>numThr:
# #         large = numOne
# #     else:
# #         if numThr>numOne:
# #             large = numThr
# #         else:
# #             large = numOne
# # else:
# #     if numTwo>numThr:
# #         large = numTwo
# #     else:
# #         large = numThr

# # print("\nLargest Number =", large)

# # def number():        
# #     number = float(input('please enter a number (must be greater thatn zero): '))

# #     if number >= 0 :    
# #         print ('you choose number:', number)    
# #     else:
# #         print ('invalid input')    
# #         return 

# # number()

# # def avgfun (*n):
# #     sum = 0
# #     for t in n:
# #         sum = sum + t
# #     avg = sum / len(n)
# #     return avg
# # r1 = avgfun(1, 2, 3, 6, 15)
# # r2 = avgfun(2, 6, 4, 8)
# # print(round(r1, 2))
# # print(round(r2, 2))
# *Question 1:*
# Write a Python function named `calculate_average` that takes a list of numbers as
# a parameter and returns the average of those numbers.
# def cal_avg(lst):
#     # print(lst)
#     avg = 0
#     for i in lst:
#         avg = avg + i
#     # print(avg)
#     avg = avg / len(lst)
#     # print(avg)
#     return avg

# lst1 = [20,459,12,349,4621,4971,34185,465,1654,69854]
# print(cal_avg(lst1))

# *Question 2:*
# Create a function `find_max_min` that takes a list of numbers as input and
# returns a tuple containing the maximum and minimum values in the list.
# def find_max_min(lst):
#     print(lst)
#     min = lst[0]
#     max = lst[0]
#     for i in lst:
#         if i > max:
#             max = i
#         if i < min:
#             min = i
#     print("max is ", max)
#     print("min is", min)
#     return (min,max)
# lst1 = [20,459,12,349,4621,4971,34185,465,1654,69854]
# print(find_max_min(lst1))

# *Question 3:*
# Write a function `is_prime` that takes an integer as an argument and returns `True` if it's a prime number, 
# and `False` otherwise.
# def is_prime(a):
#     for i in range(2,a):
#         if a % i == 0:
#             return False
#         else:
#             continue
#     return True

# print(is_prime(18))


# *Question 4:*
# Create a function `reverse_string` that takes a string as input and returns the string in reverse order.
# def reverse_string(str1):
#     # print(str1[0])
#     # print(len(str1))
#     str2 = ""
#     for i in range(len(str1)-1,-1,-1):
#         # print(str1[i])
#         str2 = str2 + str1[i]
        
#     print(str2)
        
# reverse_string("Amar Patil")




# *Question 5:*
# Write a function `count_vowels` that takes a string as input
# and returns the count of vowels (both lowercase and uppercase) in the string.

# *Question 6:*
# Create a function `unique_elements` that takes two lists as parameters and returns a new list containing only the unique elements from both lists.

# *Question 7:*
# Write a function `power_list` that takes a list of numbers and a power as arguments and returns a new list with each number raised to the given power.

# *Question 8:*
# Create a function `remove_duplicates` that takes a list as input and returns a new list with duplicate elements removed while maintaining the original order.

# *Question 9:*
# Write a function `matrix_transpose` that takes a 2D matrix (list of lists) as input and returns the transpose of the matrix.

# *Question 10:*
# Create a function `find_common_elements` that takes two lists as parameters and returns a new list containing the common elements between the two lists.

# *Question 11:*
# Write a function `fibonacci_sequence` that generates the first n numbers in the Fibonacci sequence as a list. The function should take `n` as an argument.

# *Question 12:*
# Create a function `capitalize_titles` that takes a list of strings (book titles) as input and returns a new list with the titles properly capitalized (capitalize the first letter of each word except for common words like "and", "the", "of", etc.).

# *Question 13:*
# Write a function `flatten_list` that takes a nested list as input and returns a flat list containing all the elements.

# *Question 14:*
# Create a function `largest_continuous_sum` that takes a list of integers and finds the largest sum of continuous elements in the list.

# *Question 15:*
# Write a function `anagram_check` that takes two strings as input and returns `True` if the strings are anagrams (contain the same characters in different orders), and `False` otherwise.

# *Question 16:*
# Create a function `binary_search` that performs a binary search on a sorted list and returns the index of the target element if found, or `-1` if not found.

# *Question 17:*
# Write a function `flatten_dictionary` that takes a nested dictionary as input and returns a flattened dictionary where the keys are concatenated with parent keys using underscores.

# *Question 18:*
# Create a function `prime_factors` that takes an integer as input and returns a list of its prime factors.

# *Question 19:*
# Write a function `shuffle_list` that takes a list as input and returns a new list with the elements shuffled randomly.

# *Question 20:*
# Create a function `run_length_encoding` that takes a string as input and returns its run-length encoded version. For example, `"aaabbbccaa"` should become `"3a3b2c2a"`.