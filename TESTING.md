# Testing
Click here to return to [README.md](README.md)

## Changes made after user testing

During devleopment I sought user feedback from my mentor and another user. Based on their feedback the follwing changes were made.

- Removing of previous outputs when the entered an invalid input.
	- If a user entered an invalid input, like the letter F instead of D the game would output an error message along with their incorrect input. Now the game also removes the previously outputted question and options to keep the terminal output clean and readable.
	
		| Before | After |
		|---|---|
		|![Before main menu](md_assets/menu_before.jpeg)|![After main menu](md_assets/menu_after.jpeg)|

- Messages in the game such as game won/complete/walk away messages disappeared after a number of seconds. During testing this was found to result in a negative user experience, so now the messages remain on the screen until a key is pressed on the keyboard.

	![Walk away message](md_assets/walk.jpeg)

- The 'How to Play' instruction section used to output all of its text in one go. During testing both of the users did not like this approach. Instead paragraphs of text are outputted individually and to continue reading the user presses the enter key.

	| Before | After |
	|---|---|
	|![How to before](md_assets/how_to_before.jpeg)|![How to after](md_assets/how_to_after.jpeg)|

## Code Validation

**PEP8 validator**

The code passes through the validator except for two lines which are too long because of long variable names.
These lines are commented as `# noqa`

| File | Screenshot |
|---|---|
|run.py|![Test screenshot](md_assets/pep8.jpeg)|

## User Story Testing