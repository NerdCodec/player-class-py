def player_position():
    Player = int(input("Enter the number of jersey: "))

    if 1 <= Player <= 5:
        print("This is a good defender in a back four or five")
        
    elif 6<= Player <= 8:
        print("This player is a midfielder")

    elif 10 <= Player <= 11:
        print("This is an offensive player")

    elif 9:
        print("This is a striker")


player_position()