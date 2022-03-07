from os.path import basename, splitext
import tkinter as tk
from tkinter import Listbox, Radiobutton, IntVar, StringVar, END
 

class About(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent, class_=parent.name)
        self.config()

        btn = tk.Button(self, text="Konec", command=self.close)
        btn.pack()

    def close(self):
        self.destroy()

class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Směnárna"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="Hello World")
        self.lbl.pack()
        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()
        self.btn2 = tk.Button(self, text="About", command=self.about)
        self.btn2.pack()

        self.varOperace = StringVar()
        self.rbtNakup = Radiobutton(
            self, text="Nákup", variable=self.varOperace, value="nakup"
        )
        self.rbtProdej = Radiobutton(
            self, text="Prodej", variable=self.varOperace, value="prodej"
        )
        self.rbtNakup.pack()
        self.rbtProdej.pack()
        self.varOperace.set("prodej")

        self.lstBx = Listbox(self)
        self.lstBx.pack()
        self.lstBx.bind("<ButtonRelease-1>", self.kliknu)

        f = open("listek.txt")
        self.radky = f.readlines()

        for radek in self.radky:
            radek = radek.split()
            self.lstBx.insert(END, radek[0])
    def cteni():
        print vstupObsah.get()   # pristup pres tkPromennou
        print vstup.get()        # pristup pres metodu get instance Entry 

        vstup = Entry(hlavni, textvariable=vstupObsah, width=40, validate="key", 
                validatecommand=overeni)
        vstup.pack(side=LEFT)
        vstup.focus_set()           # aby se dalo hned psát
        vstup.icursor(END)          # aby byl kurzor na konci
        vstup.selection_range(0, END)
  
        tlacitko = Button(hlavni, text=u"přečti", width=10, command=cteni)
        tlacitko.pack()
       

    def kliknu(self, event):
        index = self.lstBx.curselection()[0]
        print(self.radky[index])

    def about(self):
        window = About(self)
        window.grab_set()

    def quit(self, event=None):
        super().quit()


#smenarna = Tk()
#l = Label(smenarna, text = "Směnárna")
#l.config(font =("Courier", 14))
#v = IntVar() 
#Radiobutton(smenarna, text="Nákup", variable=v, value=1).pack(anchor=W) 
#Radiobutton(smenarna, text="Prodej", variable=v, value=2).pack(anchor=W) 
#smenarna.option_add('*Font', 'serif 8') # protože defaultní písmo pod Windows je hrozné
#listbox = Listbox(smenarna)
#listbox.pack()
#listbox.insert(END, u"Měna")
#for item in ["AUD", "DKK", "EUR", "HDK"]:
#    listbox.insert(END, item) 
# specify size of window.
#smenarna.geometry("200x300")
# Create an Exit button.
#b1 = Button(smenarna, text = "Exit",
 #           command = smenarna.destroy)
#mena = {}
#mena[0]
#l.pack()
#T.pack()
#b1.pack()
 


 
app = Application()
app.mainloop()