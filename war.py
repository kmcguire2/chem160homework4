from cards import *

ngames = 10000
winsby = [0] * 27

for i in range(ngames):
    p1wins = 0
    p2wins = 0
    p1deck = deck()
    p1deck.shuffle()
    p2deck = deck()
    p2deck.shuffle()
    for j in range(52):
        p1card = p1deck.dealcard()
        p2card = p2deck.dealcard()
        if p1card.value() > p2card.value():
            p1wins += 1
        if p1card.value() < p2card.value():
            p2wins += 1
    winsby[int(abs(p1wins-p2wins))] += 1

for i in range(27):
    print("%2d %5.2f" % (i*2, winsby[i]/ngames))
