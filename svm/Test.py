from Tkinter import *
import ttk
import tkFont


##def calculate(*args):
##    try:
##        value = float(feet.get())
##        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
##    except ValueError:
##        pass
##

root = Tk()
root.title("American Sign Language Translation")

font1 = tkFont.Font(family="Helvetica", size=60, weight=tkFont.BOLD, slant=tkFont.ITALIC)

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

currenttranslation = 'A'
imgobj = PhotoImage(file='A.gif')
historytranslation = 'ABCDE'

#ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
#ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Current:", font=font1).grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Recent Translation:", font=font1).grid(column=1, row=3, sticky=E)
ttk.Label(mainframe, text=currenttranslation, font=font1, foreground="blue").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text=historytranslation, font=font1, foreground="green").grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, image=imgobj).grid(column=1, row=1, sticky=E)

for child in mainframe.winfo_children(): child.grid_configure(padx=25, pady=25)

#feet_entry.focus()
#root.bind('<Return>', calculate)

root.mainloop()
