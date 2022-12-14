import collections

Card = collections.namedtuple("Card", ["rank", "suit"])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


if __name__ == "__main__":
    card = Card("7", "club")
    print(card)

    frenchdeck = FrenchDeck()
    # __len__ allows the len() method to be used
    print(len(frenchdeck))
    # __getitem__ allows for indexing and looping to be used
    print(frenchdeck[0:10])
    for card in frenchdeck:
        print(card)
