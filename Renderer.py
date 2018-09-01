from UI import *
import numpy
UI.mainloop()

root = Tk()

Image = Canvas(root, height = UI.winsize, width = UI.winsize)
Image.pack()

for x1 in range(0, UI.winsize+1):
    x = ((x1-(UI.winsize/2)) / UI.scale) + UI.x_offset

    for y1 in range(0, UI.winsize+1):
        y = ((y1-(UI.winsize/2)) / UI.scale) - UI.y_offset

        z = UI.Z**2 + complex(x, y)

        iters = 0
        count = 0

        while count < UI.Iter:

            z = z**2 + complex(x, y)

            count += 1
            iters += 1

            if abs(z) > 2:
                count = UI.Iter

            if abs(z) >= 10000:
                count = UI.Iter

        factor = (iters/UI.Iter)**(1/2)
        #print(factor)
        intensity = int(round(factor*UI.Iter))
        #print(intensity)

        if 2 < abs(z):
            Image.create_rectangle(x1, y1, x1 + 1, y1 + 1, fill="black", outline="#%02x%02x%02x" % (round(intensity),intensity,round(intensity)))

        if abs(z) <= 2:
            Image.create_rectangle(x1, y1, x1 + 1, y1 + 1, fill="black", outline="#%02x%02x%02x" % (0,0,0))

root.mainloop()
root.quit()
