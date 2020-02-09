#Given a Roman numeral, find the corresponding decimal value. Inputs will be between 1 and 3999. 


class Solution():
    def romanToInt(self, s):
        int tot = 0         # Create the int tot
        for i in range(0, length(s)):   # For the length of the string s,
            int j = i
            while s(i) > s(j+1):       # Check from the LHS to the RHS if the current idx, converted to int, is bigger than the next idx.
                tot += s(j)         # If so, add the index to the running total
            else:                   # if not, 
                                    # check how many letters until this is not the case


                tot += (s(i) - s(i+1))                 # subtract the first index from the second index ((i+1)--)
                # Add the new value to the running total, tot
                i+=(inARow)

        # return tot

    def romanLetToInt(self, l, idx):
        # If character is 'M'
        if (l = 'I'):
            return 1
        elif (l = 'V'):
            return 5
        elif (l = 'X'):
            return 10
        elif (l = 'L'):
            return 50
        elif (l = 'C'):
            return 100
        elif (l = 'D'):
            return 500
        elif (l = 'M'):
            return 1000
        else:
            return "INVALID!!!"    

###MAIN###
    
n = 'MCMX'
print(Solution().romanToInt(n))
