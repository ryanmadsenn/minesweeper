import pygame, math
from Position import Position


class InputHandler:
    RESET = "reset"
    board = None
    video_service = None
    clock = None

    def __init__(self, board, video_service, clock):
        self.board = board
        self.video_service = video_service
        self.clock = clock

    def handle_click(self):
        mouse_pos = pygame.mouse.get_pos()
        space_clicked = self.determine_space_clicked(mouse_pos)

        if space_clicked == self.RESET:
            self.board.reset()
            self.clock.reset()
            return

        if pygame.mouse.get_pressed()[0]:
            if self.board.array[space_clicked.X][space_clicked.Y].is_bomb:
                self.board.loss = True
                self.board.show_all_bombs()
            elif (
                self.board.array[space_clicked.X][space_clicked.Y].bombs_around == 0
                and not self.board.loss
            ):
                self.cascade_empty_spaces(space_clicked)
            elif (
                self.board.array[space_clicked.X][space_clicked.Y].bombs_around > 0
                and not self.board.loss
            ):
                self.board.array[space_clicked.X][space_clicked.Y].clicked = True

            if self.board.count_spaces_cleared() == (
                100 - self.board.count_total_bombs()
            ):
                self.board.win = True

        elif pygame.mouse.get_pressed()[2]:
            if self.board.array[space_clicked.X][space_clicked.Y].flagged == False:
                self.board.array[space_clicked.X][space_clicked.Y].flagged = True
            elif self.board.array[space_clicked.X][space_clicked.Y].flagged == True:
                self.board.array[space_clicked.X][space_clicked.Y].flagged = False

    def cascade_empty_spaces(self, space_clicked):
        self.board.array[space_clicked.X][space_clicked.Y].clicked = True

        if self.board.array[space_clicked.X][space_clicked.Y].bombs_around > 0:
            return

        # Check space above.
        if (
            (space_clicked.X - 1 >= 0)
            and (space_clicked.X - 1 < len(self.board.array))
            and not self.board.array[space_clicked.X - 1][space_clicked.Y].clicked
        ):
            next_space = Position(space_clicked.X - 1, space_clicked.Y)
            self.cascade_empty_spaces(next_space)

        # Check space to the right.
        if (
            (space_clicked.Y + 1 >= 0)
            and (space_clicked.Y + 1 < len(self.board.array[space_clicked.X]))
            and not self.board.array[space_clicked.X][space_clicked.Y + 1].clicked
        ):
            next_space = Position(space_clicked.X, space_clicked.Y + 1)
            self.cascade_empty_spaces(next_space)

        # Check space to the left.
        if (
            (space_clicked.Y - 1 >= 0)
            and (space_clicked.Y - 1 < len(self.board.array[space_clicked.X]))
            and not self.board.array[space_clicked.X][space_clicked.Y - 1].clicked
        ):
            next_space = Position(space_clicked.X, space_clicked.Y - 1)
            self.cascade_empty_spaces(next_space)

        # Check space above.
        if (
            (space_clicked.X + 1 >= 0)
            and (space_clicked.X + 1 < len(self.board.array))
            and not self.board.array[space_clicked.X + 1][space_clicked.Y].clicked
        ):
            next_space = Position(space_clicked.X + 1, space_clicked.Y)
            self.cascade_empty_spaces(next_space)

        # Check top left corner.
        if (
            (space_clicked.X - 1 >= 0)
            and (space_clicked.X - 1 < len(self.board.array))
            and (space_clicked.Y - 1 >= 0)
            and (space_clicked.Y - 1 < len(self.board.array))
            and not self.board.array[space_clicked.X - 1][space_clicked.Y - 1].clicked
        ):
            next_space = Position(space_clicked.X - 1, space_clicked.Y - 1)
            self.cascade_empty_spaces(next_space)

        # Check top right corner.
        if (
            (space_clicked.X - 1 >= 0)
            and (space_clicked.X - 1 < len(self.board.array))
            and (space_clicked.Y + 1 >= 0)
            and (space_clicked.Y + 1 < len(self.board.array[space_clicked.X]))
            and not self.board.array[space_clicked.X - 1][space_clicked.Y + 1].clicked
        ):
            next_space = Position(space_clicked.X - 1, space_clicked.Y + 1)
            self.cascade_empty_spaces(next_space)
        # Check bottom left corner.
        if (
            (space_clicked.X + 1 >= 0)
            and (space_clicked.X + 1 < len(self.board.array))
            and (space_clicked.Y - 1 >= 0)
            and (space_clicked.Y - 1 < len(self.board.array[space_clicked.X]))
            and not self.board.array[space_clicked.X + 1][space_clicked.Y - 1].clicked
        ):
            next_space = Position(space_clicked.X + 1, space_clicked.Y - 1)
            self.cascade_empty_spaces(next_space)

        # Check bottom right corner.
        if (
            (space_clicked.X + 1 >= 0)
            and (space_clicked.X + 1 < len(self.board.array))
            and (space_clicked.Y + 1 >= 0)
            and (space_clicked.Y + 1 < len(self.board.array))
            and not self.board.array[space_clicked.X + 1][space_clicked.Y + 1].clicked
        ):
            next_space = Position(space_clicked.X + 1, space_clicked.Y + 1)
            self.cascade_empty_spaces(next_space)

        return

    def determine_space_clicked(self, mouse_pos):
        if (
            mouse_pos[0] > 180
            and mouse_pos[0] < 220
            and mouse_pos[1] > 3
            and mouse_pos[1] < 39
        ):
            return self.RESET

        posX = math.floor((mouse_pos[1] - 40) / 40)
        posY = math.floor(mouse_pos[0] / 40)

        return Position(posX, posY)
