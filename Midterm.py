# Diogo Terra Simões da Motta
# Programming for Economists II - Midterm

# Q1
# print(25 % 7 * 3 - 4)
# result is 8

# ------------------------------------------------------------
# Q2
# Github Repo -> https://github.com/DMotta23/Midterm

# ------------------------------------------------------------
# Q3
# A mutable object is one whose contents can be changed in place, without creating a new object in memory.
# Lists are mutable, so we can add, remove, or modify their elements directly. An immutable object cannot be changed after
# it is created. If we try to “modify” a string, Python actually creates a new string object instead of altering the original one.

# So, a list is like a whiteboard, where whatever's written can be erased, modified, but the whiteboard itself remains the
# same "object" in this case. Meanwhile, a string is like a receipt, where the content cannot be modified but this implies printing
# out a new receipt (new object), as you cannot erase the ink.

# l1 = [1,"a",True,None]
# print(l1)
# l1[1] = "b"
# print(l1)
#
# s1 = "Hello, my name is Diogo"
# # s1[5] = "." # Will give a TypeError: 'str' object does not support item assignment
# s2 = s1[:5] + "." + s1[6:] # correct way of implementing the code above
# print(s2)

# ------------------------------------------------------------
# Q4
# URL must be a string, start with a valid protocol "http//:" or "https//:", have no spaces,
# have characters after the protocol, and contain at least one dot after the domain

# Valid examples:
# http://google.com
# https://bbc.co.uk

# Invalid examples:
# google.com           (missing protocol)
# http://              (no domain)
# http://google        (no dot)
# http://goo gle.com   (space)

# def is_valid_url(url):
#     """
#     Checks whether the provided string is a valid basic URL.
#
#     A valid URL in this context:
#     - starts with http:// or https://
#     - contains no spaces
#     - contains at least one dot in the domain
#     - does not start or end the domain with a dot
#
#     :param url: string representing the URL to validate
#     :return: True if URL is valid, False otherwise
#     """
#
#     # no spaces allowed
#     if " " in url:
#         print("Invalid URL: spaces are not allowed.")
#         return False
#
#     # check protocol
#     if url.startswith("http://"):
#         start = 7
#     elif url.startswith("https://"):
#         start = 8
#     else:
#         print("Invalid URL: must start with http:// or https://")
#         return False
#
#     # extract domain
#     domain = url[start:]
#
#     # domain must not be empty
#     if domain == "":
#         print("Invalid URL: missing domain name.")
#         return False
#
#     # must contain at least one dot
#     if "." not in domain:
#         print("Invalid URL: domain must contain a dot.")
#         return False
#
#     # dot cannot be first or last
#     if domain.startswith(".") or domain.endswith("."):
#         print("Invalid URL: dot cannot be at the start or end of the domain.")
#         return False
#
#     print("The URL is valid.")
#     return True

# url = input("Enter URL: ")
# is_valid_url(url)

# ------------------------------------------------------------
# Q5
# def days_since_birthday(birthday):
#     """
#     Calculates how many days have passed since the given birthday,
#     counting only full years between the birth year and the current year.
#
#     Assumes current year = 2026.
#
#     :param birthday: string in format "DD-MM-YYYY"
#     :return: number of days in full years between
#     """
#
#     # --- extract year from string ---
#     parts = birthday.split("-") #splits day,month,year into list
#     birth_year = int(parts[2]) #transforms year into integer
#
#     current_year = 2026
#
#     # if no full years in between
#     if birth_year >= current_year - 1:
#         return 0
#
#     total_days = 0
#
#     # loop through full years only
#     for year in range(birth_year + 1, current_year):
#
#         # check leap year
#         if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#             total_days += 366
#         else:
#             total_days += 365
#
#     return total_days
#
# bday = input("Enter birthday (DD-MM-YYYY): ")
# print("Days in full year since birth: ", days_since_birthday(bday))

# ------------------------------------------------------------
# Q6
# def longest_c_word(filename):
#     """
#     Returns the longest word in the file that starts with 'c'.
#
#     :param filename: name of the text file
#     :return: longest word starting with 'c' (or empty string if none)
#     """
#
#     longest = ""  # stores the best word found so far
#
#     try:
#         with open(filename, "r") as f:   # open file for reading
#             for line in f:               # process file line by line
#                 line = line.lower()      # make search case-insensitive
#
#                 # remove common punctuation (course-level cleaning)
#                 for ch in ".,;:!?()[]\"'\n\t":
#                     line = line.replace(ch, "")
#
#                 words = line.split()     # split line into words
#
#                 for word in words:       # examine each word
#                     if word.startswith("c"):      # must start with 'c'
#                         if len(word) > len(longest):  # check if longer
#                             longest = word            # update best word
#
#         return longest
#     except FileNotFoundError:
#         return ""
#
# filename = input("Enter filename: ")
# result = longest_c_word(filename)
# if result == "":
#     print("File not found, or there are no words with c.")
# else:
#     print("Longest word starting with 'c':", result)

# ------------------------------------------------------------
# Q7
# def palindrome(word):
#     if word == word[::-1]:
#         return True
#     else:
#         return False
#
# print(palindrome("9847255590886266818998186626880955527489"))
# print(palindrome("6892149109325320763773670235239019412986"))
# print(palindrome("6800923757255865070000705685527573290086"))
# print(palindrome("1414884937242655719669145562427394884141")) # returns False

# ------------------------------------------------------------
# Q8
# a = 6
# a = a - 2
# print(a*2)
# a = a * 2
# print(a+1)
# a = a // 3
# print(a) # a is 2

# ------------------------------------------------------------
# Q9
# import random
#
# random_numbers = []
#
# # build the original list
# for i in range(10):
#     random_numbers.append(random.randint(1, 100))
#
# # iterate through list by index so we can MODIFY elements in place
# for i in range(len(random_numbers)):
#
#     # if number is greater than 50 → replace with random 20–30
#     if random_numbers[i] > 50:
#         random_numbers[i] = random.randint(20, 30)
#
#     # if number is less than 50 → replace with "XX"
#     elif random_numbers[i] < 50:
#         random_numbers[i] = "XX"
#
# # print final list
# print(random_numbers)

# ------------------------------------------------------------
# Q10
# import datetime
#
# a = 7
# b = 2
# today = datetime.datetime.today()
# day_of_week = today.weekday()
# month_of_year = today.month
# a = a + day_of_week
# b += month_of_year
#
# print(a)
# print(b)
# c = a + b
# print(c)
# d = "xyz" * (c // 3)
# print(d)