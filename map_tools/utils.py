import pygame
import sys


class PyGameApp:

    def __init__(self, name="PyGameApp", fps=60, width=960, height=600) -> None:
        pygame.init()
        pygame.display.set_caption(name)
        self.screen = pygame.display.set_mode(
            (width, height), flags=pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.fps_delta = fps/1000.0

        self.background = self._create_black_background(width, height)

    def _create_black_background(self, width, height):
        background = pygame.Surface((width, height))
        background.fill(pygame.Color('#000000'))

        return background

    def _process_events(self, event):
        pass

    def _update(self, *args, **kwargs):
        pass

    def _draw(self, surface):
        pass

    def main_loop(self):
        while True:
            self.fps_delta = self.clock.tick(self.fps)/1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                self._process_events(event)

            self._update()
            self._draw(self.screen)
            pygame.display.update()
