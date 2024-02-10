from settings import *

class Apple:
    def __init__(self) -> None:
        self.position = pygame.Vector2(5, 8)
        self.display_surface = pygame.display.get_surface()


    def draw(self):
        pygame.draw.rect(self.display_surface, "yellow", 
                         pygame.Rect(self.position.x * CELL_SIZE, self.position.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))