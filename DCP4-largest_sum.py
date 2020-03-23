l = [2,4,6,2,5]

#calculate two values, depending on whether you use odd or even starting number

#FUNCTIONAL DECOMPOSITION

# Sum every odd element

# Sum every even element

# Generate a list of even numbers

# There's basically two options for this to work. Either you start on an odd or even list and pick every other element. This works for the following list:
# l1 = [5 0 5 0 5 0 5]

# The other way is that the largest sum of elements requires some combination of even-list and odd-list sequences, like the following:
# l2 = [5 0 0 5 0 0 0 5 0 0 5]

# Probably the easiest way is to 

# Find every valid combination of numbers. Basically run the same algo starting on either the first or the second element.
def combinator(l):
	max_num = 0	# maximum number generated so far
	elems = []	# list of elements selected for the list

	# start on the first (0-place) element
		# 


	# start on the second (1-place) element


# If a combo produces a higher value than previously, set it as max and best

# Check 

# Create all sets of nonadjacent sums
# 

# Calculate the sum of n numbers
def calc_nonadj_sum




