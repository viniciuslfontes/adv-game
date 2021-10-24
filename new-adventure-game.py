import time
import random

def print_pause(printMsg):
    print(printMsg)
    time.sleep(2)

def intro(car, rival):
    print_pause("The race is almost starting and you don't feel confident.")
    print_pause("That's because you know you haven't a great car.")
    print_pause("You're going to face " + rival + " in front row.")
    print_pause("Are you ready to race? Or do you want to sneak into garage?\n")
    
def Garage(car, rival):
    if "Ferrari" in car:
        print_pause("\nYou're already a Ferrari driver!")
    else:
        print_pause("\nThe red horse is here! You can fell it.")
        print_pause("\nYou see a red nose...")
        print_pause("\nIt's true, the Ferrari is there!")
        print_pause("\nLet's race.\n")
        car.append("Ferrari")
    decision(car, rival)

def race(car, rival):
    print_pause("\nYou're going to race.")
    print_pause("\nAnd is almost lights out when "
                "you look right and it's a " + rival + ".")
    print_pause("\nDamn! I have to start with this " + rival + " right side!")
    print_pause("\nIt's green flag and " + rival + " starts better!!!\n")
    if "Ferrari" not in car:
        print_pause("I can't beat them. Looks like I'm driving a turtle.\n")
    while True:
        choice2 = input("Do you wanna (1) race ou (2) leave?")
        if choice2 == "1":
            if "Ferrari" in car:
                print_pause("\nWhile the " + rival + " approachs first corner, "
                            "you trottle your Red Horse.")
                print_pause("\nYour car moves like a bolt "
                            "and you fell ready to win!")
                print_pause("\nThe " + rival + " gives you a look and spins!")
                print_pause("\nNow just go! You're ready to win!")
            else:
                print_pause("\nYou tried...")
                print_pause("but this car isn't fast enough for " + rival + ".")
                print_pause("\nYou're done. Game Over!\n")
            replay()
            break
        if choice2 == "2":
            print_pause("\nYou run for warm bed.")
            decision(car, rival)
            break
            
def decision(car, rival):
    print_pause("Press 1 to race.")
    print_pause("Press 2 to go into garage.")
    print_pause("So, what's your decision?")
    while True:
        choice1 = input("(Type 1 or 2.)\n")
        if choice1 == "1":
            race(car, rival)
            break
        elif choice1 == "2":
            Garage(car, rival)
            break

def replay():
    again = input("Let's race again? (y/n)").lower()
    if again == "y":
        print_pause("\nOk...\n")
        play()
    elif again == "n":
        print_pause("\nOk, have a nice day!\n")
    else:
        replay()

def play():
    car = []
    rival = random.choice(["RBR", "Mercedes"])
    intro(car, rival)
    decision(car, rival)

play()