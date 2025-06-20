import json

# eng  = "1WASHINGTON 23 Sen.999 Dianne994321 Feinstein, D-Calif., a vocal advocate of gun control measures who was known for trying to find common  ground with Republicans during her three decades in the Senate, has died, her office confirmed on Friday She was "
eng = input("please enter some text: \n")
morse = ""

eng = eng.lower()

print(eng)


with open("eng_2_norse.json","r") as eng2:
    eng2 = json.load(eng2)
    for word in eng:
        for letter in word:
            morse  = morse + eng2[letter]

print(morse)