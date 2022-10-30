from Space import Space
from Position import Position

class Board():

    array = []
    loss = False
    win = False

    def __init__(self):
        self.construct_spaces()
        self.call_count_bombs_around()

    def reset(self):
        self.array = []
        self.construct_spaces()
        self.call_count_bombs_around()
        self.loss = False
        self.win = False

    def construct_spaces(self):
        for i in range(10):
            sub_array = []

            for i2 in range(10):
                pos = Position(i, i2)
                space = Space(pos)
                sub_array.append(space)
            
            self.array.append(sub_array)

    def call_count_bombs_around(self):
        for sub_array in self.array:
            for space in sub_array:
                space.count_bombs_around(self.array)

    
    def count_spaces_cleared(self):
        spaces_cleared = 0

        for sub_array in self.array:
            for space in sub_array:
                if space.clicked == True and space.bomb == False:
                    spaces_cleared += 1
        
        return spaces_cleared


    def count_total_bombs(self):
        bombs = 0

        for sub_array in self.array:
            for space in sub_array:
                if space.bomb == True:
                    bombs += 1
        
        return bombs

    
    def show_all_bombs(self):
        for sub_array in self.array:
            for space in sub_array:
                if space.bomb == True:
                    space.clicked = True

    

       