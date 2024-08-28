# 1. Declare and assign the variables here:
ss_name = 'Determination'
ss_speed = 17500
dis_to_mars = 225000000
dis_to_moon = 384400
mpk = .621
# 2. Use print() to print the 'type' each variable. Print one item per line.
print(type(ss_name))
print(type(ss_speed))
print(type(dis_to_mars))
print(type(dis_to_moon))
print(type(mpk))
# Code your solution to exercises 3 and 4 here:
miles_to_mars = dis_to_mars * mpk
hours_to_mars = miles_to_mars/ss_speed
days_to_mars = hours_to_mars/24

print(ss_name + " " + "will take" +" "+ str(days_to_mars) + " " + "days to reach Mars.")
# Code your solution to exercise 5 here
