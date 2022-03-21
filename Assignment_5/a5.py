import random

ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = self.get_value()

    def get_value(self):
        if self.rank == "Ace":
            return 11
        elif self.rank == "Jack" or self.rank == "Queen" or self.rank == "King":
            return 10
        return int(self.rank)
    def get_rank(self):
        return self.rank

class Deck:
    def __init__(self):
        self.cards = []
        suitNum = 0
        rankNum = 0
        for x in range(0, 52):
            self.cards.append(Card(ranks[rankNum], suits[suitNum]))

            rankNum += 1
            if rankNum > 12:
                suitNum += 1
                rankNum = 0

    def shuffle(self):
        random.shuffle(self.cards)
    def deal_card(self):
        lastCard = self.cards[len(self.cards)-1]
        del self.cards[len(self.cards)-1]
        return lastCard

    def print_deck(self):
        for x in range(0, 52):
            print(self.cards[x].rank + " of " + self.cards[x].suit)

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)
    def count(self):
        return len(self.cards)
    def points(self):
        sum = 0
        ace = 0

        for x in self.cards:
            if x.get_rank == "Ace":
                ace += 1
            sum += x.get_value()
        if ace > 0 and sum > 21:
            sum -= (ace * 10)

        return sum

if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()

    print("HAND")
    hand = Hand()
    for i in range(3):
        hand.add_card(deck.deal_card())

    for i in range(hand.count()):
        card = hand.cards[i]
        print(card.rank + " of " + card.suit)

    print("Hand points:", hand.points())
