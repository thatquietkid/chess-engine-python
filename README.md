# Python Chess Engine

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [TODO](#todo)
* [Instructions](#instructions)
* [Installation](#installation)
* [Further development ideas](#further-development-ideas)

## General info
With a keen interest in Chess ever since I was a kid, I wanted to learn how to implement it within a computer using coding and then I came across a tutorial by Eddie Sharick, who made a whole 16 episodes series covering the topic.
This repository is a result of following his videos. I highly encourage you to visit his YouTube channel and check the whole series by yourself.

[Eddie's YouTube channel](https://www.youtube.com/channel/UCaEohRz5bPHywGBwmR18Qww)

[First episode of "Chess engine in Python"](https://www.youtube.com/watch?v=EnYui0e73Rs&ab_channel=EddieSharick)

## Technologies
* Python 3.7.8
* pygame 2.0.1

## TODO
- [ ] Using numpy arrays instead of 2d lists.
- [ ] Menu to select player vs player/computer.
- [ ] Allow dragging pieces.

## Instructions
1. Clone this repository.
2. Select whether you want to play versus computer, against another player locally, or watch the game of engine playing against itself by setting appropriate flags in lines 52 and 53 of `ChessMain.py`.

### Installation
- Switch to Python3.
- Follow the code below to install the necessary libraries and run the game locally.
```
git clone https://github.com/thatquietkid/chess-engine-python.git
cd chess-engine-python/Chess/
pip install -r requirements.txt
python ChessMain.py
```

#### Keyboard commands in-game:
* Press `z` to undo a move.
* Press `r` to reset the game.

## Further development ideas
1. Keeping track of all the possible moves in a given position, so that after a move is made the engine doesn't have to recalculate all the moves.
2. Evaluating kings placement on the board (separate in middle game and in the late game).
3. Book of openings.
