pirates = [
  {'Name': 'Olaf', 'has_wooden_leg': False, 'gold': 12},
  {'Name': 'Uwe', 'has_wooden_leg': True, 'gold': 9},
  {'Name': 'Jack', 'has_wooden_leg': True, 'gold': 16},
  {'Name': 'Morgan', 'has_wooden_leg': False, 'gold': 17},
  {'Name': 'Hook', 'has_wooden_leg': True, 'gold': 20},
]

# Write a function that takes any list that contains pirates as in the example,
# And returns a list of names containing the pirates that has wooden leg and
# more than 15 gold

def pirates_check(check_dictonary):
    ### MAKE A NEW EMPTY LIST ###
    rich_pirates_with_wood_leg = []
    ### CHECK EVERY ELEMENT ###
    for i in range(len(check_dictonary)):
        if check_dictonary[i]["has_wooden_leg"] == True and check_dictonary[i]["gold"] > 15:
            ### PUT TO THE NEW EMPTY LIST ###
            rich_pirates_with_wood_leg.append(check_dictonary[i]["Name"])

    return rich_pirates_with_wood_leg

### CALL THE FUNCTION ###
pirates_check(pirates)
