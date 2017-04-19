from tkinter import Tk, Frame, BOTH, Button

class EuchreApp(Tk):
    def __init__(self, title):
        Tk.__init__(self)
        self.title(title)
        self.centerWindow()

        self.w = Frame(self)
        self.w.pack(fill=BOTH, expand=1)

    def centerWindow(self):
        w = 800
        h = 600

        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
