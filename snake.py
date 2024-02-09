from settings import *


class Snake:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        self.body = [pygame.Vector2(START_COLUMN - column, START_ROW) for column in range(START_LENGTH)]


    def draw(self):
        for point in self.body:
            rectangle = pygame.Rect(point.x * CELL_SIZE, point.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)

            pygame.draw.rect(self.display_surface, 'blue', rectangle)