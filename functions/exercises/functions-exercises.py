# Part 1 A -- Make a Line
def make_line(num):
    line = ''
    for i in range(num):
        line += '#'
    return line
# print(make_line(5)

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

print('test')
'yes'
# print(make_rectangle(5,3))


# Part 2 A -- Make a Stairs
def make_stairs(steps):
    stairs = '' 
    for x in range(steps):
        stairs += '\n#'+ make_line(x)
    return stairs

# print(make_stairs(5))  


# Part 2 B -- Make Space-Line 
def make_space_line(numspaces, numchars):
    space = ''
    hash = ''
    for x in range(numspaces):
       space = numspaces * ' '
    for y in range(numchars):
       hash = numchars * '#'
    return space + hash + space
# print(make_space_line(2,3))


# Part 2 C -- Make Isosceles Triangle

def make_isosceles_triangle(height):
    tri = ''
    for x in range(height):
       tri += make_space_line(height - x - 1, 2 * x + 1) + "\n"
    return tri

# print(make_isosceles_triangle(5))

# Part 3 -- Make a Diamond

def make_diamond(height):
    diamond = ''
    bottom_diamond = make_isosceles_triangle(height)
    diamond += bottom_diamond[:-1]
    for x in range(len(bottom_diamond)-1,-1,-1):
       diamond += bottom_diamond[x]
    return diamond
print(make_diamond(4))



