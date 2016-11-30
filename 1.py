# Create a function that takes a list as a parameter,
# and returns a new list with all its element's values doubled.
# It should raise an error if the parameter is not a list.

list_for_function =[2,3,4,5,10]

def list_doubled(list_simple):
    if isinstance(list_simple, list):
        for i in range(len(list_simple)):
            list_simple[i] *= 2
        return list_simple
    else:
        raise TypeError("it's not a list")

list_doubled(list_for_function)
list_doubled(5)
