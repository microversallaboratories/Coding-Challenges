#Prompt: Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#Bonus: Can you do this in one pass?

#LANG=Python

list1 = [10,15,3,7,6,3,9]
k = 18
copy_list1 = list1

#Option 1:
#-  Loop through the list, and check whether the value i 
#   plus any other value in the list is equal to k.

for i in list1:
    for j in copy_list1:
        if (i + j == k) and (i != j):
            print("Yes, because ",i, " + ",j, " = ", k)

