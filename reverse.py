# Write your solution for algorithm 3 below

from random_list_gen import make_random_list

unsorted_list = make_random_list(20)

sorted_list = sorted(unsorted_list, reverse = True)

print(sorted_list)

new_sorted_list = sorted(unsorted_list, reverse = False)
print(new_sorted_list)