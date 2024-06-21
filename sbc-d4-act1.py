from random import randint # nag import kog function nga randint from random module

user = int(input("Enter 0 for 'hayang' or 1 for 'kulob': ")) # it will ask the user to enter 0 or 1
player = [user, randint(0, 1), randint(0, 1)] #nag create kog list with 3 elements nga nag hold ug value which is si 0 and 1
choose = ["hayang", "kulob"] # naghimo kog list with variable name "choose" nga naay sulod nga 2 string element

#nag create kog variable name "results" with dictionary
# 011 ,100 etc. is tuple na nga serve as key sa dictionary which is si hayang or kulob
results = {
    (0, 1, 1): "Congratulations! You Win!",  # If player chooses "hayang" and computer choices are "kulob", "kulob"
    (1, 0, 0): "you win",  # If player chooses "kulob" and computer choices are "hayang", "hayang"
    (1, 0, 1): "Computer2 win",  # If player chooses "kulob" and computer choices are "hayang", "kulob"
    (0, 1, 0): "c2 win",  # If player chooses "hayang" and computer choices are "kulob", "hayang"
    (1, 1, 0): "Computer3 win",  # If player chooses "kulob" and computer choices are "kulob", "hayang"
    (0, 0, 1): "c3 win"  # If player chooses "hayang" and computer choices are "hayang", "kulob"
}
print(f"P1: {choose[player[0]]}\nC2: {choose[player[1]]}\nC3: {choose[player[2]]}") # mo print ni sa choice sa player
#if ang user ray nakalahi mo print ang "Congratulations! You Win!"
#if ang computer2 ray nakalahi mo print ang "C2 Win!"
#if ang computer3 ray nakalahi mo print ang "C3 Win!"
print(results.get(tuple(player), "Draw!,Try Again")) # mo print ni if wala sa results (dictionary)ang gipangita
