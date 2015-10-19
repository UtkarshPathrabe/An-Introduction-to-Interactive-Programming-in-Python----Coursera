# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
inPlay = False
outcome = ""
score = 0
playerString = "PLAYER"
dealerString = "DEALER"

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
    def draw_back(self, canvas, pos):
        card_loc = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0] + 1, pos[1] + CARD_BACK_CENTER[1] + 1], CARD_BACK_SIZE)

# define hand class
class Hand:
    def __init__(self):
        """ Creates Hand object """
        self.cards = []

    def __str__(self):
        """ Returns a string representation of a hand """
        handCards = ""
        for card in self.cards:
            handCards = handCards + str(card) + " "
        if len(handCards) == 0:
            return "Hand contains nothing."
        else:
            return "Hand contains " + handCards.strip() + "."

    def add_card(self, card):
        """ Adds a card object to a hand """
        self.cards.append(card)

    def get_value(self):
        """ Computes the value of the hand """
        """ Counts aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust """
        currentValue = 0
        isAcePresent = False
        for card in self.cards:
            rank = card.get_rank()
            currentValue += VALUES[rank]
            if rank == 'A':
                isAcePresent = True
        if isAcePresent and currentValue < 12:
            currentValue += 10
        return currentValue
   
    def draw(self, canvas, pos):
        """ Draws a hand on the canvas, uses the draw method for cards """
        for card in self.cards:
            pos[0] = pos[0] + CARD_SIZE[0] + 30
            card.draw(canvas, pos)
 
        
# define deck class 
class Deck:
    def __init__(self):
        """ Creates a Deck object """
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        """ Shuffles the deck, using random.shuffle() """
        random.shuffle(self.cards)

    def deal_card(self):
        """ Deals a card object from the deck """
        return self.cards.pop()
    
    def __str__(self):
        """ Returns a string representing the deck """
        deckCards = ""
        for card in self.cards:
            deckCards = deckCards + str(card) + " "
        if len(deckCards) == 0:
            return "Deck contains nothing."
        else:
            return "Deck contains " + deckCards.strip() + "."


#define event handlers for buttons
def deal():
    global outcome, score, inPlay, deck, playerHand, dealerHand, message
    if inPlay:
        inPlay = False
        score -= 1
        deal()
    else:
        playerHand = Hand()
        dealerHand = Hand()
        deck = Deck()
        deck.shuffle()
        playerHand.add_card(deck.deal_card())
        playerHand.add_card(deck.deal_card())
        dealerHand.add_card(deck.deal_card())
        dealerHand.add_card(deck.deal_card())
        outcome = "Hit or Stand?"
        message = ""
        inPlay = True

def hit():
    global message, outcome, score, inPlay, deck, playerHand
    if inPlay:
        if playerHand.get_value() <= 21:
            playerHand.add_card(deck.deal_card())
            if playerHand.get_value() > 21:
                message = "You are BUSTED! You loose."
                score -= 1
                outcome = "New Deal?"
                inPlay = False
       
def stand():
    global message, playerHand, dealerHand, score, inPlay, deck, outcome
    if inPlay:
        while dealerHand.get_value() < 17:
            dealerHand.add_card(deck.deal_card())
        if dealerHand.get_value() > 21:
            message = "Dealer BUSTED! You win."
            score += 1
        elif playerHand.get_value() > dealerHand.get_value():
            message = "You win."
            score += 1
        else:
            message = "You loose."
            score -= 1
        outcome = "New Deal?"
        inPlay = False

# draw handler    
def draw(canvas):
    canvas.draw_text("BLACKJACK", (150, 70), 50, "Aqua")
    canvas.draw_text(dealerString, (36, 185), 30, "Black")
    canvas.draw_text(playerString, (36, 385), 30, "Black")
    canvas.draw_text(outcome, (235, 385), 30, "Black")
    canvas.draw_text(message, (235, 185), 30, "Black")
    canvas.draw_text("Score " + str(score), (450, 115), 30, "Black")
    dealerHand.draw(canvas, [-65, 200])
    playerHand.draw(canvas, [-65, 400])
    if inPlay:
        dealerHand.cards[0].draw_back(canvas, [36, 199])

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()

# remember to review the gradic rubric