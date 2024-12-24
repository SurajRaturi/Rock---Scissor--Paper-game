#rock paper scisor
import random
def game():

    while True: # for condition true it will run
            
        def design():# used to design programm layout 
            for m in range(0,56):
                print("-",end="")

        print("ROCK -  PAPER - SCISSOR ")# program title 
        print()
        print()
        design()
        print()
        print("Rule Of The Game : ")#rules
        design()
        print()
        print("1.)You have three choices Rock , Paper and Scissors . \n2.)Press 1 for  Rock which  beats scissor. \n3.)Press 2 for Paper which  beats Rock \n4.)Press 3 for Scissor which  beats paper .")
        print()
        design()
        print()
        print()
        n=int(input("Enter your choice : -  "))#user choice 
        a=["rock","scissor","paper"]
        c=random.choice(a)#Random  choice of program
        print("Thinking....")
        design()
        print()
        #conditions
        if n==1 and c=="rock":
            print(c)
            design()
            print()
            print("Game tied , try again" )
        elif n==1 and c=="paper":
            print(c)
            design()
            print()
            print("You win! " )
        elif n==1 and c=="scissor":
            print(c)
            design()
            print()
            print("You Win!")
        elif n==2 and c=="rock":
            print(c)
            design()
            print()
            print("You win!")
        elif n==2 and c=="paper":
            print(c)
            design()
            print()
            print("Game tied , try again ")
        elif n==2 and c=="scissor":
            print(c)
            design()
            print()
            print("You loss !")
        elif n==3 and c=="rock":
            print(c)
            design()
            print()
            print("You loss!")
        elif n==3 and c=="paper":
            print(c)
            design()
            print()
            print("You win!")
        elif n==3 and c=="scissor":
            print(c)
            design()
            print()
            print("Game tied ,try again")
        else:
            print("Invalid Input! Please enter correct input from given option . ")
        
        print()
        print()        
        b=int(input("Press 1 to play again. \nPress 2 for exit "))
        if b==1:#condition to play again or exit
            print()
            continue  
        elif b==2:
            print("Exit...")
            break            #exit the loop from here if b==2
game()




