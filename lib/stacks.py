# Pseudocude
# define a fuction with the expression as an argument
# create a stack
# scan the expression using Lookup
# do an if statement to check if characters are opening parentheses, opening curly braces or opening square brackets
#   push to the stack
#  else if the stack is empty and does not match the closing bracket for stack.pop()
# return false


def is_balanced(expression):
    stack = []
    brackets = {'(':')','[':']', '{':'}' }

    for char in expression:
        if char in brackets:
            stack.append(char)
        else:
            if len(stack) == 0 or char != brackets[stack.pop()]:
                return False
    return len(stack) == 0

    
print(is_balanced ("([]{}"))