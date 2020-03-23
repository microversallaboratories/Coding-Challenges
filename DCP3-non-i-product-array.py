#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#Follow-up: what if you can't use division?

#Using list exclusion:
input_list = [1,2,3,4,5,6,7]
output_list = [1] * len(input_list)

il = list(range(len(input_list)))   #Form index lists
ol = list(range(len(output_list)))

print("Input list is: ", input_list)

for i in il:
    for j in ol:
        if j != i:
            output_list[i] *= input_list[j];

print("Output list is: ", output_list)
