

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


if __name__ == '__main__':
    main()

"""
    #Splitting the tuple into a list of 2 tuples
    split = tuple(player_card[x:x + 1]
        for x in range(0, len(player_card), 1))
    print("result", list(split))
    if(split[])
"""