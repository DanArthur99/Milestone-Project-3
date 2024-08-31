# Music Gear Review - Testing Document

## CONTENTS
* [Manual Testing](#Manual-Testing)
  * [Full Testing](#Full-Testing)
* [W3C Validator](#W3C-Validator)
* [Lighthouse Testing](#Lighthouse-Testing)
* [Wave Accessibiliy Testing](#Wave-Accessibility-TSesting)
* [Python Checker](#Python-Checker)
* [Bugs](#Bugs)
  * [Solved Bugs](#Solved-Bugs)
* [Testing User Stories](#Testing-User-Stories)

## Manual Testing

### Full Testing

The site was tested on the following systems:

* Cyberpower Ryzen 5 - OS: Windows 11 v23H2
* Samsung Galaxy A52S 5G

This was also tested on the following browsers:

* Google Chrome - Version 125.0.6422.77 (64-bit)
* Microsoft Edge - Version 125.0.2535.51 (64-bit)
* Mozilla Firefox - Version 126.0 (64-bit)

#### Home Page Testing

**Feature**|**Expected Outcome**|**Test Action**|**Result**|**Pass/Fail**
:-----:|:-----:|:-----:|:-----:|:-----:
Rules Modal Home Page|Rules modal should appear|Click Rules button|Rules modal opened|Pass
Rules Modal Home Page (Phone Size Screen)|Rules modal should appear|Click Rules button|Rules modal opened|Pass
Start Game Button Large Screens|HTML updates to username enter field|Click Start New Game button|HTML updates|Pass
Start Game Button Phone Size Screens|HTML updates to username enter field|Click Start New Game button|HTML updates|Pass
Username Empty Check|User is prompted for username|Click Start Game with empty text field|user cannot proceed|Pass
Username Not Empty Check|user is taken to the game page|Press the Start Game button with value in text field|game.html is loaded|Pass

#### Game Page Testing

**Test**|**Expected Outcome**|**Test Action**|**Result**|**Pass/Fail**
:-----:|:-----:|:-----:|:-----:|:-----:
API data fetch test |API fetches the deck data from the Deck of Cards API|Pause code and console.log(response)|![API Response](docs/readme-images/API-response.png)|Pass
Card Choice test|Displays the options to play the selected card -  yes or no|Click a clickable card|Play card button section is displayed|Pass
Card Choice - Phone Screens|Displays the play card options in a modal|Click a clickable card|Play card modal is displayed|Pass
Yes Button test|Lays the card to the pile and calls the next turn - card is removed from player's hand|Click play card? - yes|Card is played and next turn is called. Card is also removed from hand|Pass
No Button test|removes play card options|Click play card? - no|play card button section removed|Pass
Rules Button Game Page|displays the rules modal when clicked|Click Rules button|Rules modal displayed|Pass
Exit Button test|displays a modal asking if the player is sure|Click Exit button|Modal displayed|Pass
Game State text field test|displays text showing what action has just happened with each turn|take Player turn|Text updates with each turn e.g. Player lays 4 of HEARTS|Pass
Clicking an 8 Card|Displays a different set of buttons that allows the user to choose a suit as well|Clicking a card with the value of 8|Displays a 4 yes options with each suit labelled and a no button to cancel the choice|Pass
Clicking an 8 Card - Phone Screens|Displays a different modal that allows the user to choose a suit as well|Clicking a card with the value of 8|Displays a modal with  4 yes options with each suit labelled and a no button to cancel the choice|Pass
Clubs Button test|"The next player must then lay down club| or an 8"|Clicking the clubs button|The next player lays a club
Hearts Button test|The next player must then lay down heart or an 8|Clicking the hearts button|The next player lays a heart|Pass
Spades Button test|The next player must then lay down spade or an 8|Clicking the spades button|The next player lays a spade|Pass
Diamonds Button test|The next player must then lay down diamond or an 8|Clicking the diamonds button|The next player lays a diamond|Pass
Jack card functionality|Laying a Jack skips the next players go|Lay a Jack Card|The next players turn is skipped|Pass
2 Card functionality|Laying a 2 should mean the next player has to lay a 2 or draw 2 cards|Lay a 2 Card|The next player draws 2 cards|Pass
2 card accumulation functionality|If the user lays a 2 and the next player lays a 2 then cards needed to be drawn should accumulate to 4|Lay a 2 Card while the next player also has a 2|The next player after draws 4 cards. Also can add pauses to the code and console.log the gameState.draw2Cards property with each turn to see it increase by 2 each time.|Pass
Ace card functionality|Laying an Ace changes the direction of play|Lay an Ace|The direction of play inverses|Pass
Ace of Spades functionality|Laying an Ace of Spades changes the direction of play while also forcing the next player to either draw 6 cards. Or they lay an Ace of Spades themselves|Lay an Ace of Spades|The direction of play inverses and the next player draws 6 cards. Also can add a pause to the code and console.log the gameStates.draw6Cards property to see that a value has been added.|Pass
Ace of Spades accumulation functionality|If the next player also lays an Ace of Spades, then the direction of play changes again and the next player is forced to draw 12 cards|Lay an Ace of Spades while the next player also has an Ace of Spades|The direction of play changes with each turn and the user is forced to draw 12 cards|Pass
Play Again button|Once the game has ended the user is prompted to start a new game. When this is clicked the game resets|Click of Start New Game at game completion|Game resets and starts again|Pass
Score incrementation test|Once the game is over the player that has won has theyre score incremented by one. This is then displayed on their personal score on screen in the next game.|Complete Game. Click Start New Game|Winning player score increments by 1 at game completion. Winning players score is visible on Game reset.|Pass
Draw Card test|If the user cannot go, then the draw card button appears. Clicking it should add a new card to their hand and display it on screen|Click the draw card button when it appears|New card appears on screen. Can pause the code to console.log the gameArrays.playerHand array to see that a new card object has been added|Pass
Draw 2 Cards receiving end - can go|If the previous player lays a 2, then the only legal card to lay would be a 2 also. The draw2Cards value should also increment by 2|Wait until the previous player lays a 2|All cards are blanked out apart from ones with value 2. Upon playing, the draw2Cards value increments to 4. This can be seen by pausing the code and logging the value to the console.|Pass
Draw 2 cards receiving end - cannot go|If the previous player lays a hand and the user does not have a 2 in their hand. Then they should be forced to draw 2 cards|Wait until the previous player lays a 2|All cards are blanked out as no legal cards. Draw 2 cards button appears|Pass
Draw Card empty shuffledPile test|if the shuffledPile is empty then the contents of the discardPile should be pushed to it and then emptied|Wait until the shuffledPile.length is 0. Then call drawCardPlayerClick() from the console.|By logging the gameArrays to the console you can see that the shuffledPile now has objects inside the array. While the discardPile is empty|Pass
Draw Card empty shuffledPile AND empty discardPile test|In the rare occurrence that both are empty the the game should end and prompt the user to start a new game|Call the drawCard function with the gameArrays.playerHand and the username string as parameters in the console, until both the discardPile and shuffledPile arrays are empty. Then call the drawCardPlayerClick function in the console.|The end of game text appears saying that we seem to be out of cards. The Start New Game button also appears|Pass

#### 404 Page Testing

**Test**|**Expected Outcome**|**Test Action**|**Result**|**Pass/Fail**
:-----:|:-----:|:-----:|:-----:|:-----:
Loads correctly|If the page url is unrecognized or non existantthen the 404 page should load in its place|Typed in random characters after the base URL|404 Page loads correctly|Pass
Home button test|Should take the user back to the Home page when click|Click Go Back Home Button|Home Page Loads|Pass

## Python Linter

### __init.py

![Init.py Linter](docs/readme-images/init-linter.png)

### run.py

![Run.py Linter](docs/readme-images/linter-pass.png)

### forms.py

![Forms.py Linter](docs/readme-images/linter-pass.png)

### model.py

![Model.py Linter](docs/readme-images/linter-pass.png)

### routes.py

![Routes.py Linter](docs/readme-images/linter-pass.png)

## W3C Validator

# Home Page

# Login Page

# Sign Up Page

# Brands Page

# Categories Page

# Search Page

# Add Product Page

# Dashboard

### Stylesheet Validator

![W3C-Stylesheet](docs/readme-images/w3c-stylesheet.png)

## Wave Accessibility Testing

### Home Page

## Testing User Stories

### Client Goals

1. To have a game that is viewable and playable on different screen sizes

Desktop:

![Game Page Desktop Image](docs/testing/game-page-large-screen.png)

Mobile:

![Game Page Mobile Image](docs/testing/game-page-small-screen.png)

2. To have a crazy eights game that is logically functional and easy to follow

* Please refer to the [Manual Testing](#Manual-Testing) section for this

3. To have an overall website that is clear and easy to navigate

![Home Page](docs/testing/home-page.png)
![Rules Modal](docs/testing/modal.png)
![Exit Game Modal](docs/testing/exit-game.png)

* The overall website is easy to navigate and use, and the user can easily access the rules and exit the game.

### First Time Visit Goals

1. To be able to set a user name for the game

![Enter Username](docs/testing/enter-username.png)

2. To have a score incrementer that keeps track of how many rounds of the game have been won by each player

![Game Complete](docs/testing/game-complete.png)
![Score Increment](docs/testing/score-increment.png)

3. To be able to see the rules at any point in the game (to help first time player get to grips with the game)

![Game Page Rules](docs/testing/game-page-rules.png)

### Returning Visitor Goals

1. To make sure the game has a good and easily usable UI that makes it as easy as possible for the player to use/play

![Home Page](docs/testing/home-page.png)
![Game Page Desktop Image](docs/testing/game-page-large-screen.png)

2. To have the styling and layout visually pleasing so that players don't get visually bored.

![Home Page](docs/testing/home-page.png)
![Game Page Desktop Image](docs/testing/game-page-large-screen.png)
  
3. To have the Game functionality fully working will all rules in place, and any errors as minimal as possible

* Please refer to the [Manual Testing](#Manual-Testing) section for this


