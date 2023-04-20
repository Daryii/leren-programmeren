from functies import *

# test 1: getNumberOfCharacters
if getNumberOfCharacters('aap') == 3:
    print("Test geslaagd")
else:
    print("Deze test is niet geslaagd")

# schrijf zelf nog wat extra testen voor getNumberOfCharacters
if getNumberOfCharacters('*#*a') == 1:
    print("Test geslaagd")
else:
    print("Deze test is niet geslaagd")
    
# test 2: getNumberOfSentences
if getNumberOfSentences(getText('easy')) == 14:
    print("Test geslaagd")
else:
    print("Deze test is niet geslaagd")

# schrijf zelf nog een extra testen voor getNumberOfSentences (gebruik test.txt).
 
if getNumberOfSentences(getText('test_1')) == 15:
    print("Test geslaagd")
else:
    print("Deze test is niet geslaagd") 

# test 3: getNumberOfWords

print(getNumberOfWords(getText('difficult1.txt')))
if getNumberOfWords(getText('difficult1.txt')) == 82:
    print("Test geslaagd")
else:
    print("Deze test is niet geslaagd")

if getNumberOfWords(getText('easy1.txt')) == 11:
    print("Test geslaagd")
else:
    print("Deze test is niet geslaagd")

# schrijf zelf nog een extra testen voor getNumberOfWords (gebruik test.txt).

if getNumberOfWords(getText('difficult_1')) == 289:
    print("Test geslaagd")
else:
    print("Deze test is niet geslaagd")

if getNumberOfWords(getText('easy_1')) == 131:
    print("Test geslaagd")
else:
    print("Deze test is niet geslaagd")
