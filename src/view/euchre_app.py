from tkinter import Tk, BOTH, W, N, E, S
from tkinter.ttk import Frame, Button, Label, Style

class EuchreApp(Tk):
    def __init__(self, title, controller, user_player):
        Tk.__init__(self)
        self.title(title)
        self.centerWindow()

        self.w = Frame(self)
        self.w.pack(fill=BOTH, expand=1)
        for x in range(15):
            self.w.columnconfigure(x, weight=1)
        for y in range(2, 7, 2):
            self.w.rowconfigure(y, weight=1)

        Style().configure("playerhand.TButton", background="white")
        Style().configure("otherhand.TButton", background=("#888888" if user_player else "white"))

        self.lblTitle = Label(self.w, text="Euchre")
        self.lblTitle.grid(row=0, column=5, columnspan=5)

        # Center Table
        self.btnDeck = Button(self.w, text="Deck", state="disabled")
        self.btnDeck.grid(row=3, column=5, rowspan=2, columnspan=2, sticky=N+S+E+W)
        self.btnDeal = Button(self.w, text="Deal", command=lambda:controller.deal())
        self.btnDeal.grid(row=3, column=7, rowspan=2, columnspan=3, sticky=N+S+E+W)

        def player_choose_card_callback_factory(player, card):
            return lambda: controller.player_choose_card(player, card)

        # Player 1 hand
        self.lblPlayer1Title = Label(self.w, text=("You" if user_player else "Player 1"))
        self.lblPlayer1Title.grid(row=5, column=5, columnspan=5)
        self.btnPlayer1Cards = []
        for i in range(5):
            self.btnPlayer1Cards.append(Button(self.w, command=player_choose_card_callback_factory(0, i), state="disabled", style="playerhand.TButton"))
            self.btnPlayer1Cards[i].grid(row=6, column=5+i, sticky=N+S+E+W)

        # Player 2 hand
        self.lblPlayer2Title = Label(self.w, text="Player 2")
        self.lblPlayer2Title.grid(row=3, column=0, columnspan=5)
        self.btnPlayer2Cards = []
        for i in range(5):
            self.btnPlayer2Cards.append(Button(self.w, command=player_choose_card_callback_factory(1, i), state="disabled", style="otherhand.TButton"))
            self.btnPlayer2Cards[i].grid(row=4, column=0+i, sticky=N+S+E+W)

        # Player 3 hand
        self.lblPlayer3Title = Label(self.w, text="Player 3")
        self.lblPlayer3Title.grid(row=1, column=5, columnspan=5)
        self.btnPlayer3Cards = []
        for i in range(5):
            self.btnPlayer3Cards.append(Button(self.w, command=player_choose_card_callback_factory(2, i), state="disabled", style="otherhand.TButton"))
            self.btnPlayer3Cards[i].grid(row=2, column=5+i, sticky=N+S+E+W)

        # Player 4 hand
        self.lblPlayer4Title = Label(self.w, text="Player 4")
        self.lblPlayer4Title.grid(row=3, column=10, columnspan=5)
        self.btnPlayer4Cards = []
        for i in range(5):
            self.btnPlayer4Cards.append(Button(self.w, command=player_choose_card_callback_factory(3, i), state="disabled", style="otherhand.TButton"))
            self.btnPlayer4Cards[i].grid(row=4, column=10+i, sticky=N+S+E+W)

    def centerWindow(self):
        w = 1000
        h = 600

        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def restart_trick(self):
        pass
