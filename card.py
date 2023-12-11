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
        elif value == 100:
            return "Wild Card"
        elif value == 101:
            return "+4 Card"
        else:
            return "Something went wrong..."

peep = carp.getValue()
print(peep)

