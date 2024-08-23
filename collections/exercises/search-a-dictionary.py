flavors = {
  'chocolate' : 0.35,
  'vanilla' : 0.35,
  'strawberry' : 0.42,
  'cookies and cream' : 0.45,
  'mint chocolate chip' : 0.42,
  'fudge chunk' : 0.45,
  'saffron' : 2.25,
  'garlic' : 0.05
}

## Set a variable called choice to the flavor you want to search for.
choice = 'mint chocolate chip'
## Use an if statement to check if choice is in the flavors dictionary.
print(choice in flavors)
## If it is, set another variable called cost to the value associated with choice.
if choice in flavors:
    cost = flavors[choice]
    

## If it isn’t, set cost to 0.
if choice not in flavors:
    cost = 0
## Print the cost.
print(cost)
### Search a Dictionary Part 2:

## Initialize two variables: highest_cost to 0 and fanciest to an empty string.
highest_cost = 0
fanciest = ''
## Loop through the flavors dictionary using a for loop.
for key in flavors:
## For each flavor, check if its price is higher than highest_cost.
    if flavors[key] > highest_cost:
## If it is, update fanciest to this flavor and highest_cost to its price.
      fanciest = key
      highest_cost = flavors[key]
## After the loop, print the most expensive flavor.
print(f'''Most epensive flavor is {fanciest}
Highest cost is {highest_cost}''')