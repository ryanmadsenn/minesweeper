import sys, pygame
from Board import Board
from Clock import Clock
from VideoService import VideoService
from InputHandler import InputHandler


def main():

    board = Board()
    clock = Clock()
    video_service = VideoService(board, clock)
    input_handler = InputHandler(board, video_service, clock)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: input_handler.handle_click()

        video_service.draw_board()
        clock.update_time()


if __name__ == "__main__":
    main()