import random

top_of_range = input("Enter a Maximum Range Number: ") #This creates a var. which will be he highest number the user can guess, decided by the user itself.
guesses = 0

if top_of_range.isdigit(): #If the num is a digit, convert it into an integer
    top_of_range = int(top_of_range) #Digit to Integer conversion

    if top_of_range <= 0: #If the user enters 0 THEN; we dont use "" here because it is an INTEGER now (cause we converted it)
        print("Please enter a number larger than 0 next time!") #This gets printed telling the user to use values < 0.
        quit() #The program exits L.
else: 
    print("Please enter a number next time L") #This is printed for both conditions; if the input is NOT a digit and if the inserted digit is < 0
    quit() #The program exits L

random_number = random.randint(0, top_of_range) #This firstly, convets a random number into an integer then assigns it a value of min 0 and max top of range.

#Analyzing the users input
while True:
    guesses +=1
    user_guess = input("Make a guess: ") #Here the user tries to guess the random number by typing an input.
    if user_guess.isdigit(): #If the user guess/entered input is a digit like 2 THEN,
        user_guess = int(user_guess) #This digit is converted into an integer
    else:
        print("Please type a number number time!") #This asks the user to enter a number next time and THEN
        continue #Brings us back to Line 18 so we can enter another guess

    if user_guess == random_number: #If the User's Guess is correct/equal to the Random Number THEN,
        print("You got it correct! :)) Rider Status") #We print a status so the user feels happy :P
        break #This stops the loop if we get the number and Avoiding an infinite loop by adding break
    else:
        print("You got it wrong, better luck next time L Bozo Sir Shoaib") #We insult him if he gets it wrong XD
        if user_guess > random_number:
         print("You were above the number!")
        if user_guess < random_number:
         print("You were below the number!")

print("You got the number in " + str(guesses) + " Guesses")
    


#^Works by counting the number of times we reapeted loop beginning from Line 18; as this loop has a variable called guesses that increments each time the loop is executed
