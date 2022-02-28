import tkinter as tk
from tkinter import *
 
 
smenarna = Tk()

l = Label(smenarna, text = "Směnárna")
l.config(font =("Courier", 14))

v = IntVar() 
 
Radiobutton(smenarna, text="Nákup", variable=v, value=1).pack(anchor=W) 
Radiobutton(smenarna, text="Prodej", variable=v, value=2).pack(anchor=W) 

smenarna.option_add('*Font', 'serif 8') # protože defaultní písmo pod Windows je hrozné

listbox = Listbox(smenarna)
listbox.pack()

listbox.insert(END, u"Měna")
for item in ["AUD", "DKK", "EUR", "HDK"]:
    listbox.insert(END, item)
  

# specify size of window.
smenarna.geometry("200x300")

# Create an Exit button.
b1 = Button(smenarna, text = "Exit",
            command = smenarna.destroy)


#mena = {}
#mena[0]


 
l.pack()
#T.pack()
b1.pack()
 
 
tk.mainloop()