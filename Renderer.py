from UI import *
import numpy
UI.mainloop()

root = Tk()

Image = Canvas(root, height = UI.winsize, width = UI.winsize)
Image.pack()

for x1 in range(0, UI.winsize+1):
    x = ((x1-(UI.winsize/2)) / UI.scale) + (UI.x_offset /UI.scale)

    for y1 in range(0, UI.winsize+1):
        y = ((y1-(UI.winsize/2)) / UI.scale) + (UI.y_offset/UI.scale)

        z = 0**UI.Z + complex(x, y)

        count = 0

        while count < UI.Iter:

            z = z**UI.Z + complex(x, y)

            count += 1
            if abs(z) >= 10000:
                count = UI.Iter

        if abs(z) <= 2:
            Image.create_rectangle(x1, y1, x1 + 1, y1 + 1, fill="black", outline="#%02x%02x%02x" % (0,0,0))


root.mainloop()

