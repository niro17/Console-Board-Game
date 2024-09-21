#Interface----------------------------------------------------------------------------------------------------------
name = input("What is your name:")

print("-"*100)
print()
print(f"                              Hi *{name}* Welcome to the BoardGame :)")

#Table interface----------------------------------------------------------------------------------------
top_left_corner = "\u2554"
top_right_corner = "\u2557"
horizontal = "\u2550"
vertical = "\u2551"
bottom_left_corner = "\u255A"
bottom_right_corner = "\u255D"

import random
import datetime

run="y"

while run== "y":
    
#Variables----------------------------------------------------------------------------------------------
    comp_pos = 0
    user_pos = 0
    dice = 0
    comp_pawn = "X"
    user_pawn = "X"
    black_hole = "O"
    num_list = [1, 2, 3, 4, 5, 6]
    user = False
    computer = False
    move = 0
    user_tot = 0
    comp_tot = 0 
    user_hits = 0 
    comp_hits = 0
    
    
    pos_list=[]
    
#Main loop start of program------------------------------------------------------------------------------
    while True: #While true means makes the loop infinite
        if user != True: #Before allowed to start
            print("-"*100)
    

#Users turn----------------------------------------------------------------------------------------------
            print()
            dice = (random.sample(num_list, 1))
            roll=input("Your turn - Press Enter to roll")
            dice = (dice[0])#This shows the values in a list as a interger.
            print("You have rolled",dice,end=" ")
            user_tot = user_tot + move
            if(dice == 6):

                print(", Ready to move")
                print("-"*50)
                user = True
                roll=input("Press Enter to roll again")
                dice = (random.sample(num_list, 1))
                dice = (dice[0])
                print("You have rolled",dice)
            else:
                print("You cannot start yet")
                
#Computers turn-------------------------------------------------------------------------------------------
        if computer != True:

            print()
            print("Computers turn:")

            dice = (random.sample(num_list, 1))
            dice = (dice[0])#This shows the values in a list as a interger.
            print("Computer rolled",dice,end=" ")
            comp_tot = comp_tot + move
            
            if(dice == 6):
                print(", Computer ready to move")
                print("-"*50)
                computer = True
                dice = (random.sample(num_list, 1))
                dice = (dice[0])
                print("Computer has rolled",dice)
            else:
                print("Computer cannot start yet")
                
#After 6 is been hit---------------------------------------------------------------------------------------
#User
        if user == True:
            print()
            print("Users turn:")
            roll = input("Press Enter to Roll the Dice")

            dice = (random.sample(num_list, 1))
            dice = (dice[0])#This shows the values in a list as a interger.
            
            print("You rolled",dice ,"and Current location is",user_pos)
            move = (dice//2) #This is floor division which shows how many 2s are in each value which is rolled by the dice.
            user_pos = user_pos + move

            user_tot = user_tot + move
            
#User Black hole-------------------------------------------------------------------------------------------
        if user_pos==7 or user_pos==14:
            print("You hit a black hole, move back to square 1")
            user_pos=1

            user_hits = user_hits + 1


#Computer--------------------------------------------------------------------------------------------------
        if computer == True:
            print()
            print("Computers turn:")

            dice = (random.sample(num_list, 1))
            dice = (dice[0])#This shows the values in a list as a interger.
            print("Computer rolled",dice ,"and Current location is",comp_pos)
            move = (dice//2)
            comp_pos = comp_pos + move

            comp_tot = comp_tot + move
#Computer Black hole---------------------------------------------------------------------------------------
        if comp_pos==7 or comp_pos==14:
            print("Computer hit a black hole, move back to square 1")
            comp_pos=1

            comp_hits = comp_hits + 1

   
#User table interface--------------------------------------------------------------------------------------
        print()
        if user==True:
            
            for i in range(1,11):
                print(" ",i," ",end="")
            for i in range(11,21):
                print(i," ",end=" ",)

            print()
            pos_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
            pawn="   "
            print((top_left_corner+horizontal*3+top_right_corner)*20)
            for i in pos_list[0:6]:
                if user_pos == i:
                    pawn=" X "
                print((vertical+pawn+vertical),end="")
                pawn="   "
            print((vertical+" O "+vertical),end="")
            for i in pos_list[7:13]:
                if user_pos == i:
                    pawn=" X "
                print((vertical+pawn+vertical),end="")
                pawn="   "
            print((vertical+" O "+vertical),end="")
            for i in pos_list[14:20]:
                if user_pos == i:
                    pawn=" X "
                print((vertical+pawn+vertical),end="")
                pawn="   "
            print()
            print((bottom_left_corner+horizontal*3+bottom_right_corner)*20)

        elif user==False:
            for i in range(1,11):
                print(" ",i," ",end="")
            for i in range(11,21):
                print(i," ",end=" ",)

            print()
            pos_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
            pawn="   "
            print((top_left_corner+horizontal*3+top_right_corner)*20)
            for i in pos_list[0:6]:
                print((vertical+pawn+vertical),end="")
            print((vertical+" O "+vertical),end="")
            for i in pos_list[7:13]:
                print((vertical+pawn+vertical),end="")
            print((vertical+" O "+vertical),end="")
            for i in pos_list[14:20]:
                print((vertical+pawn+vertical),end="")
            print()
            print((bottom_left_corner+horizontal*3+bottom_right_corner)*20)

#Computer table interface----------------------------------------------------------------------------------
        if computer==True:
            print()
            print((top_left_corner+horizontal*3+top_right_corner)*20)
            for i in pos_list[0:6]:
                if comp_pos == i:
                    pawn=" X "
                print((vertical+pawn+vertical),end="")
                pawn="   "
            print((vertical+" O "+vertical),end="")
            for i in pos_list[7:13]:
                if comp_pos == i:
                    pawn=" X "
                print((vertical+pawn+vertical),end="")
                pawn="   "
            print((vertical+" O "+vertical),end="")
            for i in pos_list[14:20]:
                if comp_pos == i:
                    pawn=" X "
                print((vertical+pawn+vertical),end="")
                pawn="   "
            print()
            print((bottom_left_corner+horizontal*3+bottom_right_corner)*20)


        elif computer==False:

            print()
            pos_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
            pawn="   "
            print((top_left_corner+horizontal*3+top_right_corner)*20)
            for i in pos_list[0:6]:
                print((vertical+pawn+vertical),end="")
            print((vertical+" O "+vertical),end="")
            for i in pos_list[7:13]:
                print((vertical+pawn+vertical),end="")
            print((vertical+" O "+vertical),end="")
            for i in pos_list[14:20]:
                print((vertical+pawn+vertical),end="")
            print()
            print((bottom_left_corner+horizontal*3+bottom_right_corner)*20)

#Checks whether win or lost--------------------------------------------------------------------------------
        if user_pos >= 20:
            print()
            print("You Won the game")
            win = "User"
            print()
            break
        
        if comp_pos >= 20:
            print()
            print("You Lost the game")
            win = "Computer" 
            print()
            break
        
#File handling---------------------------------------------------------------------------------------------       
    date_time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M")
    file_name = f"{date_time}.txt"
    with open(file_name, 'w')as f:
        f.write(f"{win} won the game\n")
        f.write("User\n")
        f.write(f"Total moves =  {user_tot}\n") 
        f.write(f"Black hole hits = {user_hits}\n")
        f.write("\n")
        f.write("Computer\n")
        f.write(f"Total moves =  {comp_tot}\n") 
        f.write(f"Black hole hits = {comp_hits}\n")
        
#Asking for a choice to play another game------------------------------------------------------------------
    run = input("Do you want to play again ? (y/n) :").lower()
    while run!="y" and run!="n":                                                
        print("Invalid input")
        run=input("Do you want to play again ? (y/n) :").lower()
        print()


print("Thank you for playing")






