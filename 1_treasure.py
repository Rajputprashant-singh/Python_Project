print("Welcome to the treasure island")
A = input("where you want to go? left or right").lower()
if A == "left":
    B = input("You want to swim or wait").lower()
    if B == "wait":
        C = input("which color you want to choose? yellow or blue or red").lower()
        if C == "yellow":
            print("You Won")
        elif C == "red":
            print("Game over")
        elif C =="blue":
            print("Game over")
    else:
        print("Game is over")
else:
    print("game is over")
