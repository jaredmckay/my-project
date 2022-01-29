import random 


class Card:

    def __init__(self):


        self.value = random.randint(1,13)

    def getvalue(self):
        return self.value

        