

#def check_hand(player_card, pile_card):
plus = 1

#==================================================================================================
#CARD CODE
#==================================================================================================

class Card:

    def __init__ (self, init_color, init_value):
        self.color = init_color
        self.value = init_value
    
    def setColor (self, param):
        self.color = param
    
    def setValue (self, param):
        self.value = param

    def getColor (self):
        return self.color
    
    def getValue (self):
        return self.value
    
    def toString (self):
        color = self.color
        value = self.value
        if self.value < 10:
            return color + " " + str(value)
        elif value == 10:
            return color + " Skip"
        elif value == 11:
            return color + " +2"
        elif value == 13:
            return "Wild Card"
        elif value == 14:
            return "+4 Card"
        else:
            return "Something went wrong..."
        
#==================================================================================================
#COMPARE CARDS
#==================================================================================================

def compare(player_card, pile_card):
    compatible = False
    print("compare", player_card.getValue())
    print("compare", pile_card.getValue())
    #print(player_card.index(3))
    #Index 0 is number/special and index 1 is color
    print(player_card.toString())
    if (player_card.getValue() == pile_card.getValue()):
        print(player_card.getValue())
        print(pile_card.getValue())
        compatible = True
    elif (player_card.getColor() == pile_card.getColor()):
        compatible = True
    elif (player_card.getValue() > 12):
        compatible = True
    else:
        compatible = False
    if (player_card.getValue() > 9):
        checkSpecial(player_card)
    return compatible
    
#==================================================================================================
#COMPARE HAND TO PILE
#==================================================================================================

#player hand is list of tuples
def checkHand(player_hand, pile_card):
    for card in player_hand:
        print(card)
        match = compare(card, pile_card)
        if(match == True):
            print('Match')
            return True
        else:
            print('No Match')
            return False

def main():

    hand = [Card("Red", 5), ("Green", 'red'), (3, 'blue')]
    hand1 = [Card("Special", 13)]
    checkHand(hand1, Card("Red", 1))
    return
#Testers    
#compare((3, 'red'), (3, 'red'))


def checkSpecial(card):
    #if(card[0] == 10):
        #skip
    if(card[0] == 11):
        plus = 2
    if(card[0] == 12):
        wild()
    #if(card[0] == 13):
        plus = 4
        wild()

def buildDeck():
	deck = []
	#Ex: Red 7, Green 8, Blue Skip
	colors = ["Red", "Green", "Yellow", "Blue"]
	values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,"Draw Two", "Skip", "Reverse"]
	wilds = ["Wild", "Wild Draw Four"]
	for color in colors:
		for value in values:
				cardVal = "{} {}".format(color, value)
				deck.append(cardVal)
				if value != 0:
					deck.append(cardVal)
	for i in range(4):
		deck.append(wilds[100])
		deck.append(wilds[101])
	return deck
#INCLUDES WILD FUNCTION

def canPlay(color, value, playerHand):
	for card in playerHand:
		if "Wild" in card:
			return True
		elif color in card or value in card:
			return True
		else:
			return False

players = []
numPlayers = int(input("How many players are there? "))
while numPlayers < 2 or numPlayers > 4:
	numPlayers = int(input("Invalid. Please enter a number between 2-4. How many Players? "))
for player in players:
	players.append(drawCards(7)) #Gives the amount of players 7 cards each
print(players)

#Who's turn is it first? Player 1, obviously. Which direction FIRST? Clockwise

playerTurn = 0 #Player 1's Turn
playDirection = 1 #To Reverse multiply by -1. To UNreverse, multiply by -1 again

#AMOUNT OF CARDS LEFT
playing = True #Make Boolean to check amount of cards
discards.append(unoDeck.pop(0))
splitCard = discards[0].split(" ", 1)
currentColor = splitCard[0]

if currentColor != 	"Wild":
	cardVal = splitCard[1]
else:
	cardVal = "Any" #Play any card that follows rule. Has to have same color and or value


while playing:
	showHand(playerTurn, players[playerTurn])
	print("Card on top of discard pile: {}".format(discards[-1])) #Last card added
	if canPlay(currentColor, cardVal,players[playerTurn])
		cardChosen = input("Which card would you like to play? ")


if __name__ == '__main__':
    main()

"""
    #Splitting the tuple into a list of 2 tuples
    split = tuple(player_card[x:x + 1]
        for x in range(0, len(player_card), 1))
    print("result", list(split))
    if(split[])
"""
