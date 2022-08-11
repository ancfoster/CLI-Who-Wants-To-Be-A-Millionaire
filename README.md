# CLI Who Wants To Be A Millionaire

CLI Who Wants To Be A Millionaire is a Python command line trivia game based on the TV show of the same name. 

## Design Process

### UX Design Process

### Game Design
- Here is the flowchart that I used to plan out the logic of the game to help me when writing the game code. 

 flow chart will go here

- The game consists of 15 general knowledge trivia questions. These questions get harder as the player progresses through the game.
- The questions are valued at progressively higher sums of money, up to the top prize of £1,000,000
- The objective of the game is to try and 'win' £1,000,000.
- For each question there are four options to choose from, labelled ‘A’, ‘B’, ‘C’ and ‘D’. 
- Two monetary milestones are provided. In this version of the game they are £50,000 (reached after successfully answering question 10) and £1,000 (reeached after successfully answering question 5)
- A player can 'walk away' from any question, with the last successfully answered question being the 'prize' they walk away with. 


## Features
### Existing Features
- The game features 15 multiple choice questions.
- Input validation
	- If a user enters an invalid input like the letter 'n' instead of the letter 'b' the game will recognise this and ask the user to enter a correct input and inform them of the incorrect input they entered. 
	- This is defensive design and is a good UX practice. Every single input within the game will catch invalid inputs and allow the user to reinput.
- Score system
	- At the beginning of each game the player is asked to input their name. This is then used to populate a Google sheet with all of the different scores.
	- Within the game the user can input 'scores' from the main menu and be presented with a list of the 10 most recent scores, who achieved those scores and on what date.
- How to
	- The game feature a built in guide explaining the rules and objectives of the game.
- Connection to Google Worksheet
	- All of the game questions are stored in a Google worksheet made up of three sheets of questions.
	- The different sheets contain questions of different difficulty. There is an easy questions sheet, medium questions sheet, hard questions sheet.
	- The use of sheets in this way makes it very easy for additional questions to be added to the game, or out of date questions to be removed. 

### Features Left to Implement


## Technologies Used

- Python - the game was coded in the Python programming language ans uses Python version 3
- Google Sheets
- Google API 

## Tools used
- For writing code I used [Visual Studio Code](https://code.visualstudio.com/) which I also for Git commands and pushing to GitHub

- [GitHub](https://github.com]) was used for hosting the online repository, it provides an online version of Git, a source code management tool.

- [Markdown Editor](https://apps.apple.com/ie/app/markdown-editor/id1458220908?mt=12) by Satoshi Iwaki was used for editing .MD files.


## Testing

- For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The site was deployed to GitHub pages. The steps to deploy are as follows:
- In the [GitHub repository](https://github.com/ancfoster/flags-and-countries), navigate to the Settings tab
- From the source section drop-down menu, select the Main Branch, then click "Save".
- The page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.
- The live link can be found [here](https://ancfoster.github.io/flags-and-countries/).

### Local Deployment

In order to make a local copy of this project, you can clone it. In your IDE Terminal, type the following command to clone my repository:

`git clone https://github.com/ancfoster/CLI-Who-Wants-To-Be-A-Millionaire`

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in GitPod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/ancfoster/CLI-Who-Wants-To-Be-A-Millionaire)

## Credits

### Technical documentation & tutorials




### Acknowledgements
I would like to thank: