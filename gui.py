import tkinter

top=tkinter.Tk()
top.configure(background='red')
userInput=7
while userInput != 'n':
	userInput=input("ENTER CONTROL VALUE")

	if userInput == "g":
		top.configure(background='green')
	elif userInput == "r":
		top.configure(background="red")
top.mainloop
