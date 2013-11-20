
from Tkinter import *

root = Tk()

#Title, duh. Look at the line!
root.title("Passion Project")

var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )


photo = PhotoImage(file="accel.gif")
img = Label(root, image=None)
img.photo = photo


#Introduction
var.set("My passion is coding. Someday, I'd love to get a job developing software or being an indie game developer. \n The question, however, is how can I align this with physics? ")
#Functions 
def acceleration(photo):
    var.set("Acceleration \n \n \n \n \n \n Acceleration is defined as: \n 'the increase in the rate or speed of something. \n How could this be used in code?' \n \n \n")
    


def newton():
  var.set("Newton's Laws \n \n \n")

#Acceleration Button!
accel = Button(root, text="Acceleration", command=acceleration)
accel.pack()

#Newton's Button
newton = Button(root, text="Newton's Laws", command=newton)
newton.pack()

label.pack()


root.mainloop()
