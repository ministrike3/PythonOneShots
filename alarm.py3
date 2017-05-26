import time
import webbrowser
import random

print("When do you want to wake up")
print("ex 07:55")
Wake = input()

Time = time.strftime("%H:%M")

while Time != Wake:
	print("The time is " + Time)
	Time = time.strftime("%H:%M")
	time.sleep(1)

if Time == Wake:
	print("Time to Wake up!")
	webbrowser.open("https://www.youtube.com/watch?v=34Na4j8AVgA", new=0, autoraise=True)
