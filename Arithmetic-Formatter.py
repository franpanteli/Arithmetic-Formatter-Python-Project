"""
    -> We are defining a Python function called `arithmetic_arranger`
    -> The first argument of this function is a list of strings with operations 
    -> The second arguement of this function is an optional boolean which instructs it to return the result of these 
        operations 
    -> These are entered into the first argument of the function in a list 
    -> We want the function to return them displayed in a vertically stacked display 
"""

def arithmetic_arranger(problems, answer=False):

"""
    -> The first argument of the function is a list of the different operations which we want to stack 
    -> If we have too many operations (more than 4 of them) for this argument, then we want to return an error message
    -> This section of the function checks the number of these arguments, to see if we have too many of them or not
"""

    if len(problems) > 5:
        return "Error: Too many problems."

# We are then defining four empty arrays, to store the operations of the first argument in the function in
    first_line, second_line, third_line, fourth_line = [], [], [], []

"""
    Iterating through problems:
        -> The first argument to the function is an array of operations 
        -> Those oeprations all follow the same basic form 
        -> Some number, ± some other number 
        -> We are iterating through each of those operations listed in the first argument of the function <- This is why 
            we are using a for loop (each of those operations in the list is a `problem`)
        -> And each of those is in that same basic form <- or we want to make sure that it is 
        -> The basic form is number ± other number 
        -> If this isn't the case, we want to return error messages
        -> So we need the operand to be a ±, and if this isn't we return an error message
        -> This is us implementing the error handling with the question asked for (refer to the project task notes)
        -> Each condition we want to check that the function input satisfies requires its own error handling 
        -> Another condition that we are checking in this block is that the operation only contains digits <- In the 
            alternative case, returning another error message
        -> And finally that the number of digits in the numbers which we are operating on isn't greater than 4
"""

    for problem in problems:
        pieces = problem.split()
        first, operator, second = pieces

        if operator not in "+-":
            return "Error: Operator must be '+' or '-'."

        if not (first.isdigit() and second.isdigit()):
            return "Error: Numbers must only contain digits."

        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(first), len(second)) + 2
        first_line.append(first.rjust(width))
        second_line.append(operator + second.rjust(width - 1))
        third_line.append('-' * width)

        if answer:
            result = str(eval(problem))
            fourth_line.append(result.rjust(width))






    arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line)




    if answer:





        arranged_problems += "\n" + "    ".join(fourth_line)
    return arranged_problems