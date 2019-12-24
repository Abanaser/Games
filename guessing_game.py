from random import *
def intro():
    """ intro function to describe the rules, and how to play the game"""
    print("Hello my friend, we will play a guessing game can you beat me?")
    print("Here are the rules,")
    print("1: We choose a number between 1 and a 100 and keep it in our mind.")
    print("2: We will try to guess eachother's number in the least amount of guesses.")
    print("3: You will first try to guess my number, then I will try to guess yours.")
    print("Let us see who guesses the correct number in the least amount of guesses!.")
    print("---------------------------------------------------------------------")
def computerGuess():
    """A function where the computer is trying to guess your number using binary search approach"""
    print("Choose a number betweeen 1  and 100")
    print("Your answer should be C if my guess is correct, B if your number is bigger, S if your number is smaller: ");
    guess = 50;
    upperLimit=100;
    lowerLimit=1;
    guessCount1 = 0;
    while True:
        guessCount1 = guessCount1 + 1;
        print("I guess: ", guess);
        ans = input("Answer ""C"", ""B"", or ""S"": ");
        if guessCount1 > 7:
            print("I think I have already guessed your number correctly!")
            print("You don't want to admit that?");
            return -1;
            break;
        if ans == "b" or ans == "B":
            lowerLimit = guess;
            guess = int((guess + upperLimit+1)/2)
            continue;
        elif ans == "s" or ans == "S":
            upperLimit = guess;
            guess = int((guess + lowerLimit)/2)
            continue;
        elif ans == "c" or ans == "C":
            print("I got it right!")
            print("I've guessed your number in: ", guessCount1," guesses!")
            break;
        else:
            print("This is not a valid answer.")
            guessCount1 = guessCount1 - 1;
            continue;
    return guessCount1;
def humanGuess():
    """ Taking inputs from the user to guess the computer's number """
    guessCount2 = 0;
    Number = randint(1,100);
    print("Ok, now I will think of a number in my head that is between 1 and 100 and you will try to guess it!")
    print("I wonder how many guesses will it take you?")
    print("Can you guess my number?!")
    print("With every guess I will tell you if your guess is larger, smaller, or actually correct!")
    while True:
        guessCount2 = guessCount2 + 1
        try:
            ans = int(input("Guess a number: "))
        except ValueError:
            guessCount2 = guessCount2 - 1
            print();
            print("Your guess must be an integer")
            continue
        if ans > Number:
            print("My number is smaller than", ans);
            continue;
        if ans < Number:
            print("My number is larger than", ans);
            continue;
        if ans == Number:
            print();
            print("You got it right! You have guessed my number in ",guessCount2,"guesses!");
            break;
    return guessCount2;
def whoWins(guessCount1, guessCount2):
    """ Chechk who did the guess in least steps! to determine the winner """
    if guessCount1<guessCount2:
        print("I win!, I have guessed your number in ", guessCount1,"guesses!");
        print("While you guessed my number in ", guessCount2,"guesses!");
    elif guessCount1>guessCount2:
        print("Wow, you won! You have guessed my number in ", guessCount2,"guesses!");
        print("While I guessed your number in ",guessCount1, "guesses.")
    else:
        print("It is a draw! We both gusses our numbers in: ", guessCount1)
        print("I think that means that we are both good at the game! ... or both bad.?")
def playAgain():
    """Make the calls of other functions to play another game"""
    print("Do you want to play again? (y,n)")
    while True:
        answer = input();
        if answer == "y":
            break;
        elif answer == "n":
            break;
        else:
            continue;
            print("This is not a vaild answser, please answer with (y) if you want to play again, and (n) if you don't want to play again")
    if answer =="y":
        print("Ok! let us see who wins this time.")
        return "y";
    elif answer =="n":
        print("Thanks for playing with me. That was fun!")
        return "n";




intro();
while True:
    input("Press Enter if you are ready ");
    print();
    guessCount2 = humanGuess();
    print("-----------------------------------------------------------")
    print();
    print("Ok you have guessed my number correctly. Now it is my turn to guess yours.")
    print();
    input("Press Enter if you are ready ");
    print();
    guessCount1 = computerGuess();
    print("---------------------------------------------------------------------------------")
    print();
    if guessCount1 == -1:
        print("I win!, because you didn't want to admit that I guessed it right!");
        break;
    whoWins(guessCount1, guessCount2);
    print();
    answer = playAgain();
    if answer == "y":
        continue
    elif answer == "n":
        break
