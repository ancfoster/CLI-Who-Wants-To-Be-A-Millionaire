# Testing
Click here to return to [README.md](README.md)

## Changes made after user testing

During devleopment I sought user feedback from my mentor and another user. Based on their feedback the following changes were made.

- Removing of previous outputs when the user entered an invalid input.
	- If a user entered an invalid input, like the letter F instead of the letter D the game would output an error message along with their incorrect input. Now the game also removes the previously outputted question and options to keep the terminal output clean and readable.
	
		| Before | After |
		|---|---|
		|![Before main menu](md_assets/menu_before.jpeg)|![After main menu](md_assets/menu_after.jpeg)|

- Messages in the game such as game won/complete/walk away messages disappeared after a number of seconds. During testing this was found to result in a negative user experience, so now the messages remain on the user presses return on their keyboard.

	![Walk away message](md_assets/walk.jpeg)

- The 'How to Play' instruction section used to output all of its text in one go. During testing both of the users did not like this approach. Now sections of text are outputted individually with the user having to press enter in between sections.

	| Before | After |
	|---|---|
	|![How to before](md_assets/how_to_before.jpeg)|![How to after](md_assets/how_to_after.jpeg)|

## Code Validation

**PEP8 validator**

The code passes through the PEP8 validator.

| File | Screenshot |
|---|---|
|run.py|![Test screenshot](md_assets/pep8.jpeg)|

## Defensive programming Testing

- Main menu
	- Invalid input

		![Invalid input](md_assets/invalid_mmain_menu1.jpeg)

- Player name screen
	- Less than 3 characters

		![Less than 3 characters](md_assets/player_less3.jpeg)

	- Non-alpha characters

		![Non-alpha characters](md_assets/player_non-alpha.jpeg)

	- More than 15 characters in length
		
		![More than 15 characters](md_assets/player_more15.jpeg)


- Question screen
	- Users can enter the options A, B, C, D or walk in caps or lowercase the game will permit this to improve the experience.
	- When a non-valid input is entered an erroe message will be displayed.

		![Invalid input 1](md_assets/answer1.jpeg)

		![Invalid input 2](md_assets/answer2.jpeg)

## Browser Compatibility testing

| Screen size | Screenshot |
| --- | --- |
|![Chrome](md_assets/chrome.png)|![Running in Chrome](md_assets/chrome.jpeg)|

| Browser | Screenshot |
| --- | --- |
|![Safari](md_assets/safari.png)|![Running in Safari](md_assets/safari.jpeg)|

| Browser | Screenshot |
| --- | --- |
|![Firefox](md_assets/firefox.png)|![Running in Firefox](md_assets/firefox.jpeg)|


## Responsive Testing

| Browser | Screenshot |
| --- | --- |
|iPhone SE 2 (375 x 667)|![Running in Chrome](md_assets/iphonese.jpeg)|

| Browser | Screenshot |
| --- | --- |
|Nexus 7 Tablet (600 x 960)|![Running in Safari](md_assets/nexus.jpeg)|

| Browser | Screenshot |
| --- | --- |
|Laptop MDPI (1200 x 800)|![Running in Firefox](md_assets/laptop.jpeg)|

## User Story Testing

- I would like to play a trivia game with questions of increasing difficulty.

	![Increasing difficulty questions](md_assets/harder.jpg)

- I would like to keep track of game scores by different players.

	![Scores](md_assets/scores.png)