word = input()
vowels = 0
for i in word:
    letter = i.lower()
    if letter == "a" or letter == "e" or\
       letter == "i" or letter == "o" or\
       letter == "u":
        vowels == 5
        print ("True")
    else:
        print("False")
