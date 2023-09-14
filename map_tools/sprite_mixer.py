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
        theme = 'assets/themes/sprite_mixer_app_theme.json'
        self.manager = pygame_gui.UIManager((args.width, args.height), theme)
        self.sprite_types = ['Symmetric Size',
                             'Similar Size', 'Different Size']
        self._create_gui()

    def _create_gui(self):
        window_rect = self.screen.get_rect()
        self.up_panel = pygame_gui.elements.UIPanel(pygame.Rect(0, 0, window_rect.width * 2 / 3, 40),
                                                    manager=self.manager, object_id="#panel_red")
        self.right_panel = pygame_gui.elements.UIPanel(pygame.Rect(window_rect.width * 2 / 3, 0, window_rect.width / 3, window_rect.height),
                                                       manager=self.manager, object_id="#panel_green")
        self.working_rect = pygame.Rect(
            0, 40, window_rect.width * 2 / 3,  window_rect.height - 40)
        self.left_down_panel = pygame_gui.elements.UIPanel(self.working_rect,
                                                           manager=self.manager, object_id="#panel_blue")
        self.open_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1, 1), (40, 30)),
                                                        text='',
                                                        tool_tip_text='Open an image.',
                                                        manager=self.manager,
                                                        container=self.up_panel,
                                                        object_id='#open_btn')
        self.save_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((41, 1), (40, 30)),
                                                        text='',
                                                        tool_tip_text='Saves the sprites.',
                                                        manager=self.manager,
                                                        container=self.up_panel,
                                                        object_id='#save_btn')

        self.sprite_types_dd_menu = pygame_gui.elements.UIDropDownMenu(self.sprite_types,
                                                                       self.sprite_types[0],
                                                                       pygame.Rect(
                                                                           10, 1, 200, 30),
                                                                       self.manager,
                                                                       container=self.right_panel)

        self.main_image = self._create_main_image()

    def _create_main_image(self, img=None):
        if img == None:
            img = pygame.Surface(
                (self.working_rect.width, self.working_rect .height))

        return pygame_gui.elements.UIImage(relative_rect=pygame.Rect((1, 1), img.get_size()),
                                           image_surface=img,
                                           manager=self.manager,
                                           container=self.left_down_panel,
                                           anchors={'left': 'left',
                                                    'right': 'right',
                                                    'top': 'top',
                                                    'bottom': 'bottom'})

    def _process_events(self, event):
        self._handle_open_file(event)
        self.manager.process_events(event)

    def _handle_open_file(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == self.open_button:
            self.open_file_dialog = create_open_file_dialog(self.manager)
            self.open_button.disable()
        elif event.type == pygame_gui.UI_FILE_DIALOG_PATH_PICKED and event.ui_element == self.open_file_dialog:
            try:
                img = pygame.image.load(create_resource_path(event.text))

                if img.get_size() > self.main_image.image.get_size():
                    rc = self.main_image.get_relative_rect()
                    img = pygame.transform.smoothscale(
                        img, (rc.width, rc.height))
                self.main_image = self._create_main_image(img)

            except pygame.error as e:
                print(e)

        elif (event.type == pygame_gui.UI_WINDOW_CLOSE and event.ui_element == self.open_file_dialog):
            self.open_button.enable()
            self.open_file_dialog = None

    def _update(self, *args, **kwargs):
        self.manager.update(self.fps_delta)

    def _draw(self, surface):
        surface.blit(self.background, (0, 0))
        self.manager.draw_ui(surface)


if __name__ == '__main__':
    args = parse_arguments()
    mixer = SpriteMixer(args)
    mixer.main_loop()
