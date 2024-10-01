file =  open("../data/lorem.txt")


# print(file.readline())

lorem_dict = {}
print(lorem_dict)

words = open("../data/lorem.txt").read().split()

for word in words:
    if word.endswith('.'):
        word = word[:-1]
    elif word.endswith(','):
        word = word[:-1]
    elif word.endswith('?'):
        word = word[:-1] 
    elif word.endswith('!'):
        word = word[:-1]
    print(word)

    if word in lorem_dict:
        lorem_dict[word]+=1
    else:
        lorem_dict[word] = 1
    # for word in line:
        # # print(word)
        # if word in lorem_dict:
        #     lorem_dict[word]+=1
        # else:
        #     lorem_dict[word] = 1

print(lorem_dict)
print(len(lorem_dict))
# print(type(file))

