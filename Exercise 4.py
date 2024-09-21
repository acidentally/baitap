# <ins> Question 4 </ins>
## Code a function which takes in a nxm board of numbers in terms of tuples  as an argument
## The function then returns the sum of all columns and rows in the board described
## Example : sum((1, 3, 5),
##               (2, 4, 6),
##               (3, 5 ,7)) --> 72

def sum(board) :
    answer = 0
    for row in board :
        for num in row :
            answer += num
    print(2 * answer)

sum(((1, 3, 5),
     (2, 4, 6),
     (3, 5 ,7)))
