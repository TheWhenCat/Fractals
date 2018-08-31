from tkinter import *

class create_UI(Tk):

    def __init__(self):

        Tk.__init__(self)

        #Title
        self.Title = Label(self, text = "Fractal Renderer")
        self.Title.grid(row = 0, column = 0)

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

        #Offsets
        self.x_offset_label = Label(self, text="X-Offset")
        self.x_offset = Entry(self)
        self.y_offset_label = Label(self, text="Y-Offset")
        self.y_offset = Entry(self)
        self.Scale_label.grid(row=5, column=0)
        self.Scale_value.grid(row=5, column=1)
        self.Scale_label.grid(row=5, column=0)
        self.Scale_value.grid(row=5, column=1)

        #Window
        self.Window_label = Label(self, text = "Window")
        self.Win_value = Entry(self)
        self.Window_label.grid(row = 6, column = 0)
        self.Win_value.grid(row = 6, column = 1)

        #Enter
        self.Get = Button(self, text = "Enter", command = self.Enter)
        self.Get.grid(row = 7, column = 1)

        #Quit
        self.Quit = Button(self, text = "Quit", command = quit)
        self.Quit.grid(row = 7, column = 0)

    def Enter(self):

        print("=" * 100)
        print("Fractal Information:")

        if len(self.Iterations.get()) == 0:
            print("You have entered no value for the Iterations, the default is 10")
            self.Iter = 10
        elif len(self.Iterations.get()) > 0:
            self.Iter = int(self.Iterations.get())
            print("Iterations: {}".format(self.Iter))

        if len(self.Scale_value.get()) == 0:
            print("You have entered no value for the Scale, the default is 100")
            self.scale = 100
        elif len(self.Scale_value.get()) > 0:
            self.scale = int(self.Scale_value.get())
            print("Scale: {}".format(self.scale))

        if len(self.Z_value.get()) == 0:
            print("You have entered no value for the Z, the default is 0")
            self.Z = int(2)
        elif len(self.Z_value.get()) > 0:
            try:
                self.Z = int(self.Z_value.get())
                print("Z: {}".format(self.Z))
            except:
                raise ValueError("Please enter a complex number (0 + 4j)")

        if len(self.Win_value.get()) == 0:
            print("You have entered no value for the Window, the default is 400")
            self.winsize = 400
        elif len(self.Win_value.get()) > 0:
            self.winsize = int(self.Win_value.get())
            print("Window: {}".format(self.winsize))

        print("=" * 100)

        UI.quit()
        UI.destroy()


UI = create_UI()