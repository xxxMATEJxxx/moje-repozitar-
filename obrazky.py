from tkinter import *

from tkinter import messagebox
import random
seed = random.randint(0,100000)
print(seed)
random.seed(seed)
a = Tk()
SIZE = 500
C = Canvas(a, bg = "#000000", height = SIZE, width = SIZE)
def draw_symmetriclines(start_x, start_y, end_x, end_y, color):
	line = C.create_line(start_x, start_y, end_x, end_y, fill=color)
	line = C.create_line(SIZE - start_x, SIZE - start_y, SIZE - end_x,SIZE - end_y, fill=color)
	line = C.create_line(SIZE - start_x, start_y, SIZE - end_x, end_y, fill=color)
	line = C.create_line(start_x, SIZE - start_y, end_x, SIZE - end_y, fill=color)
draw_symmetriclines(random.randint(0,500), random.randint(0,500), random.randint(0,500), random.randint(0,500), "#"+str((random.randint(100000,999999))))	#vygeneruje náhodnou barvuXnevýhoda, nemá to písmenka
	

	
	
	

C.pack()
a.mainloop()
