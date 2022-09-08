import collections
Card = collections.namedtuple('Card',['rank','suit'])

# 有序的纸牌
class FrenchDeck:
    ranks = [str(n) for n in range(2,11)]+list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits
                                      for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

class Point:
    def __int__(self,x = 0,y = 0 ):
      self.x = x
      self.y = y



if __name__ == '__main__':
    s1 = "python:校验数据，自动化的检测脚本书写"
    print(s1)
    beer_card = Card('7','diamonds')
    deck = FrenchDeck()
    print(len(deck))