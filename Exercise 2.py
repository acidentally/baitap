# <ins> Question 2: </ins>
## Code the f(n) function which takes in a number as an argument
## and return the first n fibonacci numbers
### The fibonacci sequence is defined as : f(1) = f(2) = 1, f(n + 2) = f(n + 1) + f(n)

## Example : f(5) --> 1 1 2 3 5

def f(n) :
    if n == 1 :
        print(1)
        return
    elif n == 2 :
        print(1, 1)
        return
    else :
        print(1, 1, end = ' ')
        x = y = 1
        count = 2
        while count < n :
            y = x + y
            x = y - x
            print(y, end = ' ')
            count += 1

f(5)