from tkinter import *

class create_canvas(Tk):

    def __init__(self):

        Tk.__init__(self)

        #Title
        self.Title = Label(self, text = "Fractal Renderer")
        self.Title.grid(row = 0, column = 1)

        #C
        self.C_min_label = Label(self, text = "C Min Value")
        self.C_min = Entry(self)
        self.C_max_label = Label(self, text="C Max Value")
        self.C_max = Entry(self)
        self.C_min_label.grid(row=1, column = 0)
        self.C_min.grid(row=1, column= 1)
        self.C_max_label.grid(row=2, column=0)
        self.C_max.grid(row=2, column=1)

        #Z

        #Enter
        self.Get = Button(self, text = "Enter", command = self.Enter)
        self.Get.grid(row = 2, column = 1)

    def Enter(self):
        print(self.C_min.get())



w = create_canvas()
w.mainloop()