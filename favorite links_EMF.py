import pyautogui as pg
import webbrowser

videos = ["https://www.youtube.com/watch?v=X6SBQNXnVcs","https://www.youtube.com/watch?v=CiweaZQ8g5U"]
news = ["https://www.nationalgeographic.com/","https://www.nytimes.com/subscription/multiproduct/lp8XKUR.html?campaignId=6UUFL&gclid=EAIaIQobChMIxsGq19i52QIVDUwNCh2EMAESEAAYASAAEgKFifD_BwE&dclid=CKO569jYudkCFYSdyAodfoALmg"]

answer = pg.prompt(
"""
Which would you rather do?
a)Watch videos
b)See the news

"""
    )
if answer == "a":
    for i in videos:
        webbrowser.open(i)
elif answer == "b":
    for i in news:
        webbrowser.open(i)
