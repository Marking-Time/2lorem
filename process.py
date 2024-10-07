fin_list = []

with open("../data/en-freq-10k.txt", "r") as file:
    for contents in file:
        eng_fin = []
        contents = file.readline()
        # print(contents)
        y_position = contents.find(",")
        # print(y_position)
        eng_fin.append(contents[ :y_position])
        # print(eng_fin)
        fin_list.append(eng_fin)



lorem_dict = []
# print(lorem_dict)

words = open("../data/lorem.txt").readline().split()

for word in words:
    if word.endswith('.'):
        word = word[:-1]
    elif word.endswith(','):
        word = word[:-1]
    elif word.endswith('?'):
        word = word[:-1] 
    elif word.endswith('!'):
        word = word[:-1]
    # print(word) #<===============================================

    if word not in lorem_dict:
        lorem_dict.append(word)



print("<----------------------------------------------------------------------------------------------->")

print("                                           LOREM")

print("<----------------------------------------------------------------------------------------------->")
# <----------------------------------------------------------------------------------------------->


print(lorem_dict)



eng_list = []


print("=================================== print eng_Words")

# exp = "([A-Za-z])\w+"



eng_fin = []


print("CENTENTs")


print(fin_list)

l = open("lorem_list.txt", "w")


e = open("eng_list.txt", "w")
