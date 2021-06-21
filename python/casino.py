import math
import random as rn
import time
# Blackjack

card_deck = ['A', 'K', 'Q', 'J', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def parseCard(x):
    if isinstance(x, int):
        return x
    else:
        return 10


rn.seed(time.time())


def pickCard():
    return card_deck[rn.randrange(len(card_deck))]


def startBJ():

    dDeck = [pickCard()]
    pDeck = [pickCard()]

    pDeck_sum = sum(map(parseCard, pDeck))
    dDeck_sum = sum(map(parseCard, dDeck))

    gameover = False

    while not gameover:

        print('-----------')
        print('P Deck:', *pDeck, 'Sum: %s' % pDeck_sum)
        print('D Deck:', *dDeck, 'Sum: %s' % dDeck_sum)
        print('-----------')

        if input('(H)it or (P)ass >').lower() == 'h':
            newCard = pickCard()
            pDeck.append(newCard)
            print('You hit %s! Sum: %s' % (newCard, pDeck_sum))
            pDeck_sum = sum(map(parseCard, pDeck))
        else:
            while dDeck_sum <= 16:
                dCard = pickCard()
                dDeck.append(dCard)
                dDeck_sum = sum(map(parseCard, dDeck))

                print('Dealer hit %s' % dCard)
            print('Dealer stands at %s' % dDeck_sum)

            if(dDeck_sum > 21 and pDeck_sum < dDeck_sum):
                print('Dealer Bust! You win!')
                gameover = True

            if(pDeck_sum == dDeck_sum and dDeck_sum > 16):
                print('Draw')
            if dDeck_sum <= 21 and pDeck_sum < dDeck_sum:
                print('Game Over! Sum: %d' % sum(map(parseCard, pDeck)))
            if pDeck_sum > dDeck_sum and dDeck_sum > 16:
                print('You win!')
            if dDeck_sum > pDeck_sum:
                print('You lose!')
            gameover = True

        if dDeck_sum <= 16:
            dCard = pickCard()
            dDeck.append(dCard)
            dDeck_sum = sum(map(parseCard, dDeck))

        if pDeck_sum > 21:
            print('Bust! Game Over! Sum: %d' % sum(map(parseCard, pDeck)))
            gameover = True

        elif pDeck_sum == 21 and dDeck_sum == 21:
            print('Draw!')
            gameover = True

        elif dDeck_sum > 21:
            print('You win!')
            gameover = True

    print('########')
    print('P Deck:', *pDeck, 'Sum: %s' % pDeck_sum)
    print('D Deck:', *dDeck, 'Sum: %s' % dDeck_sum)
    print('########')


startBJ()
# End Blackjack
