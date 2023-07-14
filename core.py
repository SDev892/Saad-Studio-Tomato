from tkinter import *
import threading
import time 


root = Tk()
root.geometry("300x300")
root.configure(bg='#EE2C19')

Pomo = 1500
count = 1
focus = True



#Stopping Function 
def stop():
	global statue
	statue = False
	start_button.configure(text="start", command=start)



def PomoSystem():
	global Pomo, statue, count, focus
	statue = True
	while True:
		m, s = divmod(Pomo, 60)
		timer_text = "{:02d}:{:02d}".format(m, s)
		time_field.configure(text=timer_text)
		time.sleep(1)
		Pomo -= 1
		if Pomo == 0 and focus and count < 4 :
			Pomo = 300 #Short Break
			count += 1
			focus = False
		elif Pomo == 0 and focus == False:
			Pomo = 1500 #Focusing
			focus = True
		elif Pomo == 0 and focus and count == 4:
			Pomo = 900 #Long Break
			focus = False
			count = 0
		if statue == False:
			break

def start():
	start_button.configure(text='stop', command=stop)
	threading.Thread(target=PomoSystem).start()


time_field = Label(root, text="25:00", bd=0, fg="#EEF1F4", bg="#EE2C19", font=("Poppins", 40))
time_field.pack(pady=10)

start_button = Button(root, text="Start", bd=0, fg="#EE2C19", bg="#EEF1F4", width=10, font=("Poppins", 20),  command=start)
start_button.pack(pady=4)

mainloop()


#Project Finished 
#Don't like and subscribe ####################################################################################100%

