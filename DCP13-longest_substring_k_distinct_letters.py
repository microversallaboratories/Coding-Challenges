#This problem was asked by Amazon.
#Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
#For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

#Using: Python

#Objective: divide the string into many different substrings.
#Judge length of the substring and store them as key-value pairs in a dictionary
#Search the keys and when you find the longest ones, print all which are the longest

s = "abcba"
k = 2
mydict = {}
longest_distinct = 0

for letter in s:
    l1 = letter
    l2 = s
    while 
