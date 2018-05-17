import webbrowser
name = "Mercy Fey"

subjects = ["English", "Spanish", "Math", "History", "Science"]

print("Hello " + name)

for i in subjects:
    print("One of my classes is " + i)

sports = ["Soccer", "Softball", "Basketball", "Lacrosse"]

for i in sports:
    if i == "Socccer":
        print(i + " is my favorite sport.")
    elif i == "Softball":
        print(i + " is my least favorite sport.")
    else:
        print("One common sport is " + i)

icecream = []

while True:
    print("What is an ice cream flavor that you like? Type 'end' to quit.")
    answer = input()
    if answer == "end":
        break
    else:
        icecream.append(answer)

for i in icecream:
    print ("One of your favorite is " + i)
    webbrowser.open("google image " + i)
