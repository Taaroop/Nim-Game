# Dr. Nim
# Faiyaz Siddiquee
# Dec 15, 2023

import sys

def play(x, y, n):
    a = min(x, y)
    b = max(x, y)
    
    li = []
    status = "W"
    for i in range(b):
        if i%a == 0:
            if status == "W":
                status = "L"
            else:
                status = "W"
        if i == b:
            li.append("W")
        else:
            li.append(status)
    
    if n < b:
        return li[n]
    else:
        if play(x, y, n-x) == "L" or play(x, y, n-y) == "L":
            return "W"
        else:
            return "L"

n = int(input("Enter the total number of items: "))
x = int(input("Enter option 1: "))
y = int(input("Enter option 2: "))

if x == y or x < 0 or y < 0 or n < 0:
    print("Invalid parameters. Code terminated.")
    sys.exit()

if play(x, y, n) == "L":
    print("Okay, you go first!")
else:
    print("Okay, I go first!")
    
    if play(x, y, n-x) == "L":
        print("I take", x, "item(s). Remaining:", n-x)
        n -= x
    else:
        print("I take", y, "item(s). Items remaining:", n-y)
        n -= y

if n-x < 0 and n-y < 0:
    win = True
    print("You have no valid moves! I win!")
else:
    win = False
    
while win == False:
    
    opp_turn = -1
    while opp_turn != x and opp_turn != y or n-opp_turn < 0:
        opp_turn = int(input("Play your turn (has to be valid): "))
    n -= opp_turn
    print("Items remaining:", n)
    
    if play(x, y, n-x) == "L":
        print("I take", x, "item(s). Remaining:", n-x)
        n -= x
    else:
        print("I take", y, "item(s). Items remaining:", n-y)
        n -= y
    
    if n-x < 0 and n-y < 0:
        win = True
        print("You have no valid moves! I win!")
    else:
        win = False
