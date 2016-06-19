# Exercise 1. Count letters in the string (ex. number of letters A)

string = 'Python is a high-level programming language, with applications in numerous areas, including web programming, scripting, scientific computing, and artificial intelligence.'
letter = 't'

system_counter = string.count(letter)


def count_letters(l, s):
    """ Returns the number of occurrences of pointed letter L in string S
    """
    c = 0
    for i in s:
        if i == l:
            c += 1
    return c


letters = count_letters(letter, string)
if system_counter == letters:
    print("Count of letter '", letter, "' = ", letters)
else:
    print("Error: smth wrong")
