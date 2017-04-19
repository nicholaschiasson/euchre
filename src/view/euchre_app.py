from tkinter import Tk, BOTH, W, N, E, S
from tkinter.ttk import Frame, Button, Label, Style

class EuchreApp(Tk):
    def __init__(self, title, controller, user_player):
        self.user_player = user_player
        Tk.__init__(self)
        self.title(title)
        self.centerWindow()

        self.w = Frame(self)
        self.w.pack(fill=BOTH, expand=1)
        for x in range(15):
            self.w.columnconfigure(x, weight=1)
        self.w.rowconfigure(2, weight=1)
        self.w.rowconfigure(5, weight=1)
        self.w.rowconfigure(7, weight=1)

        Style().configure("playerhand.TButton", background="white")
        Style().configure("otherhand.TButton", background=("#888888" if user_player else "white"))

        self.lblTitle = Label(self.w, text="Euchre")
        self.lblTitle.grid(row=0, column=5, columnspan=5)

        # Center Table
        self.btnDeck = Button(self.w, text="Deck", state="disabled")
        self.btnDeck.grid(row=3, column=5, rowspan=3, columnspan=2, sticky=N+S+E+W)
        self.lblTrump = Label(self.w, text="Trump: ")
        self.lblTrump.grid(row=3, column=7, columnspan=3)
        self.lblCurrentPlayer = Label(self.w, text="Current Player: ")
        self.lblCurrentPlayer.grid(row=4, column=7, columnspan=3)
        self.btnDeal = Button(self.w, text="Deal", command=lambda:controller.deal())
        self.btnDeal.grid(row=3, column=7, rowspan=3, columnspan=3, sticky=N+S+E+W)

        def player_choose_card_callback_factory(player, card):
            return lambda: controller.player_choose_card(player, card)

        # Player 1 hand
        self.lblPlayer1Title = Label(self.w, text=("You" if user_player else "Player 1"))
        self.lblPlayer1Title.grid(row=6, column=5, columnspan=5)
        self.btnPlayer1Cards = []
        for i in range(5):
            self.btnPlayer1Cards.append(Button(self.w, command=player_choose_card_callback_factory(0, i), state="disabled", style="playerhand.TButton"))
            self.btnPlayer1Cards[i].grid(row=7, column=5+i, sticky=N+S+E+W)

        # Player 2 hand
        self.lblPlayer2Title = Label(self.w, text="Player 2")
        self.lblPlayer2Title.grid(row=3, column=0, columnspan=5)
        self.btnPlayer2Cards = []
        for i in range(5):
            self.btnPlayer2Cards.append(Button(self.w, command=player_choose_card_callback_factory(1, i), state="disabled", style="otherhand.TButton"))
            self.btnPlayer2Cards[i].grid(row=4, column=0+i, rowspan=2, sticky=N+S+E+W)

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
            self.btnPlayer4Cards[i].grid(row=4, column=10+i, rowspan=2, sticky=N+S+E+W)

    def centerWindow(self):
        w = 1000
        h = 600

        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def restart_trick(self, dealer):
        self.btnDeal.grid()
        self.lblPlayer1Title.config(text=("You" if self.user_player else "Player 1") + (": dealer" if dealer % 4 == 0 else ""))
        self.lblPlayer2Title.config(text="Player 2" + (": dealer" if dealer % 4 == 1 else ""))
        self.lblPlayer3Title.config(text="Player 3" + (": dealer" if dealer % 4 == 2 else ""))
        self.lblPlayer4Title.config(text="Player 4" + (": dealer" if dealer % 4 == 3 else ""))
        for c in self.btnPlayer1Cards:
            c.config(text="")
        for c in self.btnPlayer2Cards:
            c.config(text="")
        for c in self.btnPlayer3Cards:
            c.config(text="")
        for c in self.btnPlayer4Cards:
            c.config(text="")

    def deal(self, trump):
        self.btnDeal.grid_remove()
        self.lblTrump.config(text="Trump: " + str(trump))

    def update_player_hand(self, player, player_num):
        if player_num == 0:
            for c in self.btnPlayer1Cards:
                c.config(text="")
                c.grid_remove()
            for i, c in enumerate(player.hand.cards):
                self.btnPlayer1Cards[i].grid()
                self.btnPlayer1Cards[i].config(text=str(c.rank) + str(c.suit))
        elif player_num == 1:
            for c in self.btnPlayer2Cards:
                c.config(text="")
                c.grid_remove()
            for i, c in enumerate(player.hand.cards):
                self.btnPlayer2Cards[i].grid()
                if self.user_player:
                    self.btnPlayer2Cards[i].config(text="???")
                else:
                    self.btnPlayer2Cards[i].config(text=str(c.rank) + str(c.suit))
        elif player_num == 2:
            for c in self.btnPlayer3Cards:
                c.config(text="")
                c.grid_remove()
            for i, c in enumerate(player.hand.cards):
                self.btnPlayer3Cards[i].grid()
                if self.user_player:
                    self.btnPlayer3Cards[i].config(text="???")
                else:
                    self.btnPlayer3Cards[i].config(text=str(c.rank) + str(c.suit))
        elif player_num == 3:
            for c in self.btnPlayer4Cards:
                c.config(text="")
                c.grid_remove()
            for i, c in enumerate(player.hand.cards):
                self.btnPlayer4Cards[i].grid()
                if self.user_player:
                    self.btnPlayer4Cards[i].config(text="???")
                else:
                    self.btnPlayer4Cards[i].config(text=str(c.rank) + str(c.suit))

    def activate_player_turn(self, player, player_num):
        if player_num == 0:
            for i, c in enumerate(player.hand.cards):
                self.btnPlayer1Cards[i].config(state="enabled")
        if player_num == 1:
            for i, c in enumerate(player.hand.cards):
                self.btnPlayer2Cards[i].config(state="enabled")
        if player_num == 2:
            for i, c in enumerate(player.hand.cards):
                self.btnPlayer3Cards[i].config(state="enabled")
        if player_num == 3:
            for i, c in enumerate(player.hand.cards):
                self.btnPlayer4Cards[i].config(state="enabled")

    def deactivate_player_turn(self, player, player_num):
        if player_num == 0:
            for i, c in enumerate(player.hand.cards):
                self.btnPlayer1Cards[i].config(state="disabled")
        if player_num == 1:
            for i, c in enumerate(player.hand.cards):
                self.btnPlayer2Cards[i].config(state="disabled")
        if player_num == 2:
            for i, c in enumerate(player.hand.cards):
                self.btnPlayer3Cards[i].config(state="disabled")
        if player_num == 3:
            for i, c in enumerate(player.hand.cards):
                self.btnPlayer4Cards[i].config(state="disabled")

    def update_current_player(self, player_num):
        self.lblCurrentPlayer.config(text="Current Player: " + str(player_num))

    def player_play_card(self, player, player_num, card):
        self.update_player_hand(player, player_num)
