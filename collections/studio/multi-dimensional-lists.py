food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.
new_equipment = equipment.split(",")
new_pets = pets.split(',')
new_sleep_aids = sleep_aids.split(',')
print(new_equipment)
print(new_pets)
print(new_sleep_aids)
# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.
cargo_hold = new_equipment + new_pets + new_sleep_aids
print(cargo_hold)


# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.
selected_cabinet = input(print(f'Select which cabinet you would like from cargo hold form 0 - 3'))


# d) Use bracket notation and format to display the contents of the selected cabinet. If the user entered an invalid number, print an error message.
if selected_cabinet == 0:
    print(cargo_hold[0])
elif selected_cabinet == 1:
    print(cargo_hold[1])
elif selected_cabinet == 2:
    print(cargo_hold[2])
else:
    print('number outside range, selected a different number.')


# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. Use the in method to check if the cabinet contains the selected item, then print “Cabinet ____ DOES/DOES NOT contain ____.”
