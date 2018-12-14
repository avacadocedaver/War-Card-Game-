ScrOne=40
ScrTwo=40
PlayerOne = [2,3,4,5,6,7,8,9,10,11,12,13,14,2,3,4,5,6,7,8,9,10,11,12,13,14,]
PlayerTwo = [2,3,4,5,6,7,8,9,10,11,12,13,14,2,3,4,5,6,7,8,9,10,11,12,13,14,]
from random import randint
while (ScrOne>=0 and ScrOne<80):
    Drw1 = PlayerOne[randint(0,25)]
    Drw2 = PlayerTwo[randint(0,25)]
    if Drw1>Drw2:
        ScrOne=ScrOne + 1
        ScrTwo=ScrTwo - 1
    elif  Drw1==Drw2:
        Drw1 = PlayerOne[randint(0,25)]
        Drw2 = PlayerTwo[randint(0,25)]
        if Drw1>Drw2:
            ScrOne = ScrOne + 2
            ScrTwo = ScrTwo - 2
        else:
            ScrTwo = ScrTwo + 2
            ScrOne = ScrOne - 2
    else:
        ScrTwo = ScrTwo + 1
        ScrOne = ScrOne - 1
if ScrOne>ScrTwo:
    print("Player One wins!")
else:
    print("Player two wins!")
print(ScrOne, ScrTwo)