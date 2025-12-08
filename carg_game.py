import random
import time


def card_random():
    global balance
    #so here what im going to do is to create a list that has thier own name and each name has level that  can take your card down base on your card that you get from list
    #but you will picking if you want
    cards = [
        #this all has a points
           #THIS IS CALLED STRAIGHT, 
            "A 1 B 2 C 3", "B 2 C 3 D 4", "C 3 D 4 E 5", "D 4 E 5 F 6",
            #this is called mythic nike
            "A 2 3 4 5", "2 3 4 5 6", "A 4 2 3", "4 3 2 A", "4 3 2 A",
            #this is called legend nike
            "4 3 2", "3 A 2", "2 4 A", "6 7 A", 
            #EpicNike
            "4 3",
            "3 3",
            "7 6 A",
            #warrior 
            "A9K3D2",
            "f7Qp12",
            "Z8M1x",
            "k2B9tR",
            "P4s7Wq",
            "m9L0H3",
            "T2vX8p",
            "q6N3yF",
            "R7kD1w",
            "b5P0uC",
            "H3z9Qe",
            "x1W4mT",
            "C8r2Jv",
            "n7S0gL",
            "V5yK3a",

            #O POINTS
            "jshsd", "jshss", "ashshga","shshss", "jsss", "skdddd", "sladhd", "ksddhddd", "lahdqd", "dajdhd", "sajdjd", "jdadad", "FJISAGYFA", "DAdhhd", "jdfyafd"
    ]

    STORE_VALUE_CARDS = {
        "straight_cards": ["A 1 B 2 C 3", "B 2 C 3 D 4", "C 3 D 4 E 5", "D 4 E 5 F 6"],
        "mythic_cards": ["A 2 3 4 5", "2 3 4 5 6", "A 4 2 3", "4 3 2 A", "4 3 2 A"],
        "legend_cards": ["4 3 2", "3 A 2", "2 4 A", "6 7 A"],
        "epic_cards": ["4 4", "3 3", "2 2", "A A"],
        "warrior": ["A9K3D2", "f7Qp12", "Z8M1x", "k2B9tR", "P4s7Wq", "m9L0H3", "T2vX8p", "q6N3yF", "R7kD1w", "b5P0uC", "H3z9Qe", "x1W4mT", "C8r2Jv", "n7S0gL", "V5yK3a"],
    }

    while balance > 0:
            get_random_value = random.choice(cards)
            print(get_random_value)

            if balance == 0:
                print("sorry you dont have enough balance to spin")
            
            if get_random_value in STORE_VALUE_CARDS["straight_cards"]:
                balance += 200
                print(f"straight and you got a: 200 points")
            elif get_random_value in STORE_VALUE_CARDS["mythic_cards"]:
                balance += 50
                print(f"mythic nikr and you got a: 10 points")
            elif get_random_value in STORE_VALUE_CARDS["legend_cards"]:
                balance += 20
                print(f"legend nike and you got a: 10 points")
            elif get_random_value in STORE_VALUE_CARDS["epic_cards"]:
                balance += 10
                print(f"epic nike and you got a: 10 points")
            elif get_random_value in STORE_VALUE_CARDS["warrior"]:
                balance += 1
                print(f"warriot and you got a: 1  balance")
            else:
                print(f"you got o points: your balance is {balance}")
            break
    print(f"your total balance is: {balance}")
           
balance = 50
def time_limit():
    global balance
    starting_games = input("do you wanna play card game? enter yes/no: ").lower()
    if starting_games == "yes":
        print("okay lets start!.. ")
        for  i in range(3, 0, -1):
            print(i)
            time.sleep(1)
        start_game()
    elif starting_games == "no":
        print("its fine to not play, play it in another time or day, good luck!..")
        quit
    else:
        print("please enter valid input")

def start_game():
    global balance
    your_card = input("enter start: ").lower()
    if your_card == "start":
        while True:
                try:
                    #every spin  was 5 10 200 300 or etc
                    #bet
                    bet = [1, 2, 3, 4, 5, 6, 7, 8 , 9 ,10]
                    print("you can chose only 1 - 10 only in bet")
                    value_of_your_spin = int(input("place your bet: "))
                    
                    if value_of_your_spin not in bet:
                        print("sorry you just only chose your bet between 1 - 10")
                    elif value_of_your_spin in bet:
                        if value_of_your_spin == bet[0]:
                            balance -= 1
                        elif value_of_your_spin == bet[1]:
                            balance -=2
                        elif value_of_your_spin == bet[2]:
                            balance -= 3
                        elif value_of_your_spin == bet[3]:
                            balance -= 4
                        elif value_of_your_spin == bet[4]:
                            balance -= 5
                        elif value_of_your_spin == bet[5]:
                            balance -= 6
                        elif value_of_your_spin == bet[6]:
                            balance -= 7
                        elif value_of_your_spin == bet[7]:
                            balance -= 8
                        elif value_of_your_spin == bet[8]:
                            balance -=9
                        elif value_of_your_spin == bet[9]:
                            balance -= 10
                        card_random()
                except:
                    print("please enter valid bet coints")
    else:
        print("sorry please enter valid input")
            
                    

#log in form
def logINForm():
    print("lets play card game")

    while True: 
        user_name = input("enter your email: ").lower()
        use_pss = input("enter your password: ").lower()
            
        if user_name == "":
            print("please enter your email"),
        elif use_pss == "":
            print("please enter your password")
        else:
            time_limit()


logINForm()













