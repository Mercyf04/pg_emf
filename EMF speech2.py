import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb


speak = wincl.Dispatch("SAPI.SpVoice")

r = sr.Recognizer()
with sr.Microphone() as source:
    speak.Speak("?")
    print("Listening...")
    audio = r.listen(source)
    print("Thinking...")

try:
    words = r.recognize_google(audio)
    speak.Speak(""+ r.recognize_google(audio)+ " on Google.")
    wb.open("" + words)

except sr.UnknownValueError:
    print("")
except sr.RequestError as e:
    print("; {o}".format(e))
