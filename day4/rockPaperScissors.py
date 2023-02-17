# randomisation and python lists
# mersenne twister
# lists..... fruits=["cherry", "apple", "pear"]
# print(fruits[1]) = apple
# print(fruits[-1]) = pear
# you can alter the list as well. and add items as well, using append, extend....read documentation for more
# nested lists

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen[1][1])
# kale
import random
choice=int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors."))
rock='''  
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
    _______
---'   ____)____
          ______)
         _______)
         _______)
---.__________)
'''
scissors='''
    _______
---'   ____)____
          ______)
      __________)
      (____)
---.__(___)
'''
if choice==0:
    computer=random.randint(0, 2)
    print(rock)
    print("Computer chose:")
    if computer==0:
        print(rock)
        print("It's a Draw")
    elif computer==1:
        print(paper)
        print("You Won")
    elif computer==2:
        print(scissors)   
        print("You Lose")
if choice==1:
    computer=random.randint(0, 2)
    print(paper)
    print("Computer chose:")
    if computer==0:
        print(rock)
        print("You Won")
    elif computer==1:
        print(paper)
        print("It's a Draw")
    elif computer==2:
        print(scissors)   
        print("You Won")
if choice==2:
    computer=random.randint(0, 2)
    print(scissors)
    print("Computer chose:")
    if computer==0:
        print(rock)
        print("You Won")
    elif computer==1:
        print(paper)
        print("You Lose")
    elif computer==2:
        print(scissors)   
        print("It's a Draw") 
elif choice>=3 or choice< 0:
    print("You Dumb Fuck, Wrong Input")

# Solve this code by using the relation between 0, 1 and 2 inputs and their actions associated