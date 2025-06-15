# import tkinter 
# top = tkinter.Tk() 
# C = tkinter.Canvas(top, bg="blue", height=250, width=300) 
# coord = 10, 50, 240, 210 
# arc = C.create_arc(coord, start=0, extent=150, fill="red") 
# C.pack() 
# top.mainloop() 

import tkinter

x = tkinter.Tk()
c1 = tkinter.Canvas(x, bg="green", height=250, width=300)
coord = 10, 50, 240, 210 
arc = c1.create_arc(coord, start=-150, extent=150, fill="orange")
c1.pack()
x.mainloop()
