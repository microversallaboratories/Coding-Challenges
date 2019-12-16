#Prompt: Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.
#For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
#10 = max(10, 5, 2); 7 = max(5, 2, 7); 8 = max(2, 7, 8); 8 = max(7, 8, 7)
#Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.

#Idea: Index the list for each length of three integers, finding the max of those three
#Iterate through k - 2 times.

array = [10,5,2,7,8,7]
final_array = []

def find_max(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            return num1
        else:
            return num3
    elif num2 > num3:
        return num2
    else:
        return num3

for i in range(len(array)-2):
    final_array.append(find_max(array[i], array[(i+1)], array[(i+2)]))

print(final_array)
