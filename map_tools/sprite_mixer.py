import argparse

import pygame
import pygame_gui
from utils import PyGameApp

APP_NAME = 'Sprite Mixer'


def parse_arguments():
    parser = argparse.ArgumentParser(
        prog=APP_NAME,
        description='What the program does',
        epilog='Text at the bottom of help')
    parser.add_argument('--fps', type=int, default=60)
    parser.add_argument('--width', type=int, default=1024)
    parser.add_argument('--height', type=int, default=768)
    return parser.parse_args()


class SpriteMixer(PyGameApp):
    def __init__(self, args) -> None:
        super().__init__(name=APP_NAME, fps=args.fps, width=args.width, height=args.height)
        self.manager = pygame_gui.UIManager((args.width, args.height))
        self._create_gui()

    def _create_gui(self):
        self.hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                                         text='Say Hello',
                                                         manager=self.manager)

    def _process_events(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.hello_button:
                print('Hello World!')

        self.manager.process_events(event)

    def _update(self, *args, **kwargs):
        self.manager.update(self.fps_delta)

    def _draw(self, surface):
        surface.blit(self.background, (0, 0))
        self.manager.draw_ui(surface)


if __name__ == '__main__':
    args = parse_arguments()
    mixer = SpriteMixer(args)
    mixer.main_loop()
