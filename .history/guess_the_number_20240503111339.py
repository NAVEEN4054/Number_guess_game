import random
import time
number=random.randint(1,200)
n=int(input("enter In how many picks you guess the correct number: "))
def gamer_intro():
    name=input(print("May i know your name:"))
    time.sleep(.10)
    print(f"hey {name} nice to see you here")
    time.sleep(0.10)
    print("Lets play a game of fun with you"+name+"!!")
def guess(name):
    try:
        no_of_guesses=0
        if no_of_guesses<n:
            no_of_guesses+=1
            temp=int(input("enter your guess:"))
            if temp>0 and temp<200:
                if temp>number:
                    print("your assumption too large! Make a smaller call")
                if temp<number:
                    print("your assumption too small! make a larger call")
                if temp!=number:
                    time.sleep(.5)
                    print("try again you are left with only"+(n-1)+"attempts")
                else:
                    print("congratulations!! you make a correct guess")   
            else:
                print("hey man your number is not in range")
        else:
            print(f"{name} make a valid count of picks")
    except:
        print("I think you dont make the guess yet")
while True:
    gamer_intro()
    guess()
    play_again=input(print("Do you want to play again"))
       



    