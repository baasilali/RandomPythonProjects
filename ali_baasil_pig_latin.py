#Baasil Ali
#11 / 15 / 2022

#This program will accept any sentence as input and will
#convert each word of that sentence into "Pig Latin"

import string

def to_pig(word):

    if word[0].lower() in 'aeiou':
        return word.lower() + 'way'
    else:
        ind = 0
        upper = False

        if word[0].isupper():
            upper = True

        for i in word:
            if word.lower()[:2] == 'qu':
                ind = 2
            else:
                if i.lower() in 'aeiou' or (i.lower() == 'y' and word.index(i) != 0):
                    ind = word.index(i)
                    break

        word = word.lower()[ind:] + word.lower()[:ind] + 'ay'

        if upper:
            word = word.capitalize()
        
        return word

finished = False

while not finished:

    user = str(input('Enter a traditional english sentence: '))

    if len(user):
        result = ''
        words = user.split()

        for word in words:
            result += to_pig(word)+' '
        print(result)

    else:
        finished = True
        

           
           






    



