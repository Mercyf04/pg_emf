import pyautogui as pg
import time
import webbrowser

points = 0


# Question 1

answer = pg.prompt(
"""
Which would I rather watch?

a)How I met your Mother
b)Friends
c)New Girl
d)Baby Daddy

"""
    )
# Give Points

if answer == "a":
    points += 4
elif answer == "b":
    points += 1
elif answer == "c":
    points += 3
elif answer == "d":
    points += 0


# Question 2

answer = pg.prompt(
"""
Which would I rather eat?

a)pasta
b)pizza
c)ceaser salad
d)chicken tenders

"""
    )
# Give Points

if answer == "a":
    points += 3
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 3


# Question 3

answer = pg.prompt(
"""
What is my favorite ice cream?

a)chocolate
b)vanilla
c)coffee
d)oreo

"""
    )
# Give Points

if answer == "a":
    points += 5
elif answer == "b":
    points += 0
elif answer == "c":
    points += 5
elif answer == "d":
    points += 2


# Question 4

answer = pg.prompt(
"""
Where do I want to travel?

a)Bora Bora
b)Greece
c)Texas
d)Oregon

"""
    )
# Give Points

if answer == "a":
    points += 4
elif answer == "b":
    points += 4
elif answer == "c":
    points += 1
elif answer == "d":
    points += 0

# Question 5

answer = pg.prompt(
"""
What is my favorite season?

a)Summer
b)Spring
c)Winter
d)Fall

"""
    )
# Give Points

if answer == "a":
    points += 5
elif answer == "b":
    points += 2
elif answer == "c":
    points += 2
elif answer == "d":
    points += 1


# Question 6

answer = pg.prompt(
"""
Who is my favorite music artist?

a)Cardi B
b)Chance the Rapper
c)SZA
d)Vance Joy

"""
    )
# Give Points

if answer == "a":
    points += 2
elif answer == "b":
    points += 1
elif answer == "c":
    points += 2
elif answer =="d":
    points += 2


# End of Survey

pg.alert("You recieved...press enter")

#Bad Score
if points < 5:
        pg.alert("a bad score :(")
        webbrowser.open("https://media.giphy.com/media/132bzOAtymSqc0/giphy.gif")

#Okay Score
elif points >= 5 and points < 8:
    pg.alert("an okay score :I")
    webbrowser.open("https://media1.tenor.com/images/81c7478e130cfd8039875038f42a3fd7/tenor.gif?itemid=4197990")
#Good Score
elif points >= 8 and points < 20:
    pg.alert("a good score ;)")
    webbrowser.open("https://m.popkey.co/d86114/qxy0g.gif")
#Great Score
elif points >= 20 and points <23:
    pg.alert("a great score :)))")
    webbrowser.open("https://i.imgur.com/dUAVCVE.gif")
