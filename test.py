import json
import random

# functions from process.py

'''
def random_lorem():
    n = random.randint(0,15040)
    lorem = lorem_dict[n]
    print(lorem)
    return lorem
    
''' 
def random_lorem():
    with open("eng_2_lorem.json","r") as eng2:
        eng2lorem = json.load(eng2)
    length = len(eng2lorem)
#    print(length)
    n = random.randint(0,length)
#    print(type(eng2))

    key_number = random.randint(0,5000)
    for key in eng2lorem:
        key_number += 1
        while key_number <= 
        
        
    
   

def latinify(x_word):
    latin_endings = ["i", "isti", "it", "imus", "istis", "erunt","eram","eras","erat", "eramus", "eratis", "erant","ae","am","arum","is","as","us","o","um","em","e","orum","a","ibus","es","ium","jbus","ia","ui","uum","ei","erum","ebus"]
    n = random.randint(0,33)
    latin = x_word + latin_endings[n]

    # print(latin)
    return latin
    

# Begin code
input = input("enter some text \n")

with open("eng_2_lorem.json","r") as eng2:
    eng2lorem = json.load(eng2)


english_word = input.split()

output_str = ""

for item in english_word:
    if item in eng2lorem:
        output_str = output_str + eng2lorem[item] + " "
    else:
        output_str = output_str + latinify(item) + " "
    
print(output_str)

''' code not working
print(" Random Lorem:")
random_lorem()
'''
random_lorem()
