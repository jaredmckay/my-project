# from ast import Pass
from game.card import Card

# Hi all - I started this Director file and I don't think I am doing it correctly. I am realizing now that I may have put some of the 
# code meant for the Card class in this file... 
# I am having a hard time separating the code into the different class files in my mind and am getting confused. 
# Feel free to make suggestions on how I can fix this :)
 
class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        card (List[Card]): A list of Card instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
#### I am missing how to pull the card value from the card class
# ### if that can be done I think rest of code will work

        self.CurrentCard = Card ## code for card value will need to go here
        self.is_playing = True
        self.score = 300


    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args: 
            self (Director): an instance of Director.
        """

        print(self.CurrentCard)

        while self.is_playing:
            self.get_inputs()
            # self.do_updates()
            self.do_outputs()


    def get_inputs(self):
        """Ask the user if they want to draw.
        
        Args:
            self (Director): an instance of Director.
        """

           

        # this will take the guess and compare against the cards will 
        # also tally points depending on guess
        guess = None

        while guess != "h" or "l":
            guess = input("Higher or Lower?  (h/l) ")
            card = self.CurrentCard
            newcard = Card()
            
            if guess.lower == "h":
                if newcard > card:
                    self.score + 100
                elif newcard < card:
                    self.score - 75
            elif guess.lower == "l":
                if newcard < card:
                    self.score + 100
                elif newcard > card:
                    self.score -75
        

#### I dont think this will be needed ###########
    # def do_updates(self):
    #     """Updates the player's score. 
        
    #     Args: 
    #         self (Director): an instance of Director.
    #     """
        

    #     return  

    def do_outputs(self):
        """Displays the card and the score. 
            Also asks the player if they want to draw again.
            
        Args: 
            self (Director): An instance of Director.
        """

        print(f"your score is {self.score}!")
        print(f"you card is {self.CurrentCard}")

        if self.sore <= 0:
            self.is_playing = False
            return
        
        play = None
        
        while play.lower != "n" or "y":
            play = input("play again? (y/n)")
            if play.lower == "n":
                self.is_playing = False
            elif play.lower == "y":
                break
    

            