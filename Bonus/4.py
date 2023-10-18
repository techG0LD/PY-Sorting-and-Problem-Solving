# Write your solution for algorithm 4 below

test_string = 'Birds are not real. Nor is ball earth'

sorted_string = sorted(test_string.split(),key=str.lower)
no_key_sorted = sorted(test_string.split())


print(sorted_string)
print(no_key_sorted)