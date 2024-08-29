# Part 1 A -- Make a Line
def make_line(num):
    line = ''
    for i in range(num):
        line += '#'
    return line

# print(make_line(5))


# Part 1 B -- Make a Square
# create a function using your make_line function to code a square

def make_square(num):
    column = ''
    for x in range(num):
        column += '\n#' + make_line(num)
    return column

# print(make_square(5))

# Part 1 C -- Make a Rectangle

def make_rectangle(length,width):
    rec = ''
    for x in range(length):
        rec += "\n#" + make_line(width) 
    return rec


# print(make_rectangle(5,3))


# Part 2 A -- Make a Stairs
def make_stairs(steps):
    stairs = '' 
    for x in range(steps):
        stairs += '\n#'+ make_line(x)
    return stairs

print(make_stairs(6))  




# Part 2 B -- Make Space-Line 





# Part 2 C -- Make Isosceles Triangle





# Part 3 -- Make a Diamond






