import pygame
import os


class VideoService:
    board = None
    clock = None
    screen = None

    size = (400, 450)
    black = 0, 0, 0

    font = None
    font_size = 30

    smiley = None
    frowney = None
    is_bomb = None
    flag = None
    __path__ = os.path.dirname(os.path.abspath(__file__))

    def __init__(self, board, clock):
        self.board = board
        self.clock = clock
        self.initialize()

    def initialize(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Minesweeper")

        self.font = pygame.font.Font(
            f"{self.__path__}/VCR_OSD_MONO_1.001.ttf",
            self.font_size,
        )
        self.load_images()

    def load_images(self):
        self.smiley = pygame.image.load(f"{self.__path__}/images/smiley.png")
        self.frowney = pygame.image.load(f"{self.__path__}/images/omg.png")
        self.is_bomb = pygame.image.load(f"{self.__path__}/images/bomb.png")
        self.flag = pygame.image.load(f"{self.__path__}/images/flag.png")

    def draw_board(self):
        self.screen.fill(self.black)
        self.draw_header()
        self.draw_spaces()

        if self.board.win:
            self.draw_win_message()

        pygame.display.flip()

    def draw_header(self):
        header_outline = pygame.Rect(0, 1, 400, 41)
        pygame.draw.rect(self.screen, (100, 100, 100), header_outline, 2)
        header_background = pygame.Rect(2, 3, 396, 37)
        pygame.draw.rect(self.screen, (150, 150, 150), header_background, 0)

        smiley_background = pygame.Rect(0, 0, 35, 35)
        smiley_background.center = (200, 21)
        pygame.draw.rect(self.screen, (100, 100, 100), smiley_background, 2)

        if not self.board.loss:
            smiley_rect = self.smiley.get_rect()
            smiley_rect.center = (200, 21)
            # self._rect.inflate_ip(10, 10)

            self.screen.blit(self.smiley, smiley_rect)
        else:
            frowney_rect = self.smiley.get_rect()
            frowney_rect.center = (200, 21)
            # frowney_rect.inflate_ip(10, 10)

            self.screen.blit(self.frowney, frowney_rect)

        time_outline = pygame.Rect(0, 0, 95, 30)
        time_outline.top = 6
        time_outline.right = 396
        pygame.draw.rect(self.screen, (100, 100, 100), time_outline, 2)

        time_text = self.font.render(
            f"{str(self.clock.minutes_elapsed).zfill(2)}:{str(self.clock.seconds_elapsed).zfill(2)}",
            True,
            (235, 64, 52),
            None,
        )
        time_rect = time_text.get_rect()
        time_rect.top = 6
        time_rect.right = 394
        self.screen.blit(time_text, time_rect)

        time_outline = pygame.Rect(0, 0, 40, 30)
        time_outline.top = 6
        time_outline.left = 4
        pygame.draw.rect(self.screen, (100, 100, 100), time_outline, 2)

        squares_cleared_text = self.font.render(
            f"{str(self.board.count_spaces_cleared()).zfill(2)}",
            True,
            (235, 64, 52),
            None,
        )
        time_rect = squares_cleared_text.get_rect()
        time_rect.top = 6
        time_rect.left = 6
        self.screen.blit(squares_cleared_text, time_rect)

    def draw_spaces(self):
        top = 40
        for sub_array in self.board.array:
            left = 0
            for space in sub_array:
                if space.clicked == False:
                    square = pygame.Rect(left + 2, top + 2, 36, 36)
                    pygame.draw.rect(self.screen, (150, 150, 150), square, 0)
                    outline = pygame.Rect(left, top + 1, 40, 40)
                    pygame.draw.rect(self.screen, (100, 100, 100), outline, 2)

                    if space.flagged:
                        # flag_text = font.render(f"!", True, (235, 64, 52), None)
                        flag_rect = self.flag.get_rect()
                        flag_rect.top = top + 4
                        flag_rect.left = left + 5
                        self.screen.blit(self.flag, flag_rect)

                elif space.is_bomb == False:
                    color = self.determine_color(space.bombs_around)

                    outline = pygame.Rect(left, top + 1, 40, 40)
                    pygame.draw.rect(self.screen, (130, 130, 130), outline, 2)

                    square = pygame.Rect(left + 2, top + 3, 36, 36)
                    pygame.draw.rect(self.screen, (240, 240, 240), square, 0)

                    text = self.font.render(str(space.bombs_around), True, color, None)
                    text_rect = text.get_rect()
                    text_rect.left = left + 12
                    text_rect.top = top + 5
                    # pygame.draw.rect(self.screen, (130,130,130), text_rect, 0)
                    self.screen.blit(text, text_rect)
                else:
                    outline = pygame.Rect(left, top + 1, 40, 40)
                    pygame.draw.rect(self.screen, (130, 130, 130), outline, 2)

                    square = pygame.Rect(left + 2, top + 3, 36, 36)
                    pygame.draw.rect(self.screen, (240, 240, 240), square, 0)

                    bomb_rect = self.is_bomb.get_rect()
                    bomb_rect.left = left + 6
                    bomb_rect.top = top + 5
                    # pygame.draw.rect(self.screen, (130,130,130), bomb_rect, 0)
                    self.screen.blit(self.is_bomb, bomb_rect)

                left += 40

            top += 40

    def draw_win_message(self):
        text_background = pygame.Rect(0, 0, 160, 40)
        text_background.center = (200, 200)
        pygame.draw.rect(self.screen, (130, 130, 130), text_background, 0)

        text_outline = pygame.Rect(0, 0, 160, 40)
        text_outline.center = (200, 200)
        pygame.draw.rect(self.screen, (100, 100, 100), text_outline, 2)

        text = self.font.render(str("YOU WIN!"), True, (235, 64, 52), None)
        text_rect = text.get_rect()
        text_rect.center = (202, 199)
        # pygame.draw.rect(self.screen, (130,130,130), text_rect, 0)
        self.screen.blit(text, text_rect)

    def determine_color(self, num):
        if num == 0:
            color = (240, 240, 240)
        if num == 1:
            color = (35, 35, 160)
        elif num == 2:
            color = (60, 160, 30)
        elif num > 2:
            color = (235, 64, 52)

        return color
