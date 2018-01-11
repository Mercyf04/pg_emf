import pyautogui as pg
import time

pg.hotkey('ctrl','winleft','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n',0.5)
pg.hotkey('winleft','up')
pg.typewrite('newyorktimes.com\n',0.5)
time.sleep(1)
pg.hotkey('ctrl','t')
pg.typewrite('amazon.com\n')
pg.moveTo(332, 175,3)
pg.click(332,175,1)
pg.typewrite('iphone 7 phone case, black\n',1)
