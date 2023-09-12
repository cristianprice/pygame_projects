import argparse

import pygame
import pygame_gui
from pygame_gui.core.utility import create_resource_path

from sprite_mixer_utils import create_open_file_dialog
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
        self.manager = pygame_gui.UIManager(
            (args.width, args.height), 'assets/themes/sprite_mixer_app_theme.json')
        self._create_gui()

    def _create_gui(self):
        self.open_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1, 1), (70, 30)),
                                                        text='Open',
                                                        tool_tip_text='Opens an image',
                                                        manager=self.manager)

    def _process_events(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == self.open_button:
            self._handle_open_file(event)
        elif event.type == pygame_gui.UI_FILE_DIALOG_PATH_PICKED and event.ui_element == self.open_file_dialog:
            image_path = create_resource_path(event.text)
            print('Picked :', image_path)
        elif (event.type == pygame_gui.UI_WINDOW_CLOSE
              and event.ui_element == self.open_file_dialog):
            self.open_button.enable()
            self.open_file_dialog = None
        elif event.type == pygame_gui.UI_SELECTION_LIST_DOUBLE_CLICKED_SELECTION:
            print('Double click: ', event.ui_element)

        self.manager.process_events(event)

    def _handle_open_file(self, event):
        if event.ui_element == self.open_button:
            self.open_file_dialog = create_open_file_dialog(self.manager)
            self.open_button.disable()

    def _update(self, *args, **kwargs):
        self.manager.update(self.fps_delta)

    def _draw(self, surface):
        surface.blit(self.background, (0, 0))
        self.manager.draw_ui(surface)


if __name__ == '__main__':
    args = parse_arguments()
    mixer = SpriteMixer(args)
    mixer.main_loop()
