import pyautogui as pg
import webbrowser
import time

mood = pg.prompt(
    """
What season would you like to shop for today?
a)Summer
b)Winter
c)Spring
d)Fall

""")

if season == "a":
    answer = pg.prompt(
        """

""")
    pg.alert("I hope you enjoy: " + answer)
    pg.alert("Here's a fun video to keep you smiling!")
    webbrowser.open("https://www.youtube.com/watch?v=ZbZSe6N_BXs")


elif mood == "b":
    answer = pg.prompt(
        """
I'm sorry you're sad. Any particular reason?

""")
    pg.alert("I hope this will make you feel a little better.")
    webbrowser.open("https://www.youtube.com/watch?v=MBRqu0YOH14")

    
