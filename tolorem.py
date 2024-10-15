# file = open("lorem.txt")
# print(file.read())
import json

input = "1WASHINGTON 23 Sen.999 Dianne994321 Feinstein, D-Calif., a vocal advocate of gun control measures who was known for trying to find common  ground with Republicans during her three decades in the Senate, has died, her office confirmed on Friday She was  "

with open("eng_2_lorem.json","r") as eng2:
    eng2lorem = json.load(eng2)
    # print(eng2lorem)
   
    # print(eng2.readlines())

print(eng2lorem)
print(type(eng2lorem))

print(input)

english_word = input.split()
print(english_word)
# # 
output_str = ""

for item in english_word:
    if item in eng2lorem:
        output_str = output_str + eng2lorem[item] + " "
    
print(output_str)

# f = open("english_words.txt","x")

