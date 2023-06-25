import random #randomization

print("welcome to hangeman")
print("________")

WordDictionary = ["book" , "diamond" , "manage", "great"] #a list of words the imported random class would choose from

### choose a random word

random_word = random.choice(WordDictionary)  #.choice is the method that randomly selects a word from our list of words in WordDictionary

for x in random_word:
    print("_", end=" ")

def hangmanDisplay(wrong):   #FUNCTION TO DISPLAY THE HANGMAN WHEN YOU GET THE LETTER WRONG
    if (wrong == 0):
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong == 1):
        print("\n+---+")
        print(" O  |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong == 2):
        print("\n+---+")
        print(" O  |")
        print(" |  |")
        print("    |")
        print("   ===")
    elif(wrong == 3):
        print("\n+---+")
        print(" O  |")
        print("/|  |")
        print("    |")
        print("   ===")
    elif(wrong == 4):
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("    |")
        print("   ===")
    elif(wrong == 5):
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("/   |")
        print("   ===")
    elif(wrong == 6):
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("/ \ |")
        print("   ===")

def printword(guessedletter):     #this prints out the word any time the loop runs
    counter = 0
    rightletters = 0  #the amount of letters guessed correctly
    for char in random_word:
        if (char in guessedletter):
            print(random[counter], end=" ")
            rightletters +=1
        else:
            print("  " , end= " ")
            counter +=1
    return rightletters

def printlines():
    print("\r")
    for char in random_word:
        print("\u203E", end=" ")

lengthofwordtoguess = len(random_word)
amountoftimewrong = 0
currentguessindex = 0
currentlettersguessed= []
currentlettersright = 0

while(amountoftimewrong != 6 and currentlettersright != lengthofwordtoguess):
    print("\n letters gueseed so far ")
    for letter in currentlettersguessed:
        print(letter, end=" ")
        #### prompt the user for input
    letterguessed = input("\n please guess a letter ")


## user is right
if(random_word[currentguessindex] == letterguessed):
    hangmanDisplay(amountoftimewrong)
    ### print word
    currentguessindex+=1
    currentlettersguessed.append(letterguessed)
    currentlettersright = printword(currentlettersguessed)
    printlines()
    ### user is wrong
else:
    amountoftimewrong+=1
    currentlettersguessed.append(letterguessed)
    ### update the hangman drawing
    hangmanDisplay(amountoftimewrong)
    ###  print word
    currentlettersright = printword(currentlettersguessed)
    printlines()


print("game over loser")
