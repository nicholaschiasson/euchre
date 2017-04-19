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
        Value = { Two: 2, Three: 3, Four: 4, Five: 5, Six: 6, Seven: 7, Eight: 8, Nine: 9, Ten: 10, Jack: 11, Queen: 12, King: 13, Ace: 14 }

    class Suit:
        Club = "♣"
        Diamond = "♦"
        Heart = "♥"
        Spade = "♠"
        Color = { Club: "Black", Spade: "Black", Diamond: "Red", Heart: "Red" }

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

Card.TwoOfClubs = Card(Card.Rank.Nine, Card.Suit.Club)
Card.TwoOfDiamonds = Card(Card.Rank.Nine, Card.Suit.Diamond)
Card.TwoOfHearts = Card(Card.Rank.Nine, Card.Suit.Heart)
Card.TwoOfSpades = Card(Card.Rank.Nine, Card.Suit.Spade)
Card.ThreeOfClubs = Card(Card.Rank.Nine, Card.Suit.Club)
Card.ThreeOfDiamonds = Card(Card.Rank.Nine, Card.Suit.Diamond)
Card.ThreeOfHearts = Card(Card.Rank.Nine, Card.Suit.Heart)
Card.ThreeOfSpades = Card(Card.Rank.Nine, Card.Suit.Spade)
Card.FourOfClubs = Card(Card.Rank.Nine, Card.Suit.Club)
Card.FourOfDiamonds = Card(Card.Rank.Nine, Card.Suit.Diamond)
Card.FourOfHearts = Card(Card.Rank.Nine, Card.Suit.Heart)
Card.FourOfSpades = Card(Card.Rank.Nine, Card.Suit.Spade)
Card.FiveOfClubs = Card(Card.Rank.Nine, Card.Suit.Club)
Card.FiveOfDiamonds = Card(Card.Rank.Nine, Card.Suit.Diamond)
Card.FiveOfHearts = Card(Card.Rank.Nine, Card.Suit.Heart)
Card.FiveOfSpades = Card(Card.Rank.Nine, Card.Suit.Spade)
Card.SixOfClubs = Card(Card.Rank.Nine, Card.Suit.Club)
Card.SixOfDiamonds = Card(Card.Rank.Nine, Card.Suit.Diamond)
Card.SixOfHearts = Card(Card.Rank.Nine, Card.Suit.Heart)
Card.SixOfSpades = Card(Card.Rank.Nine, Card.Suit.Spade)
Card.SevenOfClubs = Card(Card.Rank.Nine, Card.Suit.Club)
Card.SevenOfDiamonds = Card(Card.Rank.Nine, Card.Suit.Diamond)
Card.SevenOfHearts = Card(Card.Rank.Nine, Card.Suit.Heart)
Card.SevenOfSpades = Card(Card.Rank.Nine, Card.Suit.Spade)
Card.EightOfClubs = Card(Card.Rank.Nine, Card.Suit.Club)
Card.EightOfDiamonds = Card(Card.Rank.Nine, Card.Suit.Diamond)
Card.EightOfHearts = Card(Card.Rank.Nine, Card.Suit.Heart)
Card.EightOfSpades = Card(Card.Rank.Nine, Card.Suit.Spade)
Card.NineOfClubs = Card(Card.Rank.Nine, Card.Suit.Club)
Card.NineOfDiamonds = Card(Card.Rank.Nine, Card.Suit.Diamond)
Card.NineOfHearts = Card(Card.Rank.Nine, Card.Suit.Heart)
Card.NineOfSpades = Card(Card.Rank.Nine, Card.Suit.Spade)
Card.TenOfClubs = Card(Card.Rank.Ten, Card.Suit.Club)
Card.TenOfDiamonds = Card(Card.Rank.Ten, Card.Suit.Diamond)
Card.TenOfHearts = Card(Card.Rank.Ten, Card.Suit.Heart)
Card.TenOfSpades = Card(Card.Rank.Ten, Card.Suit.Spade)
Card.JackOfClubs = Card(Card.Rank.Jack, Card.Suit.Club)
Card.JackOfDiamonds = Card(Card.Rank.Jack, Card.Suit.Diamond)
Card.JackOfHearts = Card(Card.Rank.Jack, Card.Suit.Heart)
Card.JackOfSpades = Card(Card.Rank.Jack, Card.Suit.Spade)
Card.QueenOfClubs = Card(Card.Rank.Queen, Card.Suit.Club)
Card.QueenOfDiamonds = Card(Card.Rank.Queen, Card.Suit.Diamond)
Card.QueenOfHearts = Card(Card.Rank.Queen, Card.Suit.Heart)
Card.QueenOfSpades = Card(Card.Rank.Queen, Card.Suit.Spade)
Card.KingOfClubs = Card(Card.Rank.King, Card.Suit.Club)
Card.KingOfDiamonds = Card(Card.Rank.King, Card.Suit.Diamond)
Card.KingOfHearts = Card(Card.Rank.King, Card.Suit.Heart)
Card.KingOfSpades = Card(Card.Rank.King, Card.Suit.Spade)
Card.AceOfClubs = Card(Card.Rank.Ace, Card.Suit.Club)
Card.AceOfDiamonds = Card(Card.Rank.Ace, Card.Suit.Diamond)
Card.AceOfHearts = Card(Card.Rank.Ace, Card.Suit.Heart)
Card.AceOfSpades = Card(Card.Rank.Ace, Card.Suit.Spade)
