# Chess
Chess game created using `python` and `pygame`
## Installation

**NOTE**: Python 3.7 or higher is required to run the game.

```bash
# clone the repo
$ git clone https://github.com/tahazulfiqar/csc290.git

# change the working directory to csc290
$ cd csc290

# install pygame (version 1.9.7 or higher) if it is not already installed
$ python3 -m pip install -U pygame --user

# run GUI.py to start the game
$ GUI.py
```

If further help is needed to install pygame, go to:
https://www.pygame.org/wiki/GettingStarted

## How To Play
When the game launches, the user will be greeted with a title screen where the user can either start the game or change settings.

![Image title screen](https://github.com/tahazulfiqar/csc290/blob/master/Screenshots/menu.PNG)

In the settings screen, the user can choose to display a timer by clicking the timer button.

![Image settings screen](https://github.com/tahazulfiqar/csc290/blob/master/Screenshots/settings.PNG)

After clicking start, the board and pieces will appear in their starting positions. The user can now click on the pieces, which will either flash red if the piece does not belong to the current player, or highlight all the possible moves that the selected piece can move to. Clicking on a possible move will move the selected piece to that position. 

![Image settings screen](https://github.com/tahazulfiqar/csc290/blob/master/Screenshots/capture1.PNG)
![Image settings screen](https://github.com/tahazulfiqar/csc290/blob/master/Screenshots/capture2.PNG)

Chess is a turn based game so after every move, the other player makes the next move. This continues until a player checkmates (when the King is under attack or in "check" and every possible move by the King will also put it in check) the opponent, and the game ends. Our game do not have CPU opponents yet so it is currently a two player game only.

Since all the valid moves are highlighted, this game does not require any knowledge of chess to play. However, you can click [here](https://www.chess.com/learn-how-to-play-chess) if you are interested to learn more.

## Documentation
In our game's current form there are two main classes that we ended up using. The board class and the gui class. I will briefly describe the purpose of each class below:
### Board Class
The board class acts as a representation of the chess board and holds all the positions of the pieces in a nested list. Tiles that are empty are represented in the nested list as a 0. The board class is also responsible for checking the valid moves of selected pieces and actually moving the pieces that the player has moved. In the board class there are a few main functions described below:
#### create_board():
This is where the chess board nested list is created and all the pieces are placed in their starting positions. If you wanted to change the initial starting positions of the pieces this is where you would do it.
#### move(old_coord, new_coord)::
Allows the piece at coordinate old_cord to new_cord. This function is called when the user executes their move.
#### get_valid_moves(self, coordinate):
If a piece is at coordinate, it returns the a list of tuples - where each tuple represents a valid coordinate it can move to. 
Unique helper functions were created for each piece - for example the logic of the Knight piece movement was done so in the helper function get_knight_moves() - which is potentially called if knight is a coordinate. 


## Individual Contributions

## License information
MIT License

Copyright (c) 2019 CSC290Chess

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

