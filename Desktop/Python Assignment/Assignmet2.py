# from tkinter import *
# root = Tk()
# frame = Frame(root)
# frame.pack()
# bottomframe = Frame(root)
# bottomframe.pack( side = BOTTOM )
# redbutton = Button(frame, text="Red", fg="red")
# redbutton.pack( side = LEFT)
# greenbutton = Button(frame, text="Brown", fg="brown")
# greenbutton.pack( side = LEFT )
# bluebutton = Button(frame, text="Blue", fg="blue")
# bluebutton.pack( side = LEFT )
# blackbutton = Button(bottomframe, text="Black", fg="black")
# blackbutton.pack( side = BOTTOM)
# root.mainloop()

from tkinter import *

root = Tk()

# Top frame
topframe = Frame(root)
topframe.pack()

# Bottom frame
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

# Reversed position and color
# Top: Red button with black text
redbutton = Button(topframe, text="Red", fg="black")
redbutton.pack()

# Bottom (right to left): Blue, Brown, Black
# with reversed colors
blackbutton = Button(bottomframe, text="Black", fg="red")
blackbutton.pack(side=RIGHT)

brownbutton = Button(bottomframe, text="Brown", fg="blue")
brownbutton.pack(side=RIGHT)

bluebutton = Button(bottomframe, text="Blue", fg="brown")
bluebutton.pack(side=RIGHT)

root.mainloop()
