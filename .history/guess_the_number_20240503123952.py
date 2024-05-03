import random
import time
number=random.randint(1,200)
n=int(input("enter In how many picks you can make the correct guess: "))
def gamer_intro():
    name=input(print("May i know your name?"))
    print(f"hey {name} nice to see you here")
    time.sleep(0.10)
    print("Lets play a game of fun with you"+name+"!!")
def guess():
        guess=input(("enter your guess:"))
        if guess>0 and guess<200:
            guess_num=0
            if guess_num<n:
                guess_num+=1
                if guess>number:
                    print("Your guess is large! Make a small all")
                if guess<number:
                    print("your guess is small! Make a large call")
                if guess!=number:
                    print(f"Try again, You left with{n-guess_num}attempts")        
            if guess==number:
                break    



    