import re

file =  open("../data/en-freq-10k.txt")

# print(type(file))

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
    # else:
    #     lorem_dict.append(word)
    # for word in line:
        # # print(word)
        # if word in lorem_dict:
        #     lorem_dict[word]+=1
        # else:
        #     lorem_dict[word] = 1

print(lorem_dict)
# print(len(lorem_dict))
# print(type(file))

# =================================================================

# def getValue(word):
#     return word[1]

# print(sorted(lorem_dict.items(), key=getValue))

# lorem_dict2 = sorted(lorem_dict.items(), key=getValue)
# print(lorem_dict2)  

# print(type(lorem_dict2))
# #
# en_word_freq = []

# for item in file:
#     en_word_freq.append(item[0])

# print(en_word_freq)
# print(file)
# print(type(file))

# for item in file:
#     print(item)

eng_list = []

# print(file)

# for line in file:
#     x = re.search("([A-Za-z])\w+",line)
#     eng_list.append(x)
#     print(x.span())

    
# print(eng_list)

print("================================")
print(type(file))

# ==================================================================================


# for line in file:
#     print(file.readline())
#     eng_list.append(file.readline())

# print(eng_list)
# eng_word = []

# for element in eng_list:
#         x = re.search(r"^[a-z]+\w",element)
#         if x:
#             eng_word.append(x.string)

# print(eng_word)


eng_words = []
print(file)
for line in file:
    # print(file.readline())
    x = file.readline()
    eng_words.append(x)


print("=================================== print eng_Words")

exp = "([A-Za-z])\w+"

print(eng_words)

eng_fin = []

for string in eng_words:
    if type(string) == None:
        print()
    else:   
        x = re.search(r"([A-Za-z])\w+",string)
        x = str(x)
        # eng_fin.append(x)
        x = x.split()
        print(x)

print(eng_fin)