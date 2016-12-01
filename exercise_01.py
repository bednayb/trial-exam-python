# Create a function that takes a list as a parameter,
# and returns a new list with all its element's values doubled.
# It should raise an error if the parameter is not a list.


list_for_function =[2,3,4,5,10]

### FUNCTION ###
def list_doubled(list_simple):
    ### CHECK THE TYPE ###
    if isinstance(list_simple, list):
        ### DOUBLE EVERY ELEMENT ###
        for i in range(len(list_simple)):
            list_simple[i] *= 2
        return list_simple
    else:
        ### ERROR FOR NOT LIST ###
        raise TypeError("it's not a list")

### CALL THE FUNCTION ###
list_doubled(list_for_function)
list_doubled(5)
