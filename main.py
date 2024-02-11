from settings import *

from snake import Snake
from apple import Apple

class Main:
    def __init__(self) -> None:
        pygame.init()

        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        pygame.display.set_caption("snake")

        self.background_rectangles = [pygame.Rect((column + int(row % 2 == 0)) * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE) 
                                      for column in range(0, COLUMNS, 2)
                                      for row in range(ROWS)]
        
        self.snake = Snake()
        self.apple = Apple(self.snake)


    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.display_surface.fill(LIGHT_GREEN)

            self.draw_background()

            self.snake.draw()
            self.apple.draw()

            pygame.display.update()


    def draw_background(self):
        for rectangle in self.background_rectangles:
            pygame.draw.rect(self.display_surface, DARK_GREEN, rectangle)


if __name__ == "__main__":
    main = Main()

    main.run()