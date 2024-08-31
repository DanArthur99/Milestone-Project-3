# Music Gear Review - Testing Document

## CONTENTS
* [Manual Testing](#Manual-Testing)
  * [Full Testing](#Full-Testing)
    * [Home Page Testing](#Home-Page-Testing)
    * [Game Page Testing](#Game-Page-Testing)
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

## Unit testing 

* Unit testing was performed on the script.js file.
* This was to test the functionality of specific functions within the file, specifically if they manipulate and the parameters in the correct way.
* The functions tested included the resetAll, dealHand, several game state setters and game state checker, as well as others.
* The results of this can be seen below:

![Unit Testing Results Image 1](docs/testing/unit-testing-results.png)
![Unit Testing Results Image 1](docs/testing/unit-testing-results-2.png)

* As you can, 32 different unit test were performed, with all 32 passing. 


## W3C Validator

### Home Page

![Home Page W3C Validator](docs/testing/index-page-w3c-validation.png)

### Game Page

![Game Page W3C Validator](docs/testing/game-page-w3c-validation.png)

### 404 Page

![404 Page W3C Validator](docs/testing/404-page-w3c-validation.png)

### Stylesheets

#### Main Stylesheet

![Stylesheet W3C Validator](docs/testing/stylesheet-w3c-validation.png)

#### Title Page Only Stylesheet

![Title Page Stylesheet W3C Validator](docs/testing/title-page-stylesheet-w3c-validation.png)

## Lighthouse Testing

### Home Page

#### Desktop

![Home Page Desktop Lighthouse Test](docs/testing/index-page-lighthouse-test-desktop.png)

#### Mobile

![Home Page Mobile Lighthouse Test](docs/testing/index-page-lighthouse-test-mobile.png)

### Game Page

#### Desktop

![Game Page Desktop Lighthouse Test](docs/testing/game-page-lighthouse-test-desktop.png)

#### Mobile

![Game Page Mobile Lighthouse Test](docs/testing/game-page-lighthouse-test-mobile.png)

### 404 Page

#### Desktop

![404 Page Lighthouse Test](docs/testing/404-page-lighthouse-test-desktop.png)

#### Mobile

![404 Page Lighthouse Test](docs/testing/404-page-lighthouse-test-mobile.png)

## Wave Accessibility Testing

### Home Page

![Home Page Wave Test Summary](docs/testing/index-page-wave-accessibility-summary.png)

![Home Page Wave Test Details](docs/testing/index-page-wave-accessibility-details.png)

### Game Page

![Game Page Wave Test Summary](docs/testing/game-page-wave-accessibility-summary.png)

![Game Page Wave Test Details](docs/testing/game-page-wave-accessibility-details.png)

* There is 1 alert appearing here about No Page Regions. This is due to the lack of header, section, and footer elemenets. However as divs are constantly appearing and disappearing due to the game functionaility and the responsiveness, there isn't as obvious a set structure or order on this HTML page.

### 404 Page

![404 Page Wave Test](docs/testing/404-page-wave-accessibility-summary.png)

![404 Page Wave Test](docs/testing/404-page-wave-accessibility-details.png)

## JS Hint Report

![JS Hint Report](docs/testing/js-hint-report.png)

* The only alerts I am getting are that async funtions are only available with ES8.

## Bugs

### Solved Bugs

* One bug I initially encountered was that functions would call multiple times rather than the intented once. This was causing duplicated data and player hands to not match with the action taken by the player. The reason this was happen is because each new player function was called inside of the previous using a setTimout, cause a recursion. By only having the the computer player's turns being called within each other. Once it's the player's turn, the the displayHand function is called, which re-enable all the event listeners, and the computer player's turn is only called once the certain event is triggered, whereas before the player's turn was its own function that was called within the last computer player turn function.

* One bug I found was that the discard Pile was not push it's entire contents into the shuffled Pile, stopping at around halfway. The reason this was happening is before with each iteration of the for loop, the discardPile.length was actually getting smaller. So say if the length was 8, and I wanted to iterate through it 8 time, as I was decreasing the length each time, the upper limit of the loop was also decreasing. This fixed by setting the value to a fixed variable before starting to loop, then iterating through the loop that number times. This way I could decrease the discardPile.length without change the upper limit of the for loop.

![Array Upper Limit Bug Fix](docs/testing/array-upper-limit-bug-fix.png)

* Another bug I came across was when a user would click a card in large screen mode, them shift the display from from large screen to mobile view, the game would still allow the user to click on the cards activating the "Play Card?" modal. This would then add add the previous card they clicked in large screen mode, causing potential confusion for players. To fix this whenever the user would click a card in large view mode, this would then remove the data-bs-toggle attribute from the clickable cards in the mobile view hand. The attributes would then be re-added on if the user were to click "no".

![Mobile View Error Fix](docs/testing/mobile-view-error-fix.png)
![Mobile View Error Fix Attribute Attachment](docs/testing/mobile-view-error-fix-attr-attachment.png)

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


