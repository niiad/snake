from settings import *


class Snake:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        self.body = [pygame.Vector2(START_COLUMN - column, START_ROW) for column in range(START_LENGTH)]