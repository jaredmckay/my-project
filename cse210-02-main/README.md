# cse210-02
Programming with clases

First class will be the Director class. 
    
    constructor
        constructs a new director
        self.card
        self.is_playing
        self.score
        self.total_score

    start_game
        starts the game by running the main game loop
        self.get_inputs()
        self.do_updates()
        self.do_outputs()
    
   get_inputs
        ask the player if they want to draw
        draw_card
        self.is_playing
    
    do_updates
        generate an account for the player

    do_outputs
        displays the cards and the score. also asks if player wants to play again. 

Second class will be the Card class.

    The player wins 100 points if guess correctly. Player loses 75 points if guess incorrectly.

    constructor
        constructs a new instance of card
    
    draw
        generates random value of card between 1-13 and then calculates the points.
        