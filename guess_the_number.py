import random
import time
number=random.randint(1,200)
n=int(input("enter In how many picks you can make the correct guess: "))
def gamer_intro():
    print("May i know your Name?")
    name=input()
    print(f"hey {name} nice to see you here")
    time.sleep(0.5)
    print(f"Lets play a game of fun with you {name} !!")
    time.sleep(0.5)
    print("START YOUR GUESS BUDDY")
def guess():
        guess_num=0
        while guess_num<n:
           guess=int(input(("GUESS:")))
           if guess>0 and guess<200:
              guess_num+=1
              if guess>number:
                    print("Your guess is large! Make a small call")
              if guess<number:
                    print("your guess is small! Make a large call")
              if guess!=number:
                    if n-guess_num!=0:
                          time.sleep(2)
                          print(f"Try again, You left with {n-guess_num} attempts")    
                    else:
                          time.sleep(0.5)
                          print("your lucky attempts are over")         
              if guess==number:
                    break
           else:
              
              print("your guess is not in range")  
              time.sleep(0.5)
              print("please enter number between 1 and 200")  
        if guess==number:
                    print("Congatulations! you make a correct guess")
        if guess!=number:
                    print(f"you make a wrong call in all attempts. My pick was {number}")
       
play_again="yes"
while play_again=="yes":
     gamer_intro()
     guess()
     play_again=input("Do you want to play again?")
     if play_again != "yes":
          continue
     else:
          break                         
                      




    