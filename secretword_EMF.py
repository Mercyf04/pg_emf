import random

number = random.randint(0,3)

words = ["DOG","TABLE","CHAIR","INTERNET"]
hint1=["animal","a flat surface","you sit in it","search anything"]
hint2=["opposite of cat","you do homeowrk on it","you push it in","parents call it the interweb"]

secretword = words[number]
guess = ""
counter = 1

while True:
    print("Guess the secret word")
    print("Type 'hint1', 'hint2', 'first letter', or 'give up' to reveal the answer.")
    guess = input().upper()
    
    if guess == secretword:
        print("You guessed it!")
        print("It took you " + str(counter) + " guesses.")
        break

    elif guess == "HINT1":
        print( hint1[number] )
        
    elif guess == "HINT2":
        print( hint2[number] )

    elif guess  == "FIRST LETTER":
        print( secretword[0] )

    elif guess == "GIVE UP":
        print("The secret word was " + secretword)
        print("You failed " + str(counter) + " times.")
        break

    else:
        counter +=1
        print("Guess again.")
