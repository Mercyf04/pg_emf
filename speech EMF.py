import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb


speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("What is your favorite food?")
answer = pg.prompt("Enter your favorite food.")

if answer == "pasta":
    speak.Speak ("I like " + answer + " too.")
elif answer == "salad":
    speak.Speak ("Oooo " + answer + " very healthy.")
elif answer == "chocolate":
    speak.Speak ("delicious, I love " + answer)
else:
    speak.Speak("Same I like " + answer + "." + "Let's look at a recipe about " + answer + " on Google.")
    wb.open("https://www.google.com/search?source=hp&ei=5FT0WtDdHqvc5gLqw6YY&q=chocolate+chip+cookies&oq=choc&gs_l=psy-ab.3.1.0l8j0i3k1j0.332.496.0.3326.4.3.0.0.0.0.115.294.1j2.3.0....0...1.1.64.psy-ab..1.3.292...0i131k1.0.4Arqx5YYTkI")


