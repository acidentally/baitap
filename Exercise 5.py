# <ins> Question 5 </ins>
## Code a function which takes in a 2 numbers `n` and `q` as an argument
## The function returns the number of numbers that is divisible by q from `0` to `n`
## Example : count_div(100, 3) --> 34

def count_div(n, q) :
    print(n // q + 1)

count_div(100, 3)