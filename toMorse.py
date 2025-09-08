import json
# Code converts english text to morse code
eng = input("please enter some text: \n")
morse = ""
eng = eng.lower()

with open("eng_2_norse.json","r") as eng2:
    eng2 = json.load(eng2)
    for word in eng:
        word = word + " "
        for letter in word:            
            morse  = morse + eng2[letter]

print(morse)