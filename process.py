file =  open("../data/lorem.txt")


# print(file.readline())

lorem_dict = {}
print(lorem_dict)



for word in file.read():
    print(word)
    # for word in line:
    #     # print(word)
    #     if word in lorem_dict:
    #         lorem_dict[word]+=1
    #     else:
    #         lorem_dict[word] = 1

print(lorem_dict)
print(type(file))

