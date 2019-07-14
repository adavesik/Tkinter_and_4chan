import Tkinter as tk
from PIL import ImageTk, Image

from chan import r4chan
from urllib2 import urlopen
from io import BytesIO


root = tk.Tk()
#root.geometry('1200x750')

img = ImageTk.PhotoImage(Image.open('logo.png'))
panel = tk.Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")

def callback(e):
    url = r4chan()
    u = urlopen(url[0])
    raw_data = u.read()
    u.close()
    im = Image.open(BytesIO(raw_data))
    basewidth = 600
    wpercent = (basewidth / float(im.size[0]))
    hsize = int((float(im.size[1]) * float(wpercent)))
    im = im.resize((basewidth, hsize), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(im)
    panel.configure(image=img2)
    panel.image = img2


root.bind("<Return>", callback)
root.mainloop()