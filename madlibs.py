# quote = 'Let it be, let it be, let it be'
#
# result = quote.find('let it')
# print("Substring 'let it':", result)
#
# result = quote.find('small')
# print("Substring 'small ':", result)
#
# song = 'Let it be, let it be, let it be, let it be'
#
# '''only two occurences of 'let' is replaced'''
# print(song.replace('let', "don't let", 2))

madlib = "The noun and then the verb and then the adjective and a color and a animal."

def user_input(prompt):
    user_input = input(prompt)
    return user_input

if madlib.find('noun') != -1:
    # input_item = user_input("Input noun: ")
    madlib = (madlib.replace('noun', input("Enter a noun: "), 1))

if madlib.find('verb') != -1:
    madlib = (madlib.replace('verb', input("Enter a verb: "), 1))

if madlib.find('adjective') != -1:
    madlib = (madlib.replace('adjective', input("Enter a adjective: "), 1))

if madlib.find('color') != -1:
    madlib = (madlib.replace('color', input("Enter a color: "), 1))

if madlib.find('animal') != -1:
    madlib = (madlib.replace('animal', input("Enter a animal: "), 1))
print(madlib)
