# Write the factorial function. Remember, for a number n, the factorial is all
# numbers from 1 to n multiplied together.

# Write your function here.
def factorial(n):
    result=1
    for number in range(1,n+1):
        result = result * number
    return result

# can also do through recursion
# def factorial(n):
#     if n < 0:
#         raise ValueError("Factorial is not defined for negative numbers.")
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)

print(factorial(1))     #> 1
print(factorial(8))     #> 40320
print(factorial(12))    #> 479001600