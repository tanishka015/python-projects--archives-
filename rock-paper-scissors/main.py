import random
#generate a random no 
comp=random.randint(1,3)
#print the instructions and rule
print('\n-----ROCK PAPER SCISSORS-----\n')
print('''Rules:
         enter a number between 1 to 3
         1 stands for rock
         2 Stands for paper
         3 stands for scissors\n''')

#take user input 
user=int(input("ENTER YOUR ELEMENT NUMBER: "))

#apply conditions to compare

if comp==1 and user==1:
    print("booth choose rock\nit`s a tie!\nplay again!")
elif comp==1 and user==2:
    print("\npaper wraped the rock\n user wins!")  
elif comp==1 and user==3:
    print("\nrock broke the scissors\n computer wins!")  
elif comp==2 and user==1:
    print("\npaper wraped the rock\n computer wins!")  
elif comp==2 and user==2:
    print("\nboth choose the paper\n it`s a tie!\nplay again!")  
elif comp==2 and user==3:
    print("\nscissors tored the paper apart\n user wins!")  
elif comp==3 and user==1:
    print("\nrock broke the scissors\n user wins!")
elif comp==3 and user==2:
    print("\nscissors tored the paper apart\n computer wins!")  
elif comp==3 and user==3:
    print("\nbooth choose the scissors\nit`s a tie!\nplay again!")  
    
    
#end the game
print("-----THANK YOU -----")
