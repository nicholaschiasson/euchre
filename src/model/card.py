class Card:
    class Rank:
        Two = "2"
        Three = "3"
        Four = "4"
        Five = "5"
        Six = "6"
        Seven = "7"
        Eight = "8"
        Nine = "9"
        Ten = "10"
        Jack = "J"
        Queen = "Q"
        King = "K"
        Ace = "A"
        Joker = "JOKER"
        Value = { Two: 2, Three: 3, Four: 4, Five: 5, Six: 6, Seven: 7, Eight: 8, Nine: 9, Ten: 10, Jack: 11, Queen: 12, King: 13, Ace: 14, Joker: 15 }
    class Suit:
        Club = "♣"
        Diamond = "♦"
        Heart = "♥"
        Spade = "♠"
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return Card.Rank.Value[self.rank] < Card.Rank.Value[other.rank]
        return NotImplemented
    def __le__(self, other):
        if isinstance(other, self.__class__):
            return Card.Rank.Value[self.rank] <= Card.Rank.Value[other.rank]
        return NotImplemented
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.rank == other.rank and self.suit == other.suit
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented
    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))
