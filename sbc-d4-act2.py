from random import randint # nag import kog function nga randint from random module

user_bet_num = list(map(int, input("Enter your bet (3 digits): "))) #naghimo kog variable nga modawat sa eh enter ni user with map function para ma convert to list
print("Your Bet is:", *user_bet_num) # eh print diri and gi enter nga bet number sa user

lotto_result = [randint(5, 7) for _ in range(3)] #mag auto generate ni ug lotto_result gamit ang randint nga function nga gi import in range 3 ra
print("The winning number is:", *lotto_result)#  mo print ni diri sa lotto_result
if user_bet_num == lotto_result: #diri, eh check if same ba sa  lotto result ang gi bet ni user
    print("You Win!") # if true, mo print dayon ni
elif sorted(user_bet_num) == sorted(lotto_result): #diri gi sort kung ang mga gi-bet nga number same sa mga winning numbers in any order
    print("You Partially Win!") # if true nga naay ni parehas sa winning number,mo print ni
else:
    print("You Lose!") # if false ang statement, mo print ni,kung wala gyud bisag isa nga sakto
