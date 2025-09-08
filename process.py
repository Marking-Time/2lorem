import random 
import json


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
   
#    word = tuple(word)

    if word not in lorem_dict:
        # word_to_tuple = tuple(word)
        lorem_dict.append(word)


'''
print("<----------------------------------------------------------------------------------------------->")

print("                                           LOREM")

print("<----------------------------------------------------------------------------------------------->")
# <----------------------------------------------------------------------------------------------->
'''

#print(lorem_dict)



eng_list = []


#print("=================================== print eng_Words")

# exp = "([A-Za-z])\w+"



eng_fin = []


#print("CONTENTs")


#print(fin_list)

# l = open("lorem_list.txt", "w")


# e = open("eng_list.txt", "w")


# print("<----------------------------------------------------------------------------------------->")

# print("                                           write lorem_list & fin_list to file")

# print("<----------------------------------------------------------------------------------------->")

# for item in lorem_dict:
#     # item = tuple(item)
#     l.write(item)

# l.close

# for item in fin_list:
    
#     item[0] = item[0] + ",\n"
#     e.write(item[0])

# e.close

'''
print("<------------------------------------------------------------------------------------------->")

print("                                           Create eng to lorem dict")

print("<----------------------------------------------------------------------------------------------->")

# ====================================================
#                 extend lorem_dict to create range for english list
# ====================================================
'''

while len(lorem_dict) < 9764:   
    lorem_dict.extend(lorem_dict)



eng2Lorem_dict = {}
n = 0

for item in fin_list:  #<================= code i'm wirking on
    # print(item)
    item = item[0]
    eng2Lorem_dict[item] = lorem_dict[n]
    n+=1
    
#print(eng2Lorem_dict)
#print(len(eng2Lorem_dict))


j_dump = json.dumps(eng2Lorem_dict)
with open("eng_2_lorem.json", "w") as json_write:
    json_write.write(j_dump)



# with open("eng2Lorem_dict.txt","w") as fool:
#     fool.write(str(eng2Lorem_dict))




def random_lorem():
    n = random.randint(0,15040)
    lorem = lorem_dict[n]
    print(lorem)
    return lorem

def latinify(x_word):
    latin_endings = ["i", "isti", "it", "imus", "istis", "erunt","eram","eras","erat", "eramus", "eratis", "erant","ae","am","arum","is","as","us","o","um","em","e","orum","a","ibus","es","ium","jbus","ia","ui","uum","ei","erum","ebus"]
    n = random.randint(0,33)
    latin = x_word + latin_endings[n]

    # print(latin)
    return latin






 

# print(eng2Lorem_dict)

# ====================================================

# print(lorem_dict)

# print(len(lorem_dict))



# print(len(lorem_dict))   

# print("len lorem_dict")
# print(len(lorem_dict))

# print("length of lorem_dict")
# print(len(lorem_dict))

#print("random lorem")
##random_lorem()

#print("latinify")
#latinify("mark")