
import webbrowser
import speech_recognition as sr
import pyttsx3 as ps
import time

flag = 0
print("---------------------------------------------------------------------------------------")

a= "\t\t\t\t\t\tWelcome \n\t\t\t\t\t\tI am your Voice Assistant.\n\t\t\t\t\t\tI can run some basic linux commands for you."
print(a)
ps.speak(a)
print("\n")

while(flag==0):

	b = "\t\t\t\t\t\tWhich command do you want me to run?"
	print(b)
	ps.speak(b)
	r = sr.Recognizer()

	with sr.Microphone() as source:
		audio = r.listen(source)	

	ch = r.recognize_google(audio)
	print(ch)
	print("\t\t\t\t\t\tI got it....")
	ps.speak("I got it....")

	if ("run" in ch) and ("cal" in ch) or ("calender" in ch):
		op = "\t\t\t\t\t\tRunning CAL command."
		print(op)
		ps.speak(op)
		webbrowser.open("http://192.168.0.10/cgi-bin/iiec.py?cmd=cal")
		time.sleep(12)
		
	elif ("run" in ch) and ("date" in ch):
		op = "\t\t\t\t\t\tRunning DATE command."
		print(op)
		ps.speak(op)
		webbrowser.open("http://192.168.0.10/cgi-bin/iiec.py?cmd=date")
		time.sleep(12)
		
	elif (("run" in ch) or ("show" in ch) or ("display") in ch) and (("list" in ch) or ("contents" in ch)):
		op = "\t\t\t\t\t\tRunning LS command."
		print(op)
		ps.speak(op)
		webbrowser.open("http://192.168.0.10/cgi-bin/iiec.py?cmd=ls")
		time.sleep(16)
		
	elif (("show" in ch) or ("display" in ch)) and ("current" in ch) and ("location" in ch):
		op = "\t\t\t\t\t\tRunning pwd command."
		print(op)
		ps.speak(op)
		webbrowser.open("http://192.168.0.10/cgi-bin/iiec.py?cmd=pwd")
		time.sleep(18)
		
		
	elif (("open" in ch) or ("start" in ch)) and ("web" in ch) and ("interface" in ch) and ("Linux" in ch) and ("commands" in ch):
		op = "\t\t\t\t\t\tOpening Web Interface for you.\n\t\t\t\t\t\tWhere you can run any linux command"
		print(op)
		ps.speak(op)
		webbrowser.open("http://192.168.0.10/task.html") 
		flag=1
	
	elif (("turn" in ch) and("off" in ch)) or (("shut" in ch) and ("down" in ch)) or (("Close" in ch) and ("program" in ch)):
		op = "\t\t\t\t\t\tClosing this program."
		print(op)
		ps.speak(op)
		flag=1
		
	else:
		x = "\t\t\t\t\t\tI am unable to understand."
		print(x)
		ps.speak(x)
		y = "\t\t\t\t\t\tCan you say it again..."
		print(y)
		ps.speak(y)
		
	if (flag==1):
		print("---------------------------------------------------------------------------------------\n")
	
	
		
		



 

