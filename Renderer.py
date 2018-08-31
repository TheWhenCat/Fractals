from UI import *
UI.mainloop()

root = Tk()

Image = Canvas(root, height = UI.winsize, width = UI.winsize)
Image.pack()

for x1 in range(0, UI.winsize+1):
    x = (x1-(UI.winsize/2)) / UI.scale

    for y1 in range(0, UI.winsize+1):
        y = (y1-(UI.winsize/2)) / UI.scale

        for i in range(int(UI.C_min), int(UI.C_max)):

            z = complex(x, y) ** 2 + i

            count = 0

            while count < UI.Iter:

                z = z**2 + i

                count += 1

                if abs(z) >= 10000:
                    count = UI.Iter

            if abs(z) <= 0.5:
                Image.create_rectangle((x1, y1, x1 + 1, y1 + 1), fill="black")
            
            if 0.5 < abs(z) <= 1:
                Image.create_rectangle((x1, y1, x1 + 1, y1 + 1), fill="green")

            if 1 < abs(z) <= 2:
                Image.create_rectangle((x1, y1, x1 + 1, y1 + 1), fill="blue")

            if 2 < abs(z) <= 100:
                Image.create_rectangle((x1, y1, x1 + 1, y1 + 1), fill="orange")

root.mainloop()

