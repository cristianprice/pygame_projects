import pygame
import sys


class PyGameApp:

    def __init__(self, name="PyGameApp", fps=60, width=960, height=600) -> None:
        pygame.init()
        pygame.display.set_caption(name)
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.actions = []

    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
            for action in self.actions:
                action(self)
            pygame.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    app = PyGameApp()
    app.main_loop()