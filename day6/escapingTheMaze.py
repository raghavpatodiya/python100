# def my_function():
#     print("Hello")
#     print("Bye")
# my_function()

# while something_is_true:
#     do this 
#     then do this 
#     then do this



# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
  

  
# Try 1
# if right_is_clear():
#         turn_right()
#         while wall_in_front() != True:
#             move()    
#     elif front_is_clear():
#         move()
#     elif front_is_clear != True and right_is_clear!= True:
#         turn_left()
#         turn_left()
#         move()
#     else:
#         turn_right()
#         move()

#  Try 2
#  if right_is_clear():
#         turn_right()
#     if front_is_clear():
#         move()
#     if front_is_clear() != True and right_is_clear()!= True:
#         turn_left()
#         turn_left()
#         move()
    

# works
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def play():
#        if right_is_clear():
#             turn_right()
#             while wall_in_front() != True:
#                 move()    
#        elif front_is_clear():
#             move()
#        elif front_is_clear() != True and right_is_clear()!= True:
#             turn_right()
#             while wall_in_front() ==True:
#                 turn_right()
#        else:
#             turn_right()
#             move()
# while at_goal()!= True:
#     play()


#best case
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while front_is_clear():   
    move()
turn_left()
# in the above 3 lines we are basically changing the starting position of the reeborg
while at_goal()!= True:
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()