import random

class Space():

    bomb = False
    bombs_around = None
    clicked = False
    pos = None
    flagged = False


    def __init__(self, position):
        num = random.randint(1,100)

        if num < 20:
            self.bomb = True

        self.pos = position

    
    def count_bombs_around(self, board):
        posX = self.pos.X
        posY = self.pos.Y
        count = 0

        if posY not in [0, 9] and posX not in [0,9]:
            # Check 3 spaces above.
            for i in range(posY - 1, posY + 2):
                if board[posX - 1][i].bomb == True:
                    count += 1

            # Check 3 spaces below.
            for i in range(posY - 1, posY + 2):
                if board[posX + 1][i].bomb == True:
                    count += 1

            # Check spaces to either side.
            if board[posX][posY - 1].bomb == True:
                count += 1
            if board[posX][posY + 1].bomb == True:
                count += 1

        # If space is on left edge of board.
        elif posY == 0 and posX not in [0, 9]:
            # Check 2 spaces above.
            for i in range(posY, posY + 2):
                if board[posX - 1][i].bomb == True:
                    count += 1

            # Check 2 spaces below.
            for i in range(posY, posY + 2):
                if board[posX + 1][i].bomb == True:
                    count += 1

            # Check space to the right.
            if board[posX][posY + 1].bomb == True:
                count += 1

        # If space is on right edge of the board.
        elif posY == 9 and posX not in [0, 9]:
            # Check 2 spaces above.
            for i in range(posY - 1, posY + 1):
                if board[posX - 1][i].bomb == True:
                    count += 1

            # Check 2 spaces below.
            for i in range(posY - 1, posY + 1):
                if board[posX + 1][i].bomb == True:
                    count += 1

            # Check space to the left.
            if board[posX][posY - 1].bomb == True:
                count += 1

        # If space is on top edge of board.
        elif posY not in [0,9] and posX == 0:
            # Check 2 spaces below.
            for i in range(posY - 1, posY + 2):
                if board[posX + 1][i].bomb == True:
                    count += 1

            # Check space to the left.
            if board[posX][posY - 1].bomb == True:
                count += 1

            # Check space to the right.
            if board[posX][posY + 1].bomb == True:
                count += 1

        # If space is on bottom edge of board.
        elif posY not in [0,9] and posX == 9:
            # Check 2 spaces above.
            for i in range(posY - 1, posY + 2):
                if board[posX - 1][i].bomb == True:
                    count += 1

            # Check space to the left.
            if board[posX][posY - 1].bomb == True:
                count += 1

            # Check space to the right.
            if board[posX][posY + 1].bomb == True:
                count += 1
 
        # If space is in top left corner.
        elif posY == 0 and posX == 0:
            # Check 2 spaces below.
            for i in range(posY, posY + 2):
                if board[posX + 1][i].bomb == True:
                    count += 1

            # Check space to the right.
            if board[posX][posY + 1].bomb == True:
                count += 1

        # If space is in bottom left corner
        elif posY == 0 and posX == 9:
            # Check 2 spaces above.
            for i in range(posY, posY + 2):
                if board[posX - 1][i].bomb == True:
                    count += 1

            # Check space to the right.
            if board[posX][posY + 1].bomb == True:
                count += 1

        # If space is in top right corner.
        elif posY == 9 and posX == 0:
            # Check 2 spaces below.
            for i in range(posY - 1, posY + 1):
                if board[posX + 1][i].bomb == True:
                    count += 1

            # Check space to the left.
            if board[posX][posY - 1].bomb == True:
                count += 1

        # If space is in bottom right corner.
        elif posY == 9 and posX == 9:
            # Check 2 spaces above.
            for i in range(posY - 1, posY + 1):
                if board[posX - 1][i].bomb == True:
                    count += 1

            # Check space to the left.
            if board[posX][posY - 1].bomb == True:
                count += 1

        self.bombs_around = count