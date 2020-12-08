from tkinter import *

from tkinter import messagebox
import random
a = Tk()
SIZE = 500
BOMB = 500
C = Canvas(a, bg = "white", height = SIZE, width = SIZE)
listjmen = ['Liam','Noah','Oliver','William','Elijah','James','Benjamin','Lucas','Mason','Ethan','Alexander','Henry','Jacob','Michael','Daniel','Logan','Jackson','Sebastian','Jack','Aiden','Owen','Samuel','Matthew','Joseph','Levi','Mateo','David','John','Wyatt','Carter','Julian','Luke','Grayson','Isaac','Jayden','Theodore','Gabriel','Anthony','Dylan','Leo','Lincoln','Jaxon','Asher','Christopher','Josiah','Andrew','Thomas','Joshua','Ezra','Hudson','Charles','Caleb','Isaiah','Ryan','Nathan','Adrian','Christian','Maverick','Colton','Elias','Aaron','Eli','Landon','Jonathan','Nolan','Hunter','Cameron','Connor','Santiago','Jeremiah','Ezekiel','Angel','Roman','Easton','Miles','Robert','Jameson','Nicholas','Greyson','Cooper','Ian','Carson','Axel','Jaxson','Dominic','Leonardo','Luca','Austin','Jordan','Adam','Xavier','Jose','Jace','Everett','Declan','Evan','Kayden','Parker','Wesley','Kai','Luka','Kyrie','Kevin','Lebron','Joe','Sal','Ja','Zion','Giannis','DeAaron','Carmelo','Kobe','Shaquille','Kareem','Hakeem','Dennis','Jim','Dwight','Obama','Sadam']



def resetCanvas():
	C.delete('all')
	telo((random.randint(80,120)), (random.randint(530, 570)), (random.randint(380,420)), (random.randint(280,320)),  "#"+str((random.randint(100000,999999))))
	hlava((random.randint(350,400)),(random.randint(350,400)),130, 130,  "#"+str((random.randint(100000,999999))))
	pusa((random.randint(130,150)),(random.randint(170,190)),(random.randint(330,360)),(random.randint(310,330)),  "#"+str((random.randint(100000,999999))), 180, 180)
	ocicka1((random.randint(200,240)), (random.randint(200,240)), (random.randint(150,190)), (random.randint(150,190)),  "#"+str((random.randint(100000,999999))))
	ocicka2((random.randint(305,345)), (random.randint(200,240)), (random.randint(255,295)), (random.randint(150,190)) , "#"+str((random.randint(100000,999999))))
	zornice1(200, 200, 190, 190, 'black')
	zornice1(305, 200, 295, 190, 'black')
	draw_symmetriclines((random.randint(120,190)),(random.randint(370,430)),(random.randint(260,320)),(random.randint(420,470)), "#"+str((random.randint(100000,999999))), (random.randint(1,22)))
	textjmeno=listjmen[random.randint(0,99)]
	jmenotext=C.create_text(250, 25, font=("Comic Sans MS",35), text=textjmeno)
	vektext=C.create_text(250 ,70, font=("Comic Sans MS",25), text=vekcislo)
	
smazatbutton=Button(text='novy', command=resetCanvas)
smazatbutton.pack()



def telo(ab, bc, de, fg, color):
	telicko=C.create_rectangle(ab, bc, de, fg, fill=color)
randomcolor = "#"
listOfHexCharacters = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
positionInList = random.randint(0,15)
for i in range(6):
    hex_char = listOfHexCharacters[positionInList]
    randomcolor+=hex_char
    positionInList = random.randint(0,15)
telo((random.randint(80,120)), (random.randint(530, 570)), (random.randint(380,420)), (random.randint(280,320)), randomcolor)
	
	
	
def hlava(jedna, dva, tri, ctyri, color):
	hlavicka=C.create_oval(jedna, dva, tri, ctyri, fill=color)
randomcolor = "#"
listOfHexCharacters = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
positionInList = random.randint(0,15)
for i in range(6):
    hex_char = listOfHexCharacters[positionInList]
    randomcolor+=hex_char
    positionInList = random.randint(0,15)
hlava((random.randint(350,400)),(random.randint(350,400)),130, 130, randomcolor)



def pusa(prvni, druha, treti, ctvrta, color, start, extent):
	pusi=C.create_arc(prvni, druha, treti, ctvrta, fill=color, start=start, extent=extent)
randomcolor = "#"
listOfHexCharacters = ["0","1","2","3","4","5","6","7","8","9","c","d","e","f"]
positionInList = random.randint(0,13)
for i in range(6):
    hex_char = listOfHexCharacters[positionInList]
    randomcolor+=hex_char
    positionInList = random.randint(0,13)
pusa((random.randint(140,160)),(random.randint(170,190)),(random.randint(320,360)),(random.randint(300,330)), randomcolor, 180, 180)



def ocicka1(uno, dos, tres, quatro, color):
	oci=C.create_oval(uno, dos, tres, quatro, fill=color)
randomcolor = "#"
listOfHexCharacters = ["0","1","2","3","4","5","6","7","8","9","e","f"]
positionInList = random.randint(0,11)
for i in range(6):
    hex_char = listOfHexCharacters[positionInList]
    randomcolor+=hex_char
    positionInList = random.randint(0,11)
ocicka1((random.randint(200,240)), (random.randint(200,240)), (random.randint(150,190)), (random.randint(150,190)), randomcolor)



def ocicka2(uno, dos, tres, quatro, color):
	oci=C.create_oval(uno, dos, tres, quatro, fill=color)
randomcolor = "#"
listOfHexCharacters = ["0","1","2","3","4","5","6","7","8","9","e","f"]
positionInList = random.randint(0,11)
for i in range(6):
    hex_char = listOfHexCharacters[positionInList]
    randomcolor+=hex_char
    positionInList = random.randint(0,11)
ocicka2((random.randint(305,345)), (random.randint(200,240)), (random.randint(255,295)), (random.randint(150,190)) ,randomcolor)



def zornice1(ein, zwei, polizei, drei, color):
	kuk=C.create_oval(ein, zwei, polizei, drei, fill=color)
zornice1(200, 200, 190, 190, 'black')



def zornice2(ein, zwei, polizei, drei, color):
	kuk=C.create_oval(ein, zwei, polizei, drei, fill=color)
zornice1(305, 200, 295, 190, 'black')



def draw_symmetriclines(start_x, start_y, end_x, end_y, color, thick):
	line = C.create_line(start_x, start_y, end_x, end_y, fill=color, width=thick)

	line = C.create_line(BOMB - start_x, start_y, BOMB - end_x, end_y, fill=color, width=thick)

draw_symmetriclines((random.randint(120,190)),(random.randint(370,430)),(random.randint(260,320)),(random.randint(420,470)), "#"+str((random.randint(100000,999999))), (random.randint(1,22)))



def jmeno():
	listjmen = ['Liam','Noah','Oliver','William','Elijah','James','Benjamin','Lucas','Mason','Ethan','Alexander','Henry','Jacob','Michael','Daniel','Logan','Jackson','Sebastian','Jack','Aiden','Owen','Samuel','Matthew','Joseph','Levi','Mateo','David','John','Wyatt','Carter','Julian','Luke','Grayson','Isaac','Jayden','Theodore','Gabriel','Anthony','Dylan','Leo','Lincoln','Jaxon','Asher','Christopher','Josiah','Andrew','Thomas','Joshua','Ezra','Hudson','Charles','Caleb','Isaiah','Ryan','Nathan','Adrian','Christian','Maverick','Colton','Elias','Aaron','Eli','Landon','Jonathan','Nolan','Hunter','Cameron','Connor','Santiago','Jeremiah','Ezekiel','Angel','Roman','Easton','Miles','Robert','Jameson','Nicholas','Greyson','Cooper','Ian','Carson','Axel','Jaxson','Dominic','Leonardo','Luca','Austin','Jordan','Adam','Xavier','Jose','Jace','Everett','Declan','Evan','Kayden','Parker','Wesley','Kai']


textjmeno=listjmen[random.randint(0,119)]
jmenotext=C.create_text(250, 25, font=("Comic Sans MS",35), text=textjmeno)


vekcislo=(random.randint(0,100))
vektext=C.create_text(250 ,70, font=("Comic Sans MS",25), text=vekcislo)
	
	
C.pack()
a.mainloop()
