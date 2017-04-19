from model.card import Card
from model.card_stack import CardStack
from view.euchre_app import EuchreApp

class Euchre:
    def __init__(self):
        self.restart_trick())
        self.view = EuchreApp("Euchre")

    def restart_tricks(self):
        self.deck = CardStack([])
        self.deck.place_card(Card(Card.Rank.Nine, Card.Suit.Club))
        self.deck.place_card(Card(Card.Rank.Nine, Card.Suit.Diamond))
        self.deck.place_card(Card(Card.Rank.Nine, Card.Suit.Heart))
        self.deck.place_card(Card(Card.Rank.Nine, Card.Suit.Spade))
        self.deck.place_card(Card(Card.Rank.Ten, Card.Suit.Club))
        self.deck.place_card(Card(Card.Rank.Ten, Card.Suit.Diamond))
        self.deck.place_card(Card(Card.Rank.Ten, Card.Suit.Heart))
        self.deck.place_card(Card(Card.Rank.Ten, Card.Suit.Spade))
        self.deck.place_card(Card(Card.Rank.Jack, Card.Suit.Club))
        self.deck.place_card(Card(Card.Rank.Jack, Card.Suit.Diamond))
        self.deck.place_card(Card(Card.Rank.Jack, Card.Suit.Heart))
        self.deck.place_card(Card(Card.Rank.Jack, Card.Suit.Spade))
        self.deck.place_card(Card(Card.Rank.Queen, Card.Suit.Club))
        self.deck.place_card(Card(Card.Rank.Queen, Card.Suit.Diamond))
        self.deck.place_card(Card(Card.Rank.Queen, Card.Suit.Heart))
        self.deck.place_card(Card(Card.Rank.Queen, Card.Suit.Spade))
        self.deck.place_card(Card(Card.Rank.King, Card.Suit.Club))
        self.deck.place_card(Card(Card.Rank.King, Card.Suit.Diamond))
        self.deck.place_card(Card(Card.Rank.King, Card.Suit.Heart))
        self.deck.place_card(Card(Card.Rank.King, Card.Suit.Spade))
        self.deck.place_card(Card(Card.Rank.Ace, Card.Suit.Club))
        self.deck.place_card(Card(Card.Rank.Ace, Card.Suit.Diamond))
        self.deck.place_card(Card(Card.Rank.Ace, Card.Suit.Heart))
        self.deck.place_card(Card(Card.Rank.Ace, Card.Suit.Spade))

    def run(self):
        self.view.mainloop()
