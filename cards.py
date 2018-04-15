# Набор базовых классов для карточной игры

class Card(object):
    """ Одна игральная карта """
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit, face_up=True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up


    def __str__(self):
        if self.is_face_up:
            rep = self.rank + self.suit
        else:
            rep = "XX"  # карта рубашкой вверх
        return rep


    def flip(self):
        self.is_face_up = not self.is_face_up


class Hand(object):
    """ 'Рука': набор карт на руках у одного игрока """

    def __init__(self):
        self.cards = []

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Deck(Hand):
    """ Колода игральных карт. """

    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))  # формируем колоду из 52 карт

    def shuffle(self):
        import random
        random.shuffle(self.cards)  # колода нужно перемешать

    def deal(self, hands, per_hand=1):  # раздача карт из колоды. Per_hand говорит, по сколько карт раздавать
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("He могу больше сдавать: карты закончились!")


if __name__ == "__main__":
    print("Этo модуль.содержащий классы для карточных игр.")
    input("\n\nHaжмитe Enter. чтобы выйти.")