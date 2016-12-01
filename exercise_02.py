# Create a function that takes a filename as string parameter,
# and counts the occurances of the letter "a", and returns it as a number.
# It should not break if the file does not exist, just return 0.

def count_a_in_text_file(file_name):
    try:
        ### OPEN THE FILE ###
        f = open(file_name)
        t = f.readlines()
        number_of_a = 0
        ### COUNT "A" ###
        for word in range(len(t)):
            for char in t[word]:
                if char == "a":
                    number_of_a +=1
        return number_of_a
    ### NOT EXIST FILE ###
    except FileNotFoundError:
        return 0
