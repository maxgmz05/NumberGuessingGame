from random import randint as rand

def game_manager():
    remaining_turns=0
    x=11
    sys_num=0
    while remaining_turns<1 or x>10:
        x=int(input("How hard do you want the game to be in the scale of 1-10?\n:"))
        if x>10:
            print("\nthe game can only handle up to a difficulty of 10")
        sys_num=rand(x,int(x**1.2))

        remaining_turns=int(x/2)
        if remaining_turns<1:
            print("\nEnter a Bigger number, the game can't be this easy")
    return(x,sys_num,remaining_turns)

def game(y,num,rem):
    while rem>0:
        guess=int(input("Enter your guess:"))
        rem=rem-1
        if guess==num:
            return (True,rem)
        elif guess<umb:
            print("\nGuess Bigger")
        elif guess>num:
            print("\nGuess Smaller")
    else:
        return(False,rem)

x,y,z=game_manager()
state,remaining_turns=game(x,y,z)

if state:
    print("You won with",remaining_turns,"remaining")
else:
    print("No more turns left, You lost")
    