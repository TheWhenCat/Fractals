from tkinter import *

class create_UI(Tk):

    def __init__(self):

        Tk.__init__(self)

        #Title
        self.Title = Label(self, text = "Fractal Renderer")
        self.Title.grid(row = 0, column = 0)

        #C
        self.C_min_label = Label(self, text = "C Min Value")
        self.C_min = Entry(self)
        self.C_max_label = Label(self, text="C Max Value")
        self.C_max = Entry(self)
        self.C_min_label.grid(row=1, column = 0)
        self.C_min.grid(row=1, column= 1)
        self.C_max_label.grid(row=2, column=0)
        self.C_max.grid(row=2, column=1)

        #Iterations
        self.Iter_label = Label(self, text = "Iterations")
        self.Iterations = Entry(self)
        self.Iter_label.grid(row = 3, column = 0)
        self.Iterations.grid(row = 3, column=1)

        #Z
        self.Z_label = Label(self, text = "Z")
        self.Z_value = Entry(self)
        self.Z_label.grid(row = 4, column = 0)
        self.Z_value.grid(row = 4, column = 1)

        #Scale
        self.Scale_label = Label(self, text = "Scale")
        self.Scale_value = Entry(self)
        self.Scale_label.grid(row=5, column=0)
        self.Scale_value.grid(row=5, column=1)

        #Enter
        self.Get = Button(self, text = "Enter", command = self.Enter)
        self.Get.grid(row = 6, column = 1)

        #Quit
        self.Quit = Button(self, text = "Quit", command = quit)
        self.Quit.grid(row = 6, column = 0)

    def Enter(self):
        print(self.C_min.get())
        print(self.C_max.get())
        print(self.Iterations.get())
        print(self.Scale_value.get())
        print(complex(self.Z_value.get()))

UI = create_UI()