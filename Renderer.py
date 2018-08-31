from UI import *
import numpy
UI.mainloop()

root = Tk()

Image = Canvas(root, height = UI.winsize, width = UI.winsize)
Image.pack()

for x1 in range(0, UI.winsize+1):
    x = (x1-(UI.winsize/2)) / UI.scale

    for y1 in range(0, UI.winsize+1):
        y = (y1-(UI.winsize/2)) / UI.scale

        z = 0**UI.Z + complex(x, y)

        count = 0

        while count < UI.Iter:

            z = z**UI.Z + complex(x, y)

            count += 1

            if abs(z) >= 10000:
                count = UI.Iter

        if 0 < abs(z) <= 0.25:
            Image.create_rectangle(x1, y1, x1 + 1, y1 + 1, fill="black", outline = "#3D1515")

        if 0.25 < abs(z) <= 0.5:
            Image.create_rectangle(x1, y1, x1 + 1, y1 + 1, fill="blue", outline = "#681E0D")

        if 0.5 < abs(z) <= 1:
            Image.create_rectangle(x1, y1, x1 + 1, y1 + 1, fill="orange", outline = "#A44200")

        if 2 < abs(z) <= 4:
            Image.create_rectangle(x1, y1, x1 + 1, y1 + 1, fill="yellow", outline = "#DBB060")

        if 1 < abs(z) <= 2:
            Image.create_rectangle(x1, y1, x1 + 1, y1 + 1, fill="red", outline = "#FFD166")

root.mainloop()

