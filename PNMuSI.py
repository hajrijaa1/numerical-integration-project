from tkinter import *
from tkinter import messagebox
import math
import tkinter

def trapezovo(f,a,b,n):
    h=(max(a,b)-min(a,b))/n
    total=0
    for n in range(0,n):
        x=a+n*h
        y0=eval(f)
        x=a+(n+1)*h
        y1=eval(f)
        total=total+((h/2)*(y0+y1))
    # label_text.set(total)   
    total = f.get()
    print(total) 
    # return total



    

def simpsonovo(f,a,b,n):
    if n%2==0:
        h=(max(a,b)-min(a,b))/n
        total=0
        for i in range(0,n+1):
            if i== 0 or i ==n:
                x=a+i*h
                total=total+eval(f)
                
            elif i%2==0:
                x=a+i*h
                total=total+2*eval(f)
                
            else:
                x=a+i*h
                total=total+4*eval(f)
         
        return total*(h/3)
    else:
        return(simpsonovo(f,a,b,n*2))

    
    
def integriranje_udesno(f,a,b,n):
    h=(max(a,b)-min(a,b))/n
    total=0
    for n in range(1,n+1):
        x=a+n*h
        total=total+eval(f)
    return total*h
    
def integriranje_ulijevo(f,a,b,n):
    h=(max(a,b)-min(a,b))/n
    total=0
    for n in range(0,n):
        x=a+n*h
        total=total+eval(f)
        
    return total*h


# KREIRANJE PROZORA
window = Tk()
window.title("Numerical Integration Solver")
window.geometry('600x400')

funkcija = StringVar()
num_a = StringVar()
num_b = StringVar()
broj_n = StringVar()
rjesenje = StringVar()
# ISPISIVANJE PORUKE PRILIKOM KLIKA NA BUTTON
def helloCallBack():
   msg = messagebox.showinfo("Simpsonovo", "Izabrali ste simpsonovo pravilo!")



def rez():
    Funk = (funkcija.get())
    Br1 = (num_a.get())
    Br2 = (num_b.get())
    Brn = (broj_n.get())
    if Funk.isdigit() or Br1.isdigit() or Br2.isdigit() or Brn.isdigit():
        if eval(Brn) % 2==0:
            h=(max(eval(Br1),eval(Br2))-min(eval(Br1),eval(Br2)))/eval(Brn)
            Rjes=0
            for i in range(0,eval(Brn)+1):
                if i== 0 or i == eval(Brn):
                    x=eval(Br1)+i*h
                    Rjes=Rjes+eval(Funk)
                elif i%2==0:
                    x=eval(Br1)+i*h
                    Rjes=Rjes+2*eval(Funk)
                
                else:
                    x=eval(Br1)+i*h
                    Rjes=Rjes+4*eval(Funk)
         
            rjesenje.set(Rjes*(h/3))
        
        else:
            rjesenje.set(Rjes(Funk, Br1, Br2, Brn*2))
            return True

def rez2():
    Funk = (funkcija.get())
    Br1 = (num_a.get())
    Br2 = (num_b.get())
    Brn = (broj_n.get())
    if Funk.isdigit() or Br1.isdigit() or Br2.isdigit() or Brn.isdigit():
        h=(max(eval(Br1),eval(Br2))-min(eval(Br1),eval(Br2)))/eval(Brn)
        Rjes=0
        for n in range(0,eval(Brn)):
            n = str(n)
            h = str(h)
            x=Br1+n*h
            y0=eval(f)
            x=Br1+(n+1)*h
            y1=eval(f)
            Rjes=Rjes+((h/2)*(y0+y1))  
        rjesenje.set(Rjes)
        return True

def rez3():
    Funk = (funkcija.get())
    Br1 = (num_a.get())
    Br2 = (num_b.get())
    Brn = (broj_n.get())
    if Funk.isdigit() or Br1.isdigit() or Br2.isdigit() or Brn.isdigit():
        h=(max(eval(Br1),eval(Br2))-min(eval(Br1),eval(Br2)))/eval(Brn)
        Rjes=0
        for n in range(1,eval(Brn)+1):
            x=eval(Br1)+n*h
            Rjes=Rjes+eval(f)
        rjesenje.set(Rjes*h)
        return True

# LABELE SU l1, l2, l3 i l4, A VRIJEDNOSTI UNOSIMO U f, a, b i n
# DA IZBJEGNEM GRID KORISTILA SAM x i y PA UNOSILA VRIJEDNOSTI :(
# bd je border oko labele gdje se unose vrijednosti
lblf = Label(window, text="Unesite funkciju f(x): ")
lblf.place(x = 120, y = 90)
f = Entry(window, bd = 3, textvariable=funkcija)
f.place(x = 300, y = 90)


lbl_a = Label(window, text="Unesite donju granicu a: ")
lbl_a.place(x = 120, y = 130)
a = Entry(window, bd = 3, textvariable = num_a)
a.place(x = 300, y = 130)

lbl_b = Label(window, text="Unesite gornju granicu b: ")
lbl_b.place(x = 120, y = 170)
b = Entry(window, bd = 3, textvariable = num_b)
b.place(x = 300, y = 170)

lbl_n = Label(window, text="Unesite broj aproksimiranja: ")
lbl_n.place(x = 120, y = 210)
n = Entry(window, bd = 3, textvariable = broj_n)
n.place(x = 300, y = 210)

    
# OVA metoda TREBA ISPISATI RJEŠENJE
l5 = Label(window, text="Rješenje funkcije f(x) iznosi:  ")
l5.place(x = 120, y = 260)
metoda = Label(window, bd = 3, textvariable=rjesenje)
metoda.place(x = 300, y = 260)

# FUNKCIJE ZA RESET I EXIT
def Reset():
    funkcija.set("")
    num_a.set("")
    num_b.set("")
    broj_n.set("")
    rjesenje.set("")

def Exit():
    Exit = tkinter.messagebox.askyesno("Validate Entry Widget", "Da li želite izaći iz aplikacije?")
    if Exit > 0:
        window.destroy()
        return

# BUTTONI
# U OVOM BUTTONU IMAMO PORUKU, STOGA IMAMO COMMAND
# RELIEF SE KORISTI ZA IZGLED BUTTONA, CURSOR SE MIJENJA PRILIKOM PRELAŽENJA PREKO BUTTONA
B1 = Button(window, text = "Simpsonovo" ,command=rez2, relief = RAISED, cursor = "exchange", height=2, width=12, background= "#C0C0C0")
B1.place(x = 50, y = 10)

B2 = Button(window, text="Trapezovo", command=rez, relief = RAISED, cursor = "exchange", height=2, width=12, justify=CENTER, background= "#C0C0C0")
B2.place(x = 180, y = 10)

B3 = Button(window, text="Udesno", command=rez3,relief = RAISED, cursor = "exchange", height=2, width=12, background= "#C0C0C0")
B3.place(x = 315, y = 10)

B4 = Button(window, text="Ulijevo",relief = RAISED, cursor = "exchange", height=2, width=12, background= "#C0C0C0")
B4.place(x = 450, y = 10)


# BUTTONI ZA RESET I EXIT
btnReset = Button(window, text="Resetuj", command=Reset, relief = RAISED, cursor = "exchange", height=2, width=12, background= "#C0C0C0")
btnReset.place(x = 315, y = 320)

btnExit = Button(window, text="Izađi", command=Exit, relief = RAISED, cursor = "exchange", height=2, width=12, background= "#C0C0C0")
btnExit.place(x = 450, y = 320)
# POZIV GLAVNOG PROZORA
window.mainloop()


# # ISPIS U KONZOLI
print("Numerička interpolacija")
f=input("Unesite funkciju f(x): ")
a=eval(input("Unesite donju granicu integrala a: "))
b=eval(input("Unesite gornju granicu integrala b: "))
n=eval(input("Unesite broj aproksimiranja: "))

print("Trapezovo pravilo:",trapezovo(f,a,b,n))
print("Simpsonovo pravilo:",simpsonovo(f,a,b,n))
print("Integriranje udesno:",integriranje_udesno(f,a,b,n))
print("Simpsonovo pravilo:",integriranje_ulijevo(f,a,b,n))
