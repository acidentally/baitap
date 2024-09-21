# <int> Question 1: </ins>
## Program a function which takes in a number (n) as a(n) parameter/argument and
## print a list of increasing positive even numbers that has n numbers

### Example : increasing_even(4) --> [2, 4, 6, 8]

def increasing_even(n) :
    cnt = 2
    outputList = []
    while cnt <= 2 * n :
        outputList.append(cnt)
        cnt += 2
    print(outputList)

increasing_even(4)