# Given a list of integers, return the difference between the largest and
# smallest integers in the list.

# Write your function here.
def difference(input):
    return max(input) - min(input)

print(difference([10, 15, 20, 2, 10, 6]))
# 20 - 2 = 18

print(difference([-3, 4, -9, -1, -2, 15]))
# 15 - (-9) = 24

print(difference([4, 17, 12, 2, 10, 2]))
# 17 - 2 = 15