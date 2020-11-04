from tkinter import *
from random import randint

class aplikace:
  def __init__ (self):
    self.okno=Tk()
    # plán je 25x25 políček o rozměrech 25x25 px
    self.platno=Canvas(self.okno,width=625,height=625,bg="#F03A3A")
    self.platno.pack()
    self.vyrobludiste()
    # směr vpravo [1,0], vlevo [-1,0], dolu [0,1], nahoru [0,-1]
    self.klavesnice=[]     # seznam zmáčknutých kláves
    self.h1=hrac(self,1,1,"panáček","salat.png",["Left","Right","Up","Down","space"],[1,0])
    self.h2=hrac(self,23,23,"robot","bla.png",["a","d","w","s","v"],[-1,0])
    # bludiště bude seznam řádků = seznamy políček
    
    # spojování událostí a reakcí na ně
    # <pismeno>, <Left>, <space>
    
    self.okno.bind("<KeyPress>",self.stisk)
    self.okno.bind("<KeyRelease>",self.pusteni)
    self.novybalicek()
  def novybalicek(self):
    b=balicek(self)
    self.okno.after(3000,self.novybalicek)
  
  def stisk(self,event):
    klapka=event.keysym
    self.klavesnice.append(klapka)
    print(self.klavesnice)
  def pusteni(self,event):
    klapka=event.keysym
    self.klavesnice.remove(klapka)
    

    
  def vyrobludiste(self):
    self.bludiste=[]
    # 0....volno, 1....zed
    self.bludiste.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
    self.bludiste.append([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1])
    self.bludiste.append([1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1])
    self.bludiste.append([1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1])
    self.bludiste.append([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1])
    self.bludiste.append([1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,1])
    self.bludiste.append([1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1])
    self.bludiste.append([1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1])
    self.bludiste.append([1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1])
    self.bludiste.append([1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1])
    self.bludiste.append([1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1])
    self.bludiste.append([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1])
    self.bludiste.append([1,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1])
    self.bludiste.append([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1])
    self.bludiste.append([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1])
    self.bludiste.append([1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
    self.bludiste.append([1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
    self.bludiste.append([1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1])
    self.bludiste.append([1,0,0,0,0,0,0,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1])
    self.bludiste.append([1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1])
    self.bludiste.append([1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1])
    self.bludiste.append([1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,1])
    self.bludiste.append([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
    self.bludiste.append([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
    self.bludiste.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
    for i in range(25):               #dá nám řádky
      for j in range(25):             #dá nám políčka
        if (self.bludiste[i][j]==1):
          self.platno.create_rectangle(j*25,i*25,j*25+25,i*25+25,fill="#0AFFD2")
        else:
          self.platno.create_rectangle(j*25,i*25,j*25+25,i*25+25,fill="#FF0FF0")
          
class hrac:
  def __init__ (self,a,x,y,jmeno,vzhled,ovladani,smer):
    self.a=a
    self.x=x
    self.y=y
    self.jmeno=jmeno
    self.vzhled=vzhled
    self.ovladani=ovladani
    self.timeout=0
    self.smer=smer
    self.zivoty=3
    self.munice=100
    self.soubor=PhotoImage(file=vzhled)
    self.vzhled=self.a.platno.create_image(x*25+12,y*25+12,image=self.soubor)
    self.pozor()
    

    
  def pozor(self):
    if(self.ovladani[0] in self.a.klavesnice): self.pohyb([-1,0])
    if(self.ovladani[1] in self.a.klavesnice): self.pohyb([1,0])
    if(self.ovladani[2] in self.a.klavesnice): self.pohyb([0,-1])
    if(self.ovladani[3] in self.a.klavesnice): self.pohyb([0,1])
    if(self.ovladani[4] in self.a.klavesnice): self.vystrel()
    self.timeout=self.timeout-50
    self.a.okno.after(50,self.pozor)
    
    
    
  def pohyb(self,smer):
    self.smer=smer
    xx=self.x+smer[0]
    yy=self.y+smer[1]
    if (self.a.bludiste[yy][xx]!=1):
      self.x=xx
      self.y=yy
      self.a.platno.move(self.vzhled,smer[0]*25,smer[1]*25)
      if(self.a.bludiste[yy][xx]!=0): #balicek
        b=self.a.bludiste[yy][xx]
        b.zmiz()
        self.munice=self.munice+10
        
        
  def vystrel(self):
    if (self.timeout<=0) and (self.munice>0):
      self.munice=self.munice-1
      s=strela(self.a,self.x,self.y,self.smer)
      self.timeout=100
      
      
  def trefa(self):
    self.zivoty=self.zivoty=self.zivoty-1
    if(self.zivoty==0):
      self.a.platno.create_text(312,312,text="PROHRÁL "+ self.jmeno,font=["Arial",40],fill="red")
      self.a.okno.after(2000,self.a.okno.quit)
      
      
class strela:
  def __init__ (self,a,x,y,smer):
    self.a=a
    self.x=x
    self.y=y
    self.smer=smer
    self.vzhled=self.a.platno.create_oval(x*25+10,y*25+10,x*25+15,y*25+15,fill="white",outline="white")
    self.pohyb()
  def pohyb(self):
    self.x=self.x+self.smer[0]
    self.y=self.y+self.smer[1]
    self.a.platno.move(self.vzhled,self.smer[0]*25,self.smer[1]*25)
    self.kolize()  # zkoumat jestli střela trefila hráče
    if (self.a.bludiste[self.y][self.x]!=1):
      self.a.okno.after(10,self.pohyb)
   
    else:
      self.zmiz()
  def zmiz(self):
    self.a.platno.delete(self.vzhled) 
    
  def kolize(self):
    if (self.x==self.a.h1.x) and (self.y==self.a.h1.y):
      self.a.h1.trefa()
    if (self.x==self.a.h2.x) and (self.y==self.a.h2.y):
      self.a.h2.trefa()
      
class balicek:
  def __init__ (self,a):
    self.a=a #aplikace
    self.x=randint(1,24)
    self.y=randint(1,24)
    while (self.a.bludiste[self.y][self.x]==1):
      self.x=randint(1,24)
      self.y=randint(1,24)
    self.vzhled=self.a.platno.create_rectangle(self.x*25+4,self.y*25+4,self.x*25+20,self.y*25+20,fill="darkblue")
    self.a.bludiste[self.y][self.x]=self
  def zmiz(self):
    self.a.platno.delete(self.vzhled)
    self.a.bludiste[self.y][self.x]=0
    
    
    
    
    
    

    
    
    
  
    
  
  
  
          
          
    
a=aplikace()
mainloop()
